import os
import re

# Constants for use throughout the application.
# Someday maybe I'll use configs or CLI args. For now this is easier.

if os.environ.get('MAX_ATTEMPTS'):
    MAX_ATTEMPTS = int(os.environ.get('MAX_ATTEMPTS'))
else:
    MAX_ATTEMPTS = 1
MAX_STATUS_LEN = 280
BACKOFF = 0.5
TIMEOUT_BACKOFF = 240
LOGO_PATH = r'/tmp/logo.png'
SCREENSHOT_PATH = r'/tmp/screenshot.png'
CHROME_PATH = r'google-chrome'
URL = 'file:///home/catherine_lee_ball/tmnt.html'
# Article titles the contain strings in BANNED_WORDS are skipped.
# Banned words are things that are very inappropriate, or things
# that are oversaturating the timeline, i.e. historic districts
BANNED_WORDS = ("rape", "nazi", "victim", "shootings")
BANNED_PHRASES = (r"(", "shooting", "murder of", "killing of", "lynching of")
# Survey can go either way but I'm wagering that in article titles it will more
# often be a noun.
PRONUNCIATION_OVERRIDES = (("HD", "10"), ("U.S.", "10"), ("Laos", "1"),
                           ("Our", "1"), ("DeMille", "01"), ("Survey", "10"),
                           ("Abreu", "010"))
TMNT_STRESSES = re.compile(r"1[02]1[02]1[02]1[02]")
CAMPTOWN_STRESSES = re.compile(r"1[02]1[02]1[02]1")
CHARS_ONLY = re.compile("[^a-zA-Z]")
