#!/bin/env python
import subprocess


def main() -> int:
    _ = subprocess.run(["poetry", "shell"])
    _ = subprocess.run(["tox", "-e", "generate"])
    # We need to do this 3 times now until we are further on and stop relying on linter fixes to make files pep8 compliant etc.
    for _ in range(3):  
        _ = subprocess.run(["tox", "-e", "linting"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
