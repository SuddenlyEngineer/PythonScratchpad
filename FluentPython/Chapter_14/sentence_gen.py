import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for word in self.words: # Iterate over self.words
            yield word # Yield the current word.
        return # This return is not needed; the function can just "fall-through" and return automatically. Either way, a generator function doesn't raise StopIteration: it simply exits when it's done producing values.

# Done! No need for a separate iterator class!