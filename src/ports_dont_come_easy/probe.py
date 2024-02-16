#!/usr/bin/env python3
"""
probe.py - the second stage a nmap-like pipeline of tools.
"""


import os
import sys

import nmap


def probe_socket(ip, socket):
    """
    Probe a specific port, using nmap, 
    telling it to run the vulnerability scripts,
    and then print the result.
    """

    nm = nmap.PortScanner()
    try:
        nm.scan(ip, socket, arguments="-sV")  # -sV for service/version detection
        service_info = "No service detected or port is closed"
        for host in nm.all_hosts():
            for proto in nm[host].all_protocols():
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
        print(f"{ip}:{socket} - {service_info}")
    except Exception as e:
        print(f"Error scanning {socket}: {e}", file=sys.stderr)


def main():
    """
    Start the program, expecting input on standard input. 
    Exit if not found. 
    Otherwise, loop over lines, epecting ip, protocol and port number,
    separated by colon, and call the probe_socket() function.
    """

    if not os.isatty(sys.stdin.fileno()):
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
