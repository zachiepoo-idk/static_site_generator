import os
import shutil
import sys

from copystatic import copy_files_recursive
from gencontent import generate_page


dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"
default_basepath = "/"


def main():
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating page...")
    paths = os.walk(dir_path_content)
    for path in paths:
        if "index.md" in path[2]:
            relative_path = os.path.relpath(path[0], dir_path_content)
            generate_page(
                os.path.join(path[0], "index.md"),
                template_path,
                os.path.join(dir_path_public, relative_path, "index.html"),
                basepath
            )
        else:
            pass

main()