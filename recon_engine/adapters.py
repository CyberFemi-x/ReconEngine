import socket


def connect_to_target(host: str, port: int, timeout: int = 5):
    """
    Connect to a target and return the open socket.
    """

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(timeout)

    client.connect((host, port))

    return client


def receive_banner(client):
    """
    Receive the first response from the target.
    """

    client.settimeout(3)

    try:
        data = client.recv(4096)
        return data.decode("utf-8", errors="replace")

    except TimeoutError:
        return ""

    except Exception:
        return ""
    
def send_command(client, command):
    """
    Send a command to the target and return its response.
    """

    client.sendall((command + "\n").encode("utf-8"))

    try:
        data = client.recv(4096)
        return data.decode("utf-8", errors="replace")

    except TimeoutError:
        return ""

    except Exception:
        return ""