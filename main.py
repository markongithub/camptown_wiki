#!/usr/bin/env python3
import json
import os
import sys
import time
import wikipedia

from lib.constants import BACKOFF, MAX_ATTEMPTS, MAX_STATUS_LEN, TIMEOUT_BACKOFF
from lib import datastore
# from lib import mastodon
from lib import twitter
from lib import words

STORED_RHYMES = './rhymes.json'

def main():
    rhyming_dict = datastore.load_local(STORED_RHYMES)
    (new_rhyming_dict, title1, title2) = searchForCamptown(rhyming_dict, MAX_ATTEMPTS, BACKOFF)
    datastore.dump_local(STORED_RHYMES, new_rhyming_dict)
    if title1 and title2:
        postTweet(title1, title2)

def postTweet(title1, title2):
    status_text = "\n".join((title1, "Doo dah, doo dah", title2, "Oh, doo dah day"))

    if len(status_text) <= MAX_STATUS_LEN:
        _ = twitter.sendTweet(status_text)
        print(status_text)
    else:
        print(f'Oh no, this was too long: {status_text}')

def read_or_new_json(path, default):
    if os.path.isfile(path):
        with open(path, "r") as f:
            try:
                return json.load(f)
            except Exception: # so many things could go wrong, can't be more specific.
                pass 
    with open(path, "w") as f:
        json.dump(default, f)
    return default

def sameFinalWord(title1, title2):
    return title1.lower().split()[-1] == title2.lower().split()[-1]

def searchForCamptown(rhyming_dict, attempts=MAX_ATTEMPTS, backoff=BACKOFF):
    """Loop MAX_ATTEMPT times, searching for a Camptown meter wikipedia title.

    Args:
        Integer: attempts, retries remaining.
        Integer: backoff, seconds to wait between each loop.
    Returns:
        String or False: String of wikipedia title in Camptown meter, or False if
                         none found.
    """
    for attempt in range(attempts):
        print(f"\r{str(attempt * 10)} articles fetched...", end="")
        sys.stdout.flush()
        rhymes = checkTenPagesForCamptown()
        for (rhyme, title) in rhymes:
            old_title = rhyming_dict.get(rhyme, None)
            if old_title:
                if sameFinalWord(old_title, title):
                    print(f"{old_title} and {title} are not a good rhyme so I will just throw {title} away for now.")
                    continue
                print(f"\nMatched: {title} and {old_title}")
                del rhyming_dict[rhyme]
                return (rhyming_dict, old_title, title)
            else:
                print(f"\nAdding {title}, which rhymes with {rhyme}")
                rhyming_dict[rhyme] = title

        time.sleep(backoff)

    print(f"\nNo matches found.")
    return (rhyming_dict, None, None)


def checkTenPagesForCamptown():
    """Get 10 random wiki titles, check if any of them isCamptown().

    We grab the max allowed Wikipedia page titles (10) using wikipedia.random().
    If any title is in Camptown meter, return the title. Otherwise, return False.

    Args:
        None
    Returns:
        List of (String,String) pairs
    """
    wikipedia.set_rate_limiting(True)
    try:
        titles = wikipedia.random(10)
    except wikipedia.exceptions.HTTPTimeoutError as e:
        print(f"Wikipedia timout exception: {e}")
        time.sleep(TIMEOUT_BACKOFF)
        main()
    except wikipedia.exceptions.WikipediaException as e:
        print(f"Wikipedia exception: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Exception while fetching wiki titles: {e}")
        sys.exit(1)

    rhymes = []
    for title in titles:
        rhyme = words.getRhymingPartIfCamptown(title)
        if rhyme:
            rhymes.append((rhyme, title))
    return rhymes


if __name__ == "__main__":
    main()
