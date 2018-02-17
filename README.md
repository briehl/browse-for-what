# browse-for-what
Let your computer browse the internet on its own. Might affect ISP search data collection. Use with caution.

This little package searches Google with some random queries, then it navigates to a few of the hits. With any luck, when some form of Big Brother (or Big Advertising) purchases your search history from your ISP and sifts through it, they'll have a harder time unraveling the signal from the noise.

I like noise.

This is a really early version of something that was more of a thought experiment than anything. I cobbled it together in Python, since that's pretty painless and fairly easily portable to a zillion environments, but still requires a few tools to get it running.

I make no claim that this can outperform professional scientific methods to extract some kind of sensible meaning from a set of queries. Anything that's meant to sift through that kind of data will likely be created with a specific goal (like identifying subversive activity, or advertising targets), and will likely be able to cluster search results easily. This isn't meant to hide you when you're being naughty, more to stick your tongue out at any advertising agency that purchases your search history. It'll be harder to market to someone who appears to search for things like `petticoat otter bloviation` on a regular basis.

# How to run
Once you download this repo, you can run the following commands from the repo's root directory:
```
pip install -r requirements.txt
python -m browse_for_what
```
(upcoming - a properly fleshed out setup.py, or conda installer or something else)

# Configuration
The `config.json` file in the root directory has everything in it.
  * `lexicon_file`: relative path to the lexicon file. This comes with one in `data/lexicon.txt`
  * `min_words` / `max_words`: the minimum and maximum number of random words to use in a query. Any more than, say, 4 or so has a good chance of just returning other dictionary files.
  * `max_links_to_browse`: sets the maximum number of links to return from the Google search, and ultimately to browse. A given search might return more or fewer, but only this value will be fetched.
  * `wait_time`: how long to wait between queries (in seconds). If you crank this down too far, you'll be spamming things and might (a) slow down your connection or (b) have Google block your IP
  * `num_searches`: how many cycles the app should run before quitting
  * `browse_timeout`: number of seconds to wait on each link request before timing out and moving on to the next one. There's lots of cruft on the internet.


# Todo
Some notes on what might be fun to do with this when I have more than a couple hours to hack on it.
* Form a lexicon that has more common words, preferably matched in a believable way, so it's not just random words from a huge dictionary. The goal is, of course, to make it look like you're doing realistic searches, right? Queries like `marls absquatulation flacon` are pretty clearly noise and full of archaic words (that one just returned a bunch of other random word lists). But something like `accipiter revisionists`, though strange, seems somewhat reasonable. Maybe you're an ornithologist and want to know more about people who disagree with hawk nomenclature?
*  Add grammatical rules to lexicon - make realistic sentences, or at least realistic groupings of words. Throwing in the odd "How do I" in front of a query. "How do I glitch buskers" could be fun.
*  Do some freaking research! It's possible to find common queries from Google Trends - those are generally nouns, and the top trends are often proper names. Maybe add those to the list. It'd be fun to see `Barry Bonds seismograph` instead of `occipital seismograph`, even though they're equally meaningless.
* How do people really search? How do people interact with results? This currently just scans through and "clicks" on the first several links, even if they're different anchors on the same Wikipedia page. (i.e., makes a GET request against the first URLs that are given). Real people don't do that. There might be some cherry picking of results that might be more sensible.


# Lexicon
166034 words in the wordlist generated with SCOWL, available at wordlist.aspell.net. See the header of /data/lexicon.txt for details and license.
