import argparse


parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('files', metavar='first_file', type=ascii, nargs=1)
parser.add_argument('files', metavar='second_file', type=ascii, nargs=1)
parser.add_argument('-f','--format',
                    help='set format of output')

args = parser.parse_args()
print(args.accumulate(args.files))



