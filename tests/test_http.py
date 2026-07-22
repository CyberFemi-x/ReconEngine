import unittest

from recon_engine.http_adapter import extract_disallowed_paths


class TestHTTP(unittest.TestCase):

    def test_extract_single_path(self):
        robots = """
User-agent: *
Disallow: /admin
"""
        self.assertEqual(
            extract_disallowed_paths(robots),
            ["/admin"]
        )

    def test_extract_multiple_paths(self):
        robots = """
User-agent: *
Disallow: /admin
Disallow: /private
"""
        self.assertEqual(
            extract_disallowed_paths(robots),
            ["/admin", "/private"]
        )

    def test_empty_robots(self):
        self.assertEqual(
            extract_disallowed_paths(""),
            []
        )


if __name__ == "__main__":
    unittest.main()