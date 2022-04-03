import argparse
from gendiff.scripts.generate_diff import generate_diff


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('file1', metavar='first_file',
                        type=argparse.FileType('r'), nargs='?')
    parser.add_argument('file2', metavar='second_file',
                        type=argparse.FileType('r'), nargs='?')
    parser.add_argument('-f', '--format',
                        help='set format of output')

    args = parser.parse_args()
    generate_diff(args.file1, args.file2)


if __name__ == '__main__':
    main()
