import unittest

from browser.browsers import browser
from config.config_processor import ConfigProcessor


class TestChromeBrowserDispatcher(unittest.TestCase):

    def setUp(self):
        self.config = ConfigProcessor('config/test-browser-config.yml')

    def test_chrome_profile1(self):
        url = 'http://github.com/johndoe'
        target = self.config.target(url)
        command = browser(target, url).command()
        self.assertEqual(command, '/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --profile-directory="Profile 1" "http://github.com/johndoe" >> /dev/null &')

    def test_default_profile(self):
        url = 'http://anything.example.com'
        target = self.config.target(url)

        with self.assertRaises(Exception) as context:
            browser(target, url).command()

        self.assertTrue('Unsupported Browser: firefox' in str(context.exception))

    def test_chrome_incognito(self):
        url = 'http://secret.example.com'
        target = self.config.target(url)
        command = browser(target, url).command()
        self.assertEqual(command, '/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --profile-directory="Default" --incognito "http://secret.example.com" >> /dev/null &')

    def test_chrome_guest(self):
        url = 'http://my-guest.example.com'
        target = self.config.target(url)
        command = browser(target, url).command()
        self.assertEqual(command, '/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --guest "http://my-guest.example.com" >> /dev/null &')

    def test_chrome_guest_overwrite_incognito(self):
        url = 'http://my-guest-not-incognito.example.com'
        target = self.config.target(url)
        command = browser(target, url).command()
        self.assertEqual(command, '/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --guest "http://my-guest-not-incognito.example.com" >> /dev/null &')

    def test_strip_trailing_slash(self):
        url = 'https://gitlab.com/exampleuser/'
        target = self.config.target(url)
        command = browser(target, url).command()
        self.assertEqual(command, '/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --profile-directory="Profile 2" "https://gitlab.com/exampleuser/" >> /dev/null &')

    def test_http_schema(self):
        url = 'http://schema.example.com/johndoe'
        target = self.config.target(url)
        command = browser(target, url).command()
        self.assertEqual(command, '/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --profile-directory="Profile 1" "http://schema.example.com/johndoe" >> /dev/null &')

    def test_https_schema(self):
        url = 'https://schema.example.com/johndoe/'
        target = self.config.target(url)
        command = browser(target, url).command()
        self.assertEqual(command, '/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --profile-directory="Profile 2" "https://schema.example.com/johndoe/" >> /dev/null &')


class TestFirefoxBrowserDispatcher(unittest.TestCase):

    def setUp(self):
        self.config = ConfigProcessor('config/test-browser-config.yml')

    def test_firefox_default(self):
        url = 'http://fox.example.com'
        target = self.config.target(url)

        with self.assertRaises(Exception) as context:
            browser(target, url).command()

        self.assertTrue('Unsupported Browser: firefox' in str(context.exception))


class TestNullBrowserDispatcher(unittest.TestCase):

    def setUp(self):
        self.config = ConfigProcessor('config/test-browser-config.yml')

    def test_start_null(self):
        url = 'http://www.bad-site.com/'
        target = self.config.target(url)
        command = browser(target, url).command()
        self.assertEqual(command, 'echo "Url http://www.bad-site.com/ was not opened" >> /dev/null &')


if __name__ == '__main__':
    unittest.main()
