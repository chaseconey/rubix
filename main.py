#!/usr/bin/python

import re

#letters = raw_input("Enter your letters: ");
letters = 'vtlarxrz'

# Format regex for 0-1 uses of each letter
regex = ''
for char in letters:
  regex += char + '?'

m = re.compile('^' + regex.lower() + '$')

# Read in word list
words = [line.strip() for line in open('enable1.txt')]

# Create a storage area for sorting words by size
sortedDict = {}

# Find words that match the letters given
for word in words:
  if (m.match(word) is not None):
    wordLen = word.__len__()
    # Make sure the key of dict exists
    if wordLen not in sortedDict:
      sortedDict[wordLen] = []

    # Add item to list
    sortedDict[wordLen].append(word)

# Print words by size
for wordLength, words in sortedDict.iteritems():
  print wordLength
  for word in words:
    print ' ' + word
