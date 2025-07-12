# Handles fetching or selecting the daily Bible verse
import random

def get_daily_verse(verses_file='verses.txt'):
    with open(verses_file, 'r') as f:
        verses = [line.strip() for line in f if line.strip()]
    return random.choice(verses)
