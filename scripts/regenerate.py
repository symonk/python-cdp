#!/bin/env python
import sys
import subprocess
import pathlib


def main() -> int:
    abs_path = pathlib.Path(__file__).parents[1] / "python_cdp.generate"
    _ = subprocess.run([sys.executable, "-m", abs_path.absolute()])
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
