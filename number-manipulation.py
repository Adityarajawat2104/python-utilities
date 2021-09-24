import argparse
import sys

def calculate(args):

    if args.operation.lower() == 'add' or args.operation.lower() == 'add':
        return args.x + args.y

    if args.operation.lower() == 'mul' or args.operation.lower() == 'multiplication':
        return args.x * args.y

    if args.operation.lower() == 'div' or args.operation.lower() == 'division':
        return args.x + args.y

    if args.operation.lower() == 'sub' or args.operation.lower() == 'substraction':
        return args.x + args.y


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--x", type=float, default=1.0, help="Enter 1st Number: ")
    parser.add_argument("--y", type=float, default=1.0, help="Enter 2st Number: ")
    parser.add_argument("--operation", type=str, default="add", help="Enter Operation: ")
    args = parser.parse_args()
    sys.stdout.write(str(calculate(args)))
