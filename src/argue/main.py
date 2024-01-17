import argparse
import sys

PROGRAM = "argue"

def main():
    parser = argparse.ArgumentParser(description='Prints a greeting message to the user.',
				     prog = PROGRAM)
    parser.add_argument('name', nargs='?', type=str, help='the name of the user')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0', help="show program's version number and exit")

    args = parser.parse_args()

    if args.name:
        print(f"Hello, {args.name}!")
    elif not sys.stdin.isatty():
        for line in sys.stdin:
            name = line.strip()
            if name:
                printf(f"Hello, {name}!")
    else:
        parser.print_usage()


if __name__ == "__main__":
    main()


