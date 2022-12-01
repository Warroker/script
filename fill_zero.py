import os
from pathlib import Path
import shutil
import argparse


def zero_fill(dir_root: str, file_path: str):
    dir_path = Path(dir_root)

    old_path = dir_path / file_path

    # num,format = file_path.split('.')
    new_path = dir_path / file_path.zfill(10)
    shutil.move(old_path, new_path)


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dir", type=str, required=True)
    return parser


def main():
    parser = parse()
    args = parser.parse_args()
    print(args.__dict__)
    files = os.listdir(args.dir)
    for f in files:
        zero_fill(args.dir, f)


if __name__ == "__main__":
    main()
