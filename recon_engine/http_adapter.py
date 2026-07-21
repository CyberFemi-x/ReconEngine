import http.client


def http_get(host: str, port: int, path: str = "/", headers=None, host_header=None):
    """
    Send an HTTP GET request and return the response.
    """

    if headers is None:
        headers = {}

    if host_header:
        headers["Host"] = host_header

    conn = http.client.HTTPConnection(host, port, timeout=5)

    conn.request("GET", path, headers=headers)

    response = conn.getresponse()

    body = response.read().decode("utf-8", errors="replace")

    result = {
        "status": response.status,
        "reason": response.reason,
        "headers": dict(response.getheaders()),
        "body": body,
    }

    conn.close()

    return result


def discover_http(host: str, port: int):
    """
    Perform basic HTTP discovery.
    """

    paths = [
        "/",
        "/robots.txt",
    ]

    results = []

    for path in paths:
        try:
            result = http_get(host, port, path)
            result["path"] = path
            results.append(result)
        except Exception:
            pass

    return results


def extract_disallowed_paths(robots_body: str):
    """
    Extract paths listed under 'Disallow:' in robots.txt.
    """

    paths = []

    for line in robots_body.splitlines():
        line = line.strip()

        if line.lower().startswith("disallow:"):
            path = line.split(":", 1)[1].strip()

            if path:
                paths.append(path)

    return paths