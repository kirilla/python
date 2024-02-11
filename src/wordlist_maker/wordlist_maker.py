"""
Wordlist_maker is a template-based wordlist generator
"""

import sys
import argparse
import itertools


class StrippingFile:
    """
    This is a file wrapper that strips the newline.
    This is useful when passing files into the itertools.product function.
    """
    def __init__(self, file_path):
        """
        Open the file for reading.
        """
        self.file_path = file_path
        # pylint: disable=consider-using-with
        self.file = open(file_path, 'r', encoding="utf-8", errors="ignore")

    def __iter__(self):
        """
        Return the iterator. (Self, in this case.)
        """
        return self

    def __next__(self):
        """
        Return the next line of the file, stripped.
        """
        line = self.file.readline()
        line = line.strip()
        if not line:
            raise StopIteration
        return line

    def close(self):
        """
        Close the file when done iterating throught it.
        """
        self.file.close()


def main():
    """
    Parse given arguments, start the wordlist generation,
    or display the usage information.
    """
    parser = argparse.ArgumentParser(
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description="A template-based wordlist generator",
            epilog="""
The wordlist, literal and character set arguments should
be given in the order in which they are used in the template.
A colon is used to separate them.

w:w:w    wordlist 1, 2 and 3
w:c       wordlist 1, character set 1
l:w:c    literal string 1, wordlist 1, character set 1
""")
    parser.add_argument("template", help="a template for the generator")

    parser.add_argument("-w", "--wordlists",
                        nargs="+", help="the path to a wordlist")

    parser.add_argument("-l", "--literals",
                        nargs="+", help="a literal string")

    parser.add_argument("-c", "--characters",
                        nargs="+", help="a character set")
    args = parser.parse_args()

    print(args.template)
    print(args.wordlists)

    references = []

    for source in args.template.split(":"):
        if source == "w":
            path = args.wordlists.pop(0)
            file = StrippingFile(path)
            references.append(file)
        elif source == "l":
            literal = args.literals.pop(0)
            references.append([literal])
        elif source == "c":
            chars = args.characters.pop(0)
            references.append(chars)
        else:
            print(f"Unexpected value in template: {source}")
            sys.exit(1)

    print(references)

    iterator = itertools.product(*references)

    for my_tuple in iterator:
        print(''.join(my_tuple))


if __name__ == '__main__':
    main()
