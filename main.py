"""Lime3ds Desktop — A local helper for Lime3ds save-state folders, config and BIOS-path files, and photo albums on Windows and macOS."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='lime3ds_desktop',
        description='A local helper for Lime3ds save-state folders, config and BIOS-path files, and photo albums on Windows and macOS.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Lime3ds Desktop')
    print('Keep the Lime3ds save-state folder tidy before an update.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
# small fix (2026-11-03)
# tweak (2026-11-03)
# refactor bit (2026-11-04)
# minor adjust (2026-11-05)
# cleanup (2026-11-05)
# minor adjust (2026-11-05)
