"""
arp_network_scanner
"""


import errno

from scapy.all import Ether, ARP, srp


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

        answered, unanswered = srp(
                packet, timeout=2, iface=INTERFACE, inter=0.1)

        for send, receive in answered:
            print(receive.sprintf(r"%Ether.src% - %ARP.psrc%"))

    except PermissionError as e:
        error_number = e.errno
        error_message = errno.errorcode.get(error_number, "Unknown error")
        print(f"PermissionError ({error_number}): {error_message}")


if __name__ == "__main__":
    main()
