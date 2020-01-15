from unittest import TestCase
from config.config_processor import ConfigProcessor


class Test(TestCase):
    def setUp(self):
        self.config = ConfigProcessor('test-browser-config.yml')

    def test_firefox_default(self):
        result = self.config.target('http://fox.example.com')

        self.assertEqual(result.browser, 'firefox')
        self.assertEqual(result.profile, 'Default')
        self.assertFalse(result.incognito)

    def test_chrome_profile1(self):
        result = self.config.target('http://github.com/johndoe')

        self.assertEqual(result.browser, 'chrome')
        self.assertEqual(result.profile, 'Profile 1')
        self.assertFalse(result.incognito)

    def test_default_profile(self):
        result = self.config.target('http://anything.example.com')

        self.assertEqual(result.browser, 'firefox')
        self.assertEqual(result.profile, 'Default')
        self.assertFalse(result.incognito)

    def test_chrome_incognito(self):
        result = self.config.target('http://secret.example.com')

        self.assertEqual(result.browser, 'chrome')
        self.assertEqual(result.profile, 'Default')
        self.assertTrue(result.incognito)


class HostsRuleTest(TestCase):
    def setUp(self):
        self.config = ConfigProcessor('test-hosts-browser-config.yml')

    def test_by_www_host(self):
        result = self.config.target('http://www.host2.com')

        self.assertEqual(result.profile, 'Default')

    def test_by_host(self):
        result = self.config.target('http://host2.com')

        self.assertEqual(result.profile, 'Profile 1')

    def test_by_ip(self):
        result = self.config.target('http://192.168.0.100:5000')

        self.assertEqual(result.profile, 'Profile 2')

    def test_by_ip_and_port_match(self):
        result = self.config.target('http://192.168.0.101:4000')

        self.assertEqual(result.profile, 'Profile 2')

    def test_by_ip_and_port_not_match(self):
        result = self.config.target('http://192.168.0.101:3000')

        self.assertEqual(result.profile, 'Default')

    def test_by_host_and_port(self):
        result = self.config.target('http://host2.com:3000/')

        self.assertEqual(result.profile, 'Profile 1')

    def test_by_host_and_port_match(self):
        result = self.config.target('http://host3.com:3000')

        self.assertEqual(result.profile, 'Profile 1')

    def test_by_host_and_port_not_match(self):
        result = self.config.target('http://www.host3.com:4000')

        self.assertEqual(result.profile, 'Default')

    def test_by_my_hosts(self):
        result = self.config.target('http://www.myhost2.com')

        self.assertEqual(result.profile, 'Default')
