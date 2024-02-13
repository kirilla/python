"""
web_directory_enumeration

This is a script to enumerate the subdirectories (or files)
on a webserver with a certain URL.

Based on sample code from
https://tryhackme.com/room/pythonforcybersecurity
"""


import requests
import sys


URL = "http://example.loc"
FILE = "wordlist.txt"


def try_word(word):

    try:
        r = requests.get(f"{URL}/{word}")
    except:
        print(f"[e] {word}")

    if r.status_code in [200]:
        print(f"[+] {word}")
    elif r.status_code in [404]:
        print(f"[-] {word}")
    elif:
        print(f"[?] {word}")


def main():
    with open(FILE, encoding="utf-8", errors="ignore") as file:
        for word in file:
            word = word.strip()
            try_word(word)


if __name__ == "__main__":
    main()
