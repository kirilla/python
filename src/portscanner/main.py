"""
Portscanner

Based on sample code from 
https://tryhackme.com/room/pythonforcybersecurity
"""


import sys
import socket
import pyfiglet


IP = "127.0.0.1"

STARTING_PORT = 1
ENDING_PORT = 65535


def try_port(port):
    result = 1

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        r = sock.connect_ex((IP, port))
        if r == 0:
            result = r
        sock.close()
    except Exception as e:
        pass

    return result


def main():
    """
    Print the banner.
    Loop trough ports in range and call try_port().
    Print the report.
    """
    ascii_banner = pyfiglet.figlet_format("portscanner")
    print(ascii_banner)

    open_ports = []

    ports = range(STARTING_PORT, ENDING_PORT)

    for port in ports:
        # sys.stdout.flush()
        response = try_port(port)
        if response == 0:
            open_ports.append(port)

    if open_ports:
        print("Open ports are:")
        print(sorted(open_ports))
    else:
        print("No open ports.")


if __name__ == "__main__":
    main()
