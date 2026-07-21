import socket


def connect_to_target(host: str, port: int, timeout: int = 5):
    """
    Connect to a target and return the open socket.
    """

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(timeout)

    client.connect((host, port))

    return client