from unittest import TestCase

from config.config_processor import ConfigProcessor
import browser_dispatcher


class Test(TestCase):

    def setUp(self):
        self.config = ConfigProcessor('../config/test-browser-config.yml')

    def test_firefox_default(self):
        url = 'http://fox.example.com'
        target = self.config.target(url)

        with self.assertRaises(Exception) as context:
            browser_dispatcher.command(target, url)

        self.assertTrue('Unsupported Browser: firefox' in context.exception)

    def test_chrome_profile1(self):
        url = 'http://github.com/johndoe'
        target = self.config.target(url)
        command = browser_dispatcher.command(target, url)
        self.assertEqual(command, '/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --profile-directory="Profile 1" "http://github.com/johndoe" >> /dev/null &')

    def test_default_profile(self):
        url = 'http://anything.example.com'
        target = self.config.target(url)

        with self.assertRaises(Exception) as context:
            browser_dispatcher.command(target, url)

        self.assertTrue('Unsupported Browser: firefox' in context.exception)

    def test_chrome_incognito(self):
        url = 'http://secret.example.com'
        target = self.config.target(url)
        command = browser_dispatcher.command(target, url)
        self.assertEqual(command, '/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --incognito "http://secret.example.com" >> /dev/null &')
