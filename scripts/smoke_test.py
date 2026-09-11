#!/usr/bin/env python3
"""Dependency-free smoke checks for the static site published from this repository."""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys


SITE_ROOT = Path(__file__).resolve().parents[1]
PAGES = (
    Path("index.html"),
    Path("presentation.html"),
    Path("ai/index.html"),
    Path("ai/presentation.html"),
)
REQUIRED_REFERENCES = {
    Path("index.html"): {
        ("a", "href", "presentation.html"),
        ("iframe", "src", "presentation.html"),
    },
    Path("presentation.html"): {("img", "src", "msf-showgarden.jpg")},
    Path("ai/index.html"): {
        ("a", "href", "../"),
        ("a", "href", "presentation.html"),
        ("iframe", "src", "presentation.html"),
    },
}
IGNORED_SCHEMES = {"data", "mailto", "tel", "javascript"}


class Document(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.tags: set[str] = set()
        self.links: list[str] = []
        self.references: set[tuple[str, str, str]] = set()
        self._in_title = False
        self.title_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.tags.add(tag)
        if tag == "title":
            self._in_title = True
        for name, value in attrs:
            if name in {"href", "src"} and value:
                self.links.append(value)
                self.references.add((tag, name, value))

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._in_title = False

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self.title_parts.append(data)


def local_target(source: Path, reference: str) -> Path | None:
    parsed = urlsplit(reference)
    if parsed.scheme or parsed.netloc or parsed.scheme in IGNORED_SCHEMES:
        return None
    if not parsed.path:
        return None

    path = unquote(parsed.path)
    target = (SITE_ROOT / path.lstrip("/") if path.startswith("/") else source.parent / path).resolve()
    try:
        target.relative_to(SITE_ROOT)
    except ValueError:
        return None
    if target.is_dir():
        target /= "index.html"
    return target


def main() -> int:
    failures: list[str] = []

    for relative_page in PAGES:
        page = SITE_ROOT / relative_page
        if not page.is_file():
            failures.append(f"Missing public page: {relative_page}")
            continue

        content = page.read_text(encoding="utf-8")
        if not content.lstrip().lower().startswith("<!doctype html>"):
            failures.append(f"{relative_page}: missing HTML doctype")

        document = Document()
        document.feed(content)
        if "html" not in document.tags or "body" not in document.tags:
            failures.append(f"{relative_page}: missing html or body element")
        if not "".join(document.title_parts).strip():
            failures.append(f"{relative_page}: missing page title")

        for required in REQUIRED_REFERENCES.get(relative_page, set()):
            if required not in document.references:
                tag, attribute, value = required
                failures.append(
                    f"{relative_page}: missing required <{tag} {attribute}={value!r}> reference"
                )

        for reference in document.links:
            target = local_target(page, reference)
            if target is not None and not target.is_file():
                failures.append(
                    f"{relative_page}: local link {reference!r} points to missing {target.relative_to(SITE_ROOT)}"
                )

    if failures:
        print("Static-site smoke test failed:", *failures, sep="\n- ")
        return 1

    print(f"Static-site smoke test passed for {len(PAGES)} public pages.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
