"""
A simple module for automatically generating mkdocs based on python docstrings throughout the package.
"""
from pathlib import Path
import itertools
import mkdocs_gen_files

nav = mkdocs_gen_files.Nav()

PROTOCOL_FILES = Path("python_cdp").joinpath("cdp").rglob("*.py")
CLIENT_FILES = Path("python_cdp").joinpath("client").rglob("*.py")


for path in sorted(itertools.chain(PROTOCOL_FILES, CLIENT_FILES)): 
    module_path = path.relative_to("python_cdp").with_suffix("")  #
    doc_path = path.relative_to("python_cdp").with_suffix(".md")  #
    full_doc_path = Path("reference", doc_path)  #
    parts = list(module_path.parts)

    if parts[-1] == "__init__":  #
        parts = parts[:-1]
        doc_path = doc_path.with_name("index.md")
        full_doc_path = full_doc_path.with_name("index.md")
    elif parts[-1] == "__main__":
        continue

    if not parts:
        continue

    nav[parts] = doc_path.as_posix()

    with mkdocs_gen_files.open(full_doc_path, "w") as fd:  #
        identifier = ".".join(parts)  #
        print("::: " + identifier, file=fd)  #
    mkdocs_gen_files.set_edit_path(full_doc_path, path)  #

with mkdocs_gen_files.open("reference/SUMMARY.md", "w") as nav_file:
    nav_file.writelines(nav.build_literate_nav())