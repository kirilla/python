"""argsys"""

import sys

PROGRAM = "argsys"

def main():
    if len(sys.argv) == 2:
        if sys.argv[1] in ['-h', '-?', '-v']:
            print_usage()
        else:
            name = sys.argv[1]
            print(f"Hello, {name}!")
    else:
        print_usage()

def print_usage():
    usage = f"""
Usage: {PROGRAM} [OPTION]... [NAME]
Prints a greeting message to the user.

Arguments:
    NAME        the name of the user.

Options:
    -h, -?      show this help message and exit
    -v          show program's version number and exit
    """
    print(usage)
    

if __name__ == "__main__":
    main()


