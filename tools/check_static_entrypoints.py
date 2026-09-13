#!/usr/bin/env python3
"""Check that the published static entrypoints and their local assets exist.

This intentionally does not fetch or validate third-party CDN URLs: availability
of those services is outside this repository's control.
"""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse
import sys


ROOT = Path(__file__).resolve().parents[1]
ENTRYPOINTS = (ROOT / "index.html", ROOT / "presentation.html")


class ReferenceCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.title = ""
        self._in_title = False
        self.references: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "title":
            self._in_title = True
        if tag in {"img", "script", "link"}:
            for attribute in ("src", "href"):
                if values.get(attribute):
                    self.references.append(values[attribute])

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._in_title = False

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self.title += data


def is_local_reference(reference: str) -> bool:
    parsed = urlparse(reference)
    return not parsed.scheme and not parsed.netloc and not reference.startswith("#")


def check_entrypoint(path: Path) -> list[str]:
    parser = ReferenceCollector()
    parser.feed(path.read_text(encoding="utf-8"))
    errors = []
    if not parser.title.strip():
        errors.append(f"{path.name}: missing a non-empty <title>")
    for reference in parser.references:
        if not is_local_reference(reference):
            continue
        asset = (path.parent / unquote(urlparse(reference).path)).resolve()
        if not asset.is_relative_to(ROOT) or not asset.is_file():
            errors.append(f"{path.name}: missing local asset {reference!r}")
    return errors


def main() -> int:
    errors = []
    for entrypoint in ENTRYPOINTS:
        if not entrypoint.is_file():
            errors.append(f"missing entrypoint: {entrypoint.name}")
        else:
            errors.extend(check_entrypoint(entrypoint))
    if errors:
        print("Static entrypoint check failed:", *errors, sep="\n- ", file=sys.stderr)
        return 1
    print("Static entrypoint check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
