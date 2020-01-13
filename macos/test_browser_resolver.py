from unittest import TestCase
from browser_resolver import process, load_yaml_config


class Test(TestCase):
    def setUp(self):
        self.config = load_yaml_config('../config/test-browser-config.yml')

    def test_firefox_default(self):
        result = process("http://fox.example.com", self.config)

        self.assertEquals(result.browser, 'firefox')
        self.assertEquals(result.profile, 'Default')
        self.assertFalse(result.incognito)

    def test_chrome_profile1(self):
        result = process("http://github.com/johndoe", self.config)

        self.assertEquals(result.browser, 'chrome')
        self.assertEquals(result.profile, 'Profile 1')
        self.assertFalse(result.incognito)

    def test_default_profile(self):
        result = process("http://anything.example.com", self.config)

        self.assertEquals(result.browser, 'firefox')
        self.assertEquals(result.profile, 'Default')
        self.assertFalse(result.incognito)

    def test_chrome_incognito(self):
        result = process("http://secret.example.com", self.config)

        self.assertEquals(result.browser, 'chrome')
        self.assertEquals(result.profile, 'Default')
        self.assertTrue(result.incognito)
