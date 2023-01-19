"""This module holds the TTTGame class, which handles the logic"""
from functools import partial
from ttt_grid import TTTGrid

class TTTGame:
    """This class handles game logic."""

    def __init__(self, grid: TTTGrid):
        self.grid = grid
        self.setup_binds()

    def setup_binds(self):
        """Bind the invisible squares on the grid to the user_clicked() when they
        receive a Button-Release event."""
        for i in range(9):
            # Issues with late binding forced me to define a new function with 'i'
            # as a default argument so each cell would be called with the correct
            # cell number.
            def func(event, cell=i):
                self.user_clicked(event, cell)
            self.grid.tag_bind(self.grid.squares[i], sequence="<Button1-ButtonRelease>", func=func)

    def user_clicked(self, event, cell: int):
        print("Square has been clicked")
        print(event, f"Cell {cell}")