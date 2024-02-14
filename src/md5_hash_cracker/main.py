"""
md5_hash_cracker - the worlds first and only full-featured md5 hash cracker

Based on sample code from
https://tryhackme.com/room/pythonforcybersecurity
"""


import argparse
import hashlib
import pyfiglet


def main():
    """
    Define arguments, open the wordlist file,
    loop over it, hash each word, compare it to the given hash,
    and print the word if the computed hash matches the given.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("hash", help="the md5 hash string")
    parser.add_argument("wordlist", help="the wordlist file path")
    args = parser.parse_args()

    with open(args.wordlist, 'r', encoding="utf-8", errors="ignore") as file:
        for line in file:

            word = line.strip()
            encoded_word = word.encode()
            print(f"Trying: {word}")

            hash_object = hashlib.md5(encoded_word)
            word_hash = hash_object.hexdigest()

            if word_hash == args.hash:
                print("\nFound it, yo!\n")
                the_winner = pyfiglet.figlet_format(word)
                print(the_winner)
                print(f"\n(That's '{word}' for you lamerz.)")
                break


if __name__ == "__main__":
    main()
