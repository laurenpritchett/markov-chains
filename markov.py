from random import choice
import sys


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    text_input = open(file_path).read()

    return text_input


def make_chains(text_string, key_word_count):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:
        >>>make_chains("Would you could you in", 3)
        {('Would', 'you', 'could'): ['you', 'you', 'you', 'you'],
        ('you', 'could', 'you'): ['in', 'with','in', 'with']
        }


        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}
    words = text_string.split()
    # loop through words to create tuples as keys for chains dictionary

    for index in range(len(words) - key_word_count):
        # if tuple key found append this value
        key_values = []
        for i in range(key_word_count):
            key_values.append(words[index + i])
        key_values = tuple(key_values)

        if key_values in chains:
            chains[key_values].append(words[index + key_word_count])
        # if tuple not found, create key and add value
        else:
            chains[key_values] = [words[index + key_word_count]]

    # your code goes here
    return chains


def is_capitalized(key):
    if key[0][0].isupper():
        return True
    else:
        return False

def is_ending_punctuation(word):
        if word[-1] in ".!?":
            return True
        else:
            return False

def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    #list of key tuples
    key_choices = chains.keys()

    #randomly selects one key tuple
    while True:
        key = choice(key_choices)
        if is_capitalized(key):
            break

    #initializes text list with first key tuple
    text = []

    for index in range(len(key)):
        text.append(key[index])

    while True:
        if key not in chains:
            break
        else:
            #picking a viable next word from value list for given key
            new_word = choice(chains[key])
            if is_ending_punctuation(new_word):
                text.append(new_word)
                break

            # append next word to text list
            text.append(new_word)

            #advance key for next iteration
            key_as_list = list(key)
            del key_as_list[0]
            key_as_list.append(new_word)
            key = tuple(key_as_list)

    # for bigram, value in chains.iteritems():
    #     text += value

    return " ".join(text)


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# print input_text

# # Get a Markov chain
chains = make_chains(input_text, 2)  # print chains

# Produce random text
random_text = make_text(chains)
print random_text

# print random_text
