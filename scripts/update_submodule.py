#!/bin/env python
import subprocess
import re
import pathlib

ROLL_UP_PATTERN = re.compile(r".*Roll protocol to (\w+)")
SUBMODULE_DIR = str(pathlib.Path(__file__).parents[1] / "devtools-protocol")


def main() -> int:
    """A simple utility for automatically upgrading the submodule version of the chrome devtools protocol to the
    latest."""
    proc = subprocess.run(["git", "submodule", "foreach", "git", "pull", "origin", "master"])
    if not proc.returncode:
        subprocess.run(["git", "add", "devtools-protocol/"])
        message = ":rocket: Updating devtools protocol"
        commit_message = subprocess.run(["git", "--no-pager", "log", "--decorate=short", "--pretty=oneline", "-n1"], stdout=subprocess.PIPE, cwd=SUBMODULE_DIR).stdout.decode("utf-8")
        if (match := ROLL_UP_PATTERN.match(commit_message)) is not None:
            message += f" \`{match.groups()[0]}\`"
        subprocess.run(["git", "commit", "-a", "-m", message])
        subprocess.run(["git", "push"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
