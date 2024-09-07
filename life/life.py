"""The "life" module within the "Chapter 4 Package"."""

import numpy as np
from matplotlib import pyplot
from scipy.signal import convolve2d

glider = np.array([
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1]
])

blinker = np.array([
    [0, 0, 0],
    [1, 1, 1],
    [0, 0, 0]
])

glider_gun = np.array([
    [0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0]
])


class Game:
    """A Game of Life."""

    def __init__(self, size):
        """Set up the Game of life with a grid size of size x size."""
        self.board = np.zeros((size, size))

    def play(self):
        """Set the Game of life into motion."""
        print("Playing life. Press ctrl + c to stop.")
        pyplot.ion()
        while True:
            self.move()
            self.show()
            pyplot.pause(0.0000005)

    def move(self):
        """
        Move forward a timestep.

        Count the neighbours of each cell and determine whether or not
        the current cell should be updated according to the number of
        neighbours.
        """
        stencil = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
        neighbour_count = convolve2d(self.board, stencil, mode='same')

        for i in range(self.board.shape[0]):
            for j in range(self.board.shape[1]):
                self.board[i, j] = (
                    1 if (
                        # Implement rules of the GoL, if 3 neightbours then 1
                        # else 0.
                        neighbour_count[i, j] == 3
                        or (
                            neighbour_count[i, j] == 2
                            and self.board[i, j]
                        )
                    )
                    else 0
                )

    def __setitem__(self, key, value):
        """Overwrite setter for item."""
        self.board[key] = value

    def show(self):
        """Show the game on a pyplot."""
        pyplot.clf()
        pyplot.matshow(self.board, fignum=0, cmap='binary')
        pyplot.show()

    def insert(self, pattern, coords):
        """Insert a pattern on the board at a specified position."""
        print("Inserting pattern...")
        if not isinstance(pattern, Pattern):
            print("ERROR: pattern not pattern")
            raise ValueError("pattern must be of type 'Pattern'.")
        elif len(coords) != 2:
            print("Coords not 2")
            raise ValueError("coords must be a length-2 sequence.")
        elif np.shape(pattern.grid) == (3, 3):
            print(pattern.grid)
            self[coords[0]-1:coords[0]+2,
                 coords[1]-1:coords[1]+2] = pattern.grid
        else:
            print("Other problem:")
            print("Pattern:")
            print(pattern.grid)
            print("Pattern shape:")
            print(np.shape(pattern.grid))
            print("Coords:")
            print(coords)
            return NotImplemented


class Pattern:
    """
    A pattern in the Game of Life.

    A pattern maintains its behaviour if translated, reflected or rotated.
    """

    def __init__(self, pattern):
        """Initialise the pattern with a pattern that is a numpy array."""
        if not isinstance(pattern, np.ndarray):
            raise ValueError(
                "Pattern must be a numpy array, not a "
                f"{type(pattern)}")
        elif len(pattern) == 0:
            raise ValueError(
                "Pattern must not be an empty array")
        else:
            self.grid = pattern

    def flip_vertical(self):
        """Flip the pattern in the vertical direction."""
        return Pattern(self.grid[::-1])

    def flip_horizontal(self):
        """Flip the pattern in the horizontal direction."""
        return Pattern(self.grid[:, ::-1])

    def flip_diag(self):
        """Flip the pattern in the diagonal."""
        return Pattern(self.grid.transpose())

    def rotate(self, n):
        """Rotate the pattern anticlockwise n times."""
        if n % 4 == 0:
            return Pattern(self.grid)
        if n % 4 == 1:
            return self.flip_diag().flip_vertical()
        if n % 4 == 2:
            return self.flip_vertical().flip_horizontal()
        if n % 4 == 3:
            return self.flip_diag().flip_horizontal()
