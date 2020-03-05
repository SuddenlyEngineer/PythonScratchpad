import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self): # This is not a generator function (it has no yield) but uses a generator expression to build a generator and then returns it.
        return (match.group() for match in RE_WORD.finditer(self.text))