import argparse
import os
import re


def rename(args):
    if re.search("#[^#]+#", args.pattern):
        print(f"Invalid pattern {args.pattern}. Chars between two # are not allowed.")
        return
    if not os.path.isdir(args.folder):
        print("Folder does not exist.")
        return

    reverse = True if args.order == "desc" else False
    files = [os.path.join(args.folder, f) for f in os.listdir(args.folder)]
    files = list(filter(os.path.isfile, files))

    if args.sort_by == "size":
        files.sort(key=os.path.getsize, reverse=reverse)
    elif args.sort_by == "creation":
        files.sort(key=os.path.getctime, reverse=reverse)
    elif args.sort_by == "access":
        files.sort(key=os.path.getatime, reverse=reverse)
    elif args.sort_by == "modified":
        files.sort(key=os.path.getmtime, reverse=reverse)

    length = args.pattern.count("#")
    for i, f in enumerate(files):
        new_name = re.sub("#+", str(i).zfill(length), args.pattern)
        os.rename(f, os.path.join(args.folder, new_name))


def parse_input():
    parser = argparse.ArgumentParser()
    parser.add_argument("folder",
                        type=str,
                        help="Folder with the files you want to rename")
    parser.add_argument("-p", "--pattern",
                        type=str,
                        help="Pattern for the new file names. # gets replaced by a number.", default="####")
    parser.add_argument("-s", "--sort-by",
                        type=str,
                        choices=["size", "creation", "access", "modified"],
                        default="creation",
                        help="Sort the files")
    parser.add_argument("-o", "--order",
                        type=str,
                        choices=["asc", "desc"],
                        default="asc",
                        help="Sort the files ascending or descending")

    return parser.parse_args()


if __name__ == "__main__":
    rename(parse_input())
