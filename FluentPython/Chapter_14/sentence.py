import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text) # re.findall returns a list with all nonoverlapping matches of the regex, as a list of strings.

    def __getitem__(self, index):
        return self.words[index] # self.words holds the result of .findall, so we simply return the word at the given index.

    def __len__(self): # To complete the sequence protocol, we implement __len__, but it is not needed to make an iterable object.
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text) # reprlib.repr is a utility function to generate abbreviated string representations of data structures that can be very large.