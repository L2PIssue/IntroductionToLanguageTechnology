import re

# let's test functions from re on a simple sentence
sentence = 'I imported a module, defined a sentence and pattern, checked for matches, and rejoiced.'
pattern = r'\w+ed\W'
print(re.findall(pattern,sentence))

# instead of a simple string, we'll give Python a file object to work with
dict = open('dictionary.txt', 'r').read()

# let's say we're interested in words ending with "-anny"
pattern = r'(\w+anny\b)'
print(re.findall(pattern,dict))

# let's look for numbers denoting years of the 1800s
pattern = r'18\d\d'
re.findall(pattern,dict)
print(len(re.findall(pattern,dict)))