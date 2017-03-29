import requests
import random
from google import search

class Browser(object):
    def __init__(self, lexicon, word_count_range, max_links_to_browse):
        self.lexicon = lexicon
        self.min_words, self.max_words = word_count_range
        if self.min_words > self.max_words:
            x = self.min_words
            self.min_words = self.max_words
            self.max_words = x
        self.max_links_to_browse = max_links_to_browse

    def browse(self):
        num_words = random.randint(self.min_words, self.max_words)
        word_list = lexicon.get_random_words(num_words)
        for url in search(" ".join(word_list), stop=max_links_to_browse):
            requests.get(url)
