import subprocess


def main() -> int:
    """A simple utility for automatically upgrading the submodule version of the chrome
    devtools protocol to the latest.""" 
    proc = subprocess.run(["git", "submodule", "foreach", "git" "pull", "origin", "master"])
    if proc.returncode:
        subprocess.run(["git", "add", "devtools-protocol"])
        subprocess.run(["git", "commit", "-a", "-m", ":rocket: Updating devtools-protocol submodule"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())