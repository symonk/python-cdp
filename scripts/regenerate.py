#!/bin/env python
import pathlib
import subprocess
import sys


def main() -> int:
    shell = subprocess.run(["poetry", "shell"])
    t1 = subprocess.run(["tox", "-e", "generate"])
    for _ in range(3):  # We need to do this 3 times now.
        _ = subprocess.run(["tox", "-e", "linting"])
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
