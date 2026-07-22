import unittest

from recon_engine.scope import load_scope, is_target_allowed


class TestScope(unittest.TestCase):

    def setUp(self):
        self.scope = load_scope("../ethical-hacking-stage-5-shared-b1/evidence/lab-runtime/scope.csv")

    def test_allowed_http_port(self):
        self.assertTrue(is_target_allowed("127.0.0.1:18090", self.scope))

    def test_allowed_signal_port(self):
        self.assertTrue(is_target_allowed("127.0.0.1:22537", self.scope))

    def test_out_of_scope_port(self):
        self.assertFalse(is_target_allowed("127.0.0.1:26000", self.scope))

    def test_non_loopback(self):
        self.assertFalse(is_target_allowed("8.8.8.8:18090", self.scope))


if __name__ == "__main__":
    unittest.main()