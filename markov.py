from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    text_input = open(file_path).read()

    return text_input


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}
    words = text_string.split()
    # loop through words to create tuples as keys for chains dictionary
    for index in range(len(words) - 2):
        # if tuple key found append this value
        if (words[index], words[index+1]) in chains:
            chains[(words[index], words[index+1])].append(words[index + 2])
        # if tuple not found, create key and add value
        else:
            chains[(words[index], words[index+1])] = [words[index + 2]]

    # your code goes here

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""
    key_choices = chains.keys()
    key = choice(key_choices)

    text = key[0] + " " + key[1]

    while True:
        if key not in chains:
            break
        else:
            new_word = choice(chains[key])
            text = text + " " + new_word
            key = (key[1], new_word)

    # for bigram, value in chains.iteritems():
    #     text += value

    return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

print input_text

# # Get a Markov chain
chains = make_chains(input_text)
print chains

# Produce random text
random_text = make_text(chains)
print random_text

# print random_text
