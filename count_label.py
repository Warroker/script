import os
from pathlib import Path
import shutil
import argparse

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dir", type=str, required=True)
    return parser


def main():
    parser = parse()
    args = parser.parse_args()
    files = os.listdir(args.dir)
    print(args.__dir__)
    total_num = 0
    dir_path = Path(args.dir)
    for file_name in files:
        count = 0
        file_path = dir_path / file_name
        with open(file_path, 'r') as f:
            for line in f:
                count += 1
        total_num += count 
    print(total_num)

if __name__ == "__main__":
    main()
