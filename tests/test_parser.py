import unittest

from recon_engine.utils import parse_target, parse_route


class TestParser(unittest.TestCase):

    def test_parse_target(self):
        host, port = parse_target("127.0.0.1:18090")

        self.assertEqual(host, "127.0.0.1")
        self.assertEqual(port, 18090)

    def test_parse_route(self):
        route, proof = parse_route(
            "route=test.local; proof=abcdef123456"
        )

        self.assertEqual(route, "test.local")
        self.assertEqual(proof, "abcdef123456")


if __name__ == "__main__":
    unittest.main()