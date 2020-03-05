import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self): # The iter method is the only addition to the previous sentence implementation. This version has no getitem, to make it clear that the class is iterable because it implements iter.
        return SentenceIterator(self.words) # iter fulfils the iterable protocol by instantiating and returning an iterator. Unnecessary, but makes SentenceIterator pass the issubclass(SentenceIterator, abc.Iterator) test


class SentenceIterator:

    def __init__(self, words):
        self.words = words # SentenceIterator holds a reference to the list of words.
        self.index = 0  # self.index is used to determine the next word to fetch.

    def __next__(self):
        try:
            word = self.words[self.index] # Get the word at self.index
        except IndexError:
            raise StopIteration() # If there is no word at self.index, raise StopIteration.
        self.index += 1 # Increment self.index
        return word # Return the word.

    def __iter__(self): # Implement self.__iter__
        return self