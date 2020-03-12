class Scoreboard:
    """Fixed-length sequence of high scores in nondecreasing order."""

    def __init__(self, capacity=10):
        """Initialize scoreboard with given maximum capacity."""
        self._board = [None] * capacity