from .lexicon import Lexicon
from .browser import Browser
import json
import time
import os


def start(config_file):
    print("BROWSE DOWN FOR WHAT")
    print("Loading from config file: {}".format(config_file))
    config = json.loads(open(config_file, "r").read())
    lex_file = config.get('lexicon_file', None)
    if lex_file is None:
        print('Your config.json file needs a valid "lexicon_file" key!')
    l = Lexicon(_relative_path(lex_file))
    b = Browser(l,
                (config['min_words'], config['max_words']),
                config['max_links_to_browse'],
                browse_timeout=config.get('browse_timeout', 20))
    sleep_time = config['wait_time']
    b.browse()

    for i in range(0, config['num_searches']):
        time.sleep(sleep_time)
        b.browse()


def _relative_path(path):
    root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    return os.path.join(root_path, path)
