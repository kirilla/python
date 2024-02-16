#!/usr/bin/env python3
"""
dont.py - the second stage a nmap-like pipeline of tools.
"""


import nmap
import sys
import argparse
import re
import os


def probe_socket(ip, port):
    nm = nmap.PortScanner()
    try:
        nm.scan(ip, port, arguments="-sV")  # -sV for service/version detection
        service_info = "No service detected or port is closed"
        for host in nm.all_hosts():
            print(f"Host? {host}") # todo
            for proto in nm[host].all_protocols():
                print(f"Proto? {proto}") # todo
                lport = list(nm[host][proto].keys())
                for port in lport:
                    state = nm[host][proto][port]['state']
                    if state == "open":
                        service = nm[host][proto][port].get('name', 'unknown service')
                        product = nm[host][proto][port].get('product', '')
                        version = nm[host][proto][port].get('version', '')
                        extra = nm[host][proto][port].get('extrainfo', '')
                        service_info = f"{service} {product} {version} {extra}".strip()
                    else:
                        service_info = "Port is closed"
        print(f"{ip}:{port} - {service_info}")
    except Exception as e:
        print(f"Error scanning {socket}: {e}", file=sys.stderr)


def main():
    if not os.isatty(sys.stdin.fileno()):
        # Handling piped input
        for line in sys.stdin:
            ip, protocol, port = line.strip().split(":")
            if ip and protocol and port:
                probe_socket(ip, port)
            else:
                print(f"Skipping {line}", file=sys.stderr)
    else:
        print("Not receiving piped input. Exiting.", file=sys.stderr)


if __name__ == "__main__":
    main()
