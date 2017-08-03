import unittest
from jiracli import config


class TestConfig(unittest.TestCase):

    def test_parse(self):

        cfg = config.parse()
        self.assertEqual(cfg.username, 'bvale')