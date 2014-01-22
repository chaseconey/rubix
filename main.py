#!/usr/bin/python

import re
import argparse

# String to hold regex
regex = ''

# Create a storage area for sorting words by size
sortedDict = {}

# Setup argument parsing
parser = argparse.ArgumentParser(description='Generate list of valid Words With Friends words from given letters.')

parser.add_argument("letters", help="List of letters to lookup words by.")
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")

args = parser.parse_args()

regex = '^[' + args.letters.lower() + ']+$'

m = re.compile(regex)

# Read in word list
words = [line.strip() for line in open('enable1.txt')]

# Find words that match the letters given
for word in words:
  if (m.match(word) is not None):
    wordLen = len(word)
    # Make sure the key of dict exists
    if wordLen not in sortedDict:
      sortedDict[wordLen] = []

    # Add item to list
    sortedDict[wordLen].append(word)

# If verbose output is enabled
if args.verbose:
  print 'Your letters: ' + args.letters
  print 'Regular expression used: ' + regex
  print '# of words searched: ' + str(len(words))

# Print words by size
for wordLength, words in sortedDict.iteritems():
  print wordLength
  for word in words:
    print ' ' + word

