import random

class Lexicon(object):
    def __init__(self, lexicon_file):
        self.lexicon = self.load_lexicon(lexicon_file)
        self.words = list()
        self.num_words = 0

    def load_lexicon(self, lexicon_file):
        with open(lexicon_file, 'r') as f:
            while (f.readline().strip != "---"):
                pass
            words = f.readlines()
            self.words = [w.strip() for w in words]
            self.num_words = len(self.words)

    def _random_word(self):
        if self.num_words == 0:
            return None
        return self.words[random.randint(0, self.num_words-1)]

    def get_random_words(self, num_words, skip_list=[], unique=True)
        word_list = list()
        if num_words >= self.num_words:
            #lol you cray.
            # return all words, minus those on the skip list
            pass
        while len(word_list) < num_words-1:
            w = self._random_word()
            if w not in skip_list:
                word_list.append(w)
                if unique:
                    skip_list.append(w)
        return word_list
