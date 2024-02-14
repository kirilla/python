"""
An ethical SSH server, written by ChatGPT,
with credentials given as command-line arguments when started.

Untested.
"""


import sys
import socket
import threading

import paramiko


def handle_connection(client, username, password):
    try:
        transport = paramiko.Transport(client)
        transport.add_server_key(paramiko.RSAKey(filename='test_rsa.key'))

        server = SSHServer()
        transport.start_server(server=server)

        channel = transport.accept(1)
        if not channel:
            print('*** No channel.')
            transport.close()
            return

        print('Authenticated!')
        channel.close()
    except Exception as e:
        print('*** Caught exception: {}'.format(str(e)))
        client.close()


class SSHServer(paramiko.ServerInterface):
    def check_auth_password(self, username, password):
        # Hardcoded credentials for demonstration purposes
        if username == 'your_username' and password == 'your_password':
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED

    def get_allowed_auths(self, username):
        return 'password'


def start_server(port, username, password):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('0.0.0.0', port))
    server_socket.listen(10)
    print('Listening for connections on port {}'.format(port))

    while True:
        client, addr = server_socket.accept()
        print('Accepted connection from {}'.format(addr))
        client_handler = threading.Thread(
            target=handle_connection,
            args=(client, username, password)
        )
        client_handler.start()


def main():
    if len(sys.argv) != 4:
        print('Usage: python ssh_server.py <port> <username> <password>')
        sys.exit(1)

    port = int(sys.argv[1])
    username = sys.argv[2]
    password = sys.argv[3]

    start_server(port, username, password)


if __name__ == "__main__":
    main()
