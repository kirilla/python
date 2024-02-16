#!/usr/bin/env python3

"""
ports.py - the first stage in an nmap-like pipeline of tools.

Based on code from
https://github.com/miwashi-edu/edu-python-docs

NOTE:
I don't think the UDP code works.
I tried slotting in some scapy code instead, but it got worse,
and does not even show a connect on the receiving end,
with "nc -luvp 3" on localhost.
"""


import argparse
import socket

from scapy.all import IP, UDP, sr


def scan_tcp_ports(host, ports, verbose):
    if verbose:
        print(f"v: scanning {host}, {len(ports)} ports")

    open_ports = []
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                result = s.connect_ex((host, port))
                if verbose:
                    print(f"port {port} result: {result}")
                if result == 0:
                    open_ports.append(port)
                    if verbose:
                        print(f"v: [+] {port}")
                else:
                    if verbose:
                        print(f"v: [-] {port}")
        except Exception as e:
            if verbose:
                print(f"v: Exception for port {port}: {e}")
            pass

    return open_ports


def scan_udp_ports(host, ports, verbose):
    if verbose:
        print(f"v: scanning udp {host}, {len(ports)} ports")
    open_ports = []
    for port in ports:
        """
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                s.settimeout(3)
                s.sendto(b'', (host, port))
                s.recvfrom(1024)
                open_ports.append(port)
                if verbose:
                    print(f"v: [+] {port}")
        except socket.timeout:
            if verbose:
                print(f"v: [-] {port}")
            pass
        except Exception as e:
            if verbose:
                print(f"v: Exception for port {port}: {e}.")
            pass
        """

        udp_packet = IP(dst=host) / UDP(dport=port)

        response = sr(udp_packet, timeout=1, verbose=0)[0]

        if response:
            print(f"Open: {port}")
            open_ports.append(port)
        else:
            print(f"Closed: {port}")

    return open_ports


def main():
    parser = argparse.ArgumentParser(
            description="Simple Port Scanner for Piping")

    parser.add_argument(
            "-H", "--host", default="127.0.0.1", 
            help="Host to scan, default is localhost")

    parser.add_argument(
            "-p", "--port", default="1-1024", 
            help="Port range to scan, default is 1-1024")

    parser.add_argument(
            "-t", "--type", default="tcp", choices=["tcp", "udp"], 
            help="Type of scan: tcp or udp, default is tcp")

    parser.add_argument(
            '-v', '--verbose', action='store_true',
            help="Print the progress.")

    args = parser.parse_args()

    host = args.host
    protocol = args.type.lower()
    
    start_port, end_port = args.port.split('-', 1)
    
    start_port = int(start_port)
    end_port = int(end_port)

    if start_port > end_port:
        print("Invalid port range.", file=sys.stderr)
        return

    ports = range(start_port, end_port+1)

    open_ports = []

    if protocol == "tcp":
        open_ports = scan_tcp_ports(host, ports, args.verbose)
    elif protocol == "udp":
        open_ports = scan_udp_ports(host, ports, args.verbose)

    for port in open_ports:
        print(f"{host}:{protocol}:{port}")

    if len(open_ports) == 0 and args.verbose:
        print("No open ports")

if __name__ == "__main__":
    main()
