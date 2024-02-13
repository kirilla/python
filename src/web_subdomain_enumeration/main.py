"""
web_subdomain_enumeration

This is a script to enumerate the subdomains of a webserver
for which the parent domain is already known.

NOTE: Untested. Not sure it works. False positives?
"""


import requests
import sys


DOMAIN = "example.loc"
FILE = "subdomains.txt"


def try_subdomain(sub):
    url = f"http://{sub}.{DOMAIN}"

    try:
        requests.get(url)
        print(f"[+] {sub}")

    except requests.ConnectionError:
        print(f"[-] {sub}")


def main():
    with open(FILE, encoding="utf-8", errors="ignore") as file:
        for sub in file:
            sub = sub.strip()
            try_subdomain(sub)


if __name__ == "__main__":
    main()
