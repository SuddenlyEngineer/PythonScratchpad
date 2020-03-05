class ArithmeticProgression:

    def __init__(self, begin, step, end=None): # __init__ requires two arguments: begin and step, end is optional, if it's None, the series will be unbounded. 
        self.begin = begin
        self.step = step
        self.end = end  # None -> "infinite" series

    def __iter__(self):
        result = type(self.begin + self.step)(self.begin) # This line produces a result value equal to self.begin, but coerced to the type of the subsequent additions.
        forever = self.end is None # For readability, the forever flag will be True if the self.end attribute is None, resulting in an unbounded series.
        index = 0
        while forever or result < self.end: # This loop runs forever or until the result matches or exceeds self.end. When this loop exits, so does the function.
            yield result # The current result is produced.
            index += 1
            result = self.begin + self.step * index # The next potential result is calculated. Is may never be yielded, because the while loop may terminate. 