"""
arp_network_scanner
"""


import errno

from scapy.all import srp, Ether, ARP


INTERFACE = "eth0"
IP_RANGE = "10.10.x.x/24"
BROADCAST_MAC = "ff:ff:ff:ff:ff:ff"


def main():
    """
    Create a ethernet packet, set a broadcast destination,
    send it, collect the results and print them.
    """

    try:
        packet = Ether(dst=BROADCAST_MAC)/ARP(pdst=IP_RANGE)

        ans, _ = srp(packet, timeout=2, iface=INTERFACE, inter=0.1)

        for _, receive in ans:
            print(receive.sprintf(r"%Ether.src% - %ARP.psrc%"))

    except PermissionError as e:
        error_number = e.errno
        error_message = errno.errorcode.get(error_number, "Unknown error")
        print(f"PermissionError ({error_number}): {error_message}")


if __name__ == "__main__":
    main()
