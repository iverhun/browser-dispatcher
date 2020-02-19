import unittest

from config.url_util import normalize_url


class UrlUtilTest(unittest.TestCase):

    def test_normalize_url__strip_scheme(self):
        expected = 'example.com/images'

        self.assertEqual(normalize_url('http://www.example.com/images/'), expected)
        self.assertEqual(normalize_url('https://www.example.com/images/'), expected)
        self.assertEqual(normalize_url('http://example.com/images/'), expected)
        self.assertEqual(normalize_url('https://example.com/images/'), expected)
        self.assertEqual(normalize_url('www.example.com/images/'), expected)

    def test_normalize_url_retain_scheme(self):
        expected = 'example.com/images'

        self.assertEqual(normalize_url('http://www.example.com/images/', False), 'http://' + expected)
        self.assertEqual(normalize_url('https://www.example.com/images/', False), 'https://' + expected)
        self.assertEqual(normalize_url('http://example.com/images/', False), 'http://' + expected)
        self.assertEqual(normalize_url('https://example.com/images/', False), 'https://' + expected)
        self.assertEqual(normalize_url('www.example.com/images/', False), expected)
