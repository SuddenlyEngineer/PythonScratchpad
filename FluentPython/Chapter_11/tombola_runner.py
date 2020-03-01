import doctest

from tombola import Tombola

# modules to test
import bingo, lotto, tombolist # Import modules containing real or virtual subclasses 

TEST_FILE = 'tombola_tests.rst'
TEST_MSG = '{0:16} {1.attempted:2} tests, {1.failed:2} failed - {2}'


def main(argv):
    verbose = '-v' in argv
    real_subclasses = Tombola.__subclasses__() # __subclasses__() lists the direct descendants that are alive in memory. That’s why we imported the modules to test, even if there is no further mention of them in the source code: to load the classes into memory.
    virtual_subclasses = list(Tombola._abc_registry) # Build a list from _abc_registry (which is a WeakSet) so we can concatenate it with the result of __subclasses__().

    for cls in real_subclasses + virtual_subclasses: # Iterate over the subclasses found, passing each to the test function.
        test(cls, verbose)


def test(cls, verbose=False):

    res = doctest.testfile(
            TEST_FILE,
            globs={'ConcreteTombola': cls}, # The cls argument - the class to be tested - is bound to the name ConcereteTombola in the global namespace provided to run the doctest.
            verbose=verbose,
            optionflags=doctest.REPORT_ONLY_FIRST_FAILURE)
    tag = 'FAIL' if res.failed else 'OK'
    print(TEST_MSG.format(cls.__name__, res, tag)) # The test result is printed with the name of the class, the number of tests attempted, tests failed, and an OK or FAIL label.


if __name__ == '__main__':
    import sys
    main(sys.argv)