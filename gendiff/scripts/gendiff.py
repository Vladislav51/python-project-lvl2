import argparse
import sys
from gendiff.scripts.generate_diff import generate_diff_func


def gendifference(argv):
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('file1', metavar='first_file',
                        type=argparse.FileType('r'), nargs='?')
    parser.add_argument('file2', metavar='second_file',
                        type=argparse.FileType('r'), nargs='?')
    parser.add_argument('-f', '--format',
                        help='set format of output',type=ascii,dest='format_name')
    args = parser.parse_args(argv)
    return generate_diff_func(args.file1, args.file2, args.format_name)


def main():
    sys.exit(print(gendifference(sys.argv[1:])))

def generate_diff():
    sys.exit(print(gendifference(sys.argv[1:])))


if __name__ == '__main__':
    main()
