"""
web_subdomain_enumeration

This is a script to enumerate the subdomains of a webserver
for which the parent domain is already known.

NOTE: Untested. Not sure it works. False positives?

Based on sample code from
https://tryhackme.com/room/pythonforcybersecurity
"""


import requests


DOMAIN = "example.loc"
FILE = "subdomains.txt"


def try_subdomain(sub):
    """
    Make an http request to see if the webserver answers to it.
    """

    url = f"http://{sub}.{DOMAIN}"

    try:
        requests.get(url, timeout=10)
        print(f"[+] {sub}")

    except requests.ConnectionError:
        print(f"[-] {sub}")


def main():
    """
    Open the file with a wordlist of common subdomain names,
    and loop over them, calling the try_subdomains() function.
    """

    with open(FILE, encoding="utf-8", errors="ignore") as file:
        for sub in file:
            sub = sub.strip()
            try_subdomain(sub)


if __name__ == "__main__":
    main()
