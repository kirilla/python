"""
An ethical SSH server, written by ChatGPT,
with credentials given as command-line arguments when started.

Untested. Work in progress.
"""


import sys
import socket
import threading

import paramiko


def handle_connection(client, username, password):
    """
    Handle the accepted connection.
    """

    try:
        transport = paramiko.Transport(client)
        transport.add_server_key(paramiko.RSAKey(filename="test_rsa.key"))

        server = SSHServer()  # pass in username and password?
        transport.start_server(server=server)

        channel = transport.accept(1)
        if not channel:
            print("*** No channel.")
            transport.close()
            return

        print("Authenticated!")
        channel.close()

    # pylint: disable=broad-exception-caught
    except Exception as e:
        print(f"*** Caught exception: {e}")
        client.close()


class SSHServer(paramiko.ServerInterface):  # add username, password, to constructor?
    """
    A class that implements the authentication behavior.
    """

    def check_auth_password(self, username, password):
        """
        Check the credentials given at server startup
        """

        if username == "your_username" and password == "your_password":  # todo
            return paramiko.AUTH_SUCCESSFUL

        return paramiko.AUTH_FAILED

    def get_allowed_auths(self, username):
        """
        Allow password authentication.
        """

        return "password"


def start_server(port, username, password):
    """
    Open a listening socket and start accepting clients.
    """

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("0.0.0.0", port))
    server_socket.listen(10)
    print(f"Listening for connections on port {port}.")

    while True:
        client, addr = server_socket.accept()
        print(f"Accepted connection from {addr}.")
        client_handler = threading.Thread(
            target=handle_connection,
            args=(client, username, password)
        )
        client_handler.start()


def main():
    """
    Call start_server() with the given command-line arguments.
    """
    if len(sys.argv) != 4:
        print('Usage: python ssh_server.py <port> <username> <password>')
        sys.exit(1)

    port = int(sys.argv[1])
    username = sys.argv[2]
    password = sys.argv[3]

    start_server(port, username, password)


if __name__ == "__main__":
    main()
