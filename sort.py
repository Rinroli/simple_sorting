#!/usr/bin/env python3
"""Simple file sort. Doesn't change files in directories.
Thanks to https://habr.com/ru/post/562362/ 
for idea and extension library

// The MIT License (MIT)

// Copyright (c) 2021 Rinroli

Version 1.3
July 2021
"""

import json
import logging as lg
from pathlib import Path
from argparse import ArgumentParser
from platform import system as sys_platform

# WARNING!
# Check the location of your Download directiry! 
downloads = "Загрузки" if sys_platform() == "Linux" else "Downloads"
MAIN_PATH = Path.home() / Path(downloads)

# key names will be folder names!
# only in lowercase (will be converted)
with open("extension_lib.json", "r") as ext_file:
    EXTENSIONS = json.load(ext_file)


def sort_files(root_path: Path):
    """Sort files to directories. Delete empty ones.
    Start at root_dir, not recursively.
    Do not touch hidden ('.*') files.
    """
    # root_path = Path(root_dir)
    create_dirs(root_path)
    for filename in filter(lambda x: (not x.name.startswith('.'))
                           and x.name != "extension_lib.json"
                           and x.is_file(), root_path.iterdir()):
        group = check_known(filename.name)
        filename.rename(f"{root_path}/{group}/{filename.name}")
        print(f"File <{filename.name}> moved to <{group}>")
        logger.info(f"File <{filename.name}> moved to <{group}>")
    clear_empty(root_path)


def clear_empty(root_path: Path):
    """Delete all empty automatic generated dirs."""
    logger.info("Start deleting empty dirs")
    for dir_name in root_path.iterdir():
        if dir_name.is_dir() and dir_name.name in EXTENSIONS:
            if not list(dir_name.iterdir()):
                dir_name.rmdir()
                logger.info(f"Remove <{dir_name.name}>")


def check_known(full_name: str):
    """Check if path (only name) in the group."""
    ext = full_name.rsplit('.')[-1]
    for type_file in EXTENSIONS:
        if ext.lower() in EXTENSIONS[type_file]:
            logger.info(f"Find <{full_name}> - type <{type_file}>")
            return type_file
    logger.info(f"Find file out of categories <{full_name}>")
    return "unsorted"


def create_dirs(root_path: Path):
    """Create directories if they not exist."""
    nu_created: int = 0
    for group in EXTENSIONS:
        dir_path = root_path / Path(group)
        if not dir_path.exists():
            dir_path.mkdir()
            nu_created += 1
            logger.info(f"Create directory <{group}>")
    logger.info(f"{nu_created} directories created")


def parse_arguments():
    """Parse arguments from the terminal."""
    parser = ArgumentParser(description="Sort files")
    parser.add_argument("-r", "--relative",
                        action="store_true",
                        help="type path (relative or absolute (default))")
    parser.add_argument("-p", "--path",
                        type=str,
                        default="",
                        help="path (default Downloads)")
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    logger = lg.getLogger("main")
    logger.setLevel(lg.DEBUG)
    fh = lg.FileHandler("logs.log")
    formatter = lg.Formatter(
        datefmt="%Y-%m-%d|%H:%M:%S",
        fmt='%(asctime)s: %(levelname)s - %(name)s - %(message)s'
    )
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    logger.info("Start session.")

    args = parse_arguments()
    if args.path == "":
        path = Path(MAIN_PATH)
    elif args.relative:
        path = (Path().cwd() / Path(args.path))
    else:
        path = Path(args.path)
    logger.info(f"Working dir is <{path}>")
    sort_files(path)

    logger.info("End session.")
