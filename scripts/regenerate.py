#!/bin/env python
import subprocess


def main() -> int:
    _ = subprocess.run(["poetry", "shell"])
    _ = subprocess.run(["tox", "-e", "generate"])
    # necessary multiple times for the short term.  Todo: Generate files accurately.
    for _ in range(3):
        _ = subprocess.run(["tox", "-e", "linting"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
