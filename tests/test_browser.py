from .context import (
    browse_for_what,
    lexicon_file
)
import unittest


class BrowserTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.lexicon = browse_for_what.Lexicon(lexicon_file)

    def test_browser_setup(self):
        browser = browse_for_what.Browser(self.lexicon, (2, 7), 5)
        self.assertIsNotNone(browser)

    def test_browsing(self):
        browser = browse_for_what.Browser(self.lexicon, (2, 7), 5)
        browser.browse()
