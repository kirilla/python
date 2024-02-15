"""
web_directory_enumeration

This is a script to enumerate the subdirectories (or files)
on a webserver with a certain URL.

Based on sample code from
https://tryhackme.com/room/pythonforcybersecurity
"""


import requests


URL = "http://example.loc"
FILE = "wordlist.txt"


def try_word(word):
    """
    Make an http/https request for the base URL and the word,
    and print the result: found, not found or unknown.
    """

    try:
        r = requests.get(f"{URL}/{word}", timeout=10)

    # pylint: disable=broad-exception-caught
    except Exception:
        print(f"[e] {word}")

    if r.status_code in [200]:
        print(f"[+] {word}")
    elif r.status_code in [404]:
        print(f"[-] {word}")
    else:
        print(f"[?] {word}")


def main():
    """
    Open the file, containing a list of common directory names,
    and/or file names, loop over these,
    and call the try_word() function.
    """

    with open(FILE, encoding="utf-8", errors="ignore") as file:
        for word in file:
            word = word.strip()
            try_word(word)


if __name__ == "__main__":
    main()
