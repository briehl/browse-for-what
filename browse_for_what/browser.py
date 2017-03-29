import requests
import random
from google import search


class Browser(object):
    def __init__(self,
                 lexicon,
                 word_count_range,
                 max_links_to_browse=1,
                 browse_timeout=20):
        self.lexicon = lexicon
        self.min_words, self.max_words = word_count_range
        if self.min_words > self.max_words:
            x = self.min_words
            self.min_words = self.max_words
            self.max_words = x
        self.max_links_to_browse = max_links_to_browse
        self.browse_timeout = browse_timeout

    def browse(self):
        num_words = random.randint(self.min_words, self.max_words)
        links_to_browse = random.randint(1, self.max_links_to_browse)
        word_list = self.lexicon.get_random_words(num_words)
        search_str = " ".join(word_list)
        print("query = {}".format(search_str))
        for url in search(search_str, num=links_to_browse, stop=1):
            print("\t{}".format(url))
            try:
                requests.get(url, timeout=self.browse_timeout)
            except:
                pass # who cares? We're just poking at the internet here. If it doesn't want to be poked, that's its problem.
