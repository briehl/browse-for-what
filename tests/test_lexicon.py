import unittest
from configparser import ConfigParser
from .context import (
    browse_for_what,
    lexicon_file
)

class LexiconTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.lex = browse_for_what.Lexicon(lexicon_file)

    def test_get_words(self):
        num_words = [1, 5, 10, 100]
        for n in num_words:
            w = self.lex.get_random_words(n)
            self.assertEqual(len(w), n)

    def test_get_words_unique(self):
        num_words = 1000
        w = self.lex.get_random_words(num_words, unique=True)
        wset = set(w)
        self.assertEqual(len(wset), num_words)

    def test_get_words_skiplist(self):
        num_words = 1000
        skip_list = [
            'supermodels',
            'overtired',
            'radiophotograph',
            "Nyasa's",
            'unapproachability',
            'carnal',
            'gallimaufries',
            'Keitel',
            'Koranic',
            "effeminacy's"
        ]
        w = self.lex.get_random_words(num_words, skip_list=skip_list)
        self.assertEqual(len(w), num_words)

if __name__ == '__main__':
    unittest.main()
