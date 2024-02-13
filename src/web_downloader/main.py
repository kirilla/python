"""
web_downloader - the poor man's curl.

Based on sample code from
https://tryhackme.com/room/pythonforcybersecurity
"""


import sys

import argparse
import requests


def main():
    parser = argparse.ArgumentParser()
    
    parser.add_argument(
            "url",
            help="the url of a file or resource")
    
    parser.add_argument(
            "-o", "--output", required=True,
            help="the name of the file you want to create")

    args = parser.parse_args()

    response = requests.get(args.url, allow_redirects=True)

    with open(args.output, 'wb') as file:
        file.write(response.content)


if __name__ == "__main__":
    main()
