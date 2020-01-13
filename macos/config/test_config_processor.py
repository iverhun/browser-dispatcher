from unittest import TestCase
from config.config_processor import ConfigProcessor


class Test(TestCase):
    def setUp(self):
        self.config = ConfigProcessor('../../config/test-browser-config.yml')

    def test_firefox_default(self):
        result = self.config.target("http://fox.example.com")

        self.assertEqual(result.browser, 'firefox')
        self.assertEqual(result.profile, 'Default')
        self.assertFalse(result.incognito)

    def test_chrome_profile1(self):
        result = self.config.target("http://github.com/johndoe")

        self.assertEqual(result.browser, 'chrome')
        self.assertEqual(result.profile, 'Profile 1')
        self.assertFalse(result.incognito)

    def test_default_profile(self):
        result = self.config.target("http://anything.example.com")

        self.assertEqual(result.browser, 'firefox')
        self.assertEqual(result.profile, 'Default')
        self.assertFalse(result.incognito)

    def test_chrome_incognito(self):
        result = self.config.target("http://secret.example.com")

        self.assertEqual(result.browser, 'chrome')
        self.assertEqual(result.profile, 'Default')
        self.assertTrue(result.incognito)
