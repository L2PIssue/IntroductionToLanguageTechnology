import nltk
from nltk.tokenize import word_tokenize

# Let's try the word_tokenize() function on a simple sentence:
print(word_tokenize("Moodle is an on-line resource."))

# Now, let's define a sentence, tokenise it, and POS-tag the list of tokens:
sentence = "And now for something completely different"
tokens = word_tokenize(sentence)
print(nltk.pos_tag(tokens))

# Some words, like race and jump, can be either verbs or nouns. 
# This kind of ambiguity can cause sentences to be tagged incorrectly.
print(nltk.pos_tag(word_tokenize("I permit you to obtain the permit.")))
nltk.help.upenn_tagset('NN')

# Here the tagger function tags both 'water' words to NN
print(nltk.pos_tag(word_tokenize("We should water the plants with cold water.")))

# Some tags include a dollar sign $ (like WP$: WH-pronoun, possessive) but as 
# you might recall, this is also a regex metacharacter. Come up with a pattern 
# that matches any tag that includes an actual dollar sign.
nltk.help.upenn_tagset('.*\$.*')