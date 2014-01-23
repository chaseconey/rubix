#!/usr/bin/python

import re
import argparse
import time

# Let's time the execution for display in -v
start_time = time.time()

# String to hold regex
regex = ''

# Create a storage area for sorting words by size
sortedDict = {}

# For comparison, let's keep record of the sorted string of characters that was input
sortedLetters = ''

# Setup argument parsing
parser = argparse.ArgumentParser(description='Generate list of valid Words With Friends words from given letters.')

parser.add_argument("letters", help="List of letters to lookup words by.")
parser.add_argument("-p", "--pivot", help="Letter that MUST be included.", default='')
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")

args = parser.parse_args()

sortedLetters = ''.join(sorted(args.letters + args.pivot.lower()))

regex = '^[' + args.letters.lower() + args.pivot.lower() + ']+$'

m = re.compile(regex)

# Read in word list
words = [line.strip() for line in open('enable1.txt')]

# Find words that match the letters given
for word in words:
  if m.match(word) is not None:

    sortedWord = ''.join(sorted(word))

    # Because our regex allows for having multiple of a letter that is given, let's check that they didn't overuse
    # the letters allowed using another very simple regex function
    letterCheckRegex = ''
    for letter in sortedWord:
      letterCheckRegex += letter + '?'

    check = re.compile('(' + letterCheckRegex + ')')

    if check.match(sortedLetters) is None:
      continue

    # Check that the letter that is required is in the string
    if args.pivot and args.pivot not in word:
      continue

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
  print ''

# Print words by size
for wordLength, words in sortedDict.iteritems():
  print wordLength
  print words

if args.verbose:
  print ''
  print 'Ececution time: ' + str(time.time() - start_time) + ' seconds'