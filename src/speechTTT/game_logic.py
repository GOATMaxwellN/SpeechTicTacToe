"""This module holds the TTTGame class, which handles the logic"""
from ttt_grid import TTTGrid
from tkinter import Event  # For typing purposes.

class TTTGame:
    """This class handles game logic.
    
    Attributes
    ----------
    cell_pressed : int
        Number of the current cell being pressed.
    mouse_pressed_down : boolean
        Indicator to if the mouse button is pressed down (not released).
    ignore_release : boolean
        Indicator to whether a release event by the mouse should be ignored.
    grid : TTTGrid
        Canvas class representing the tic-tac-toe grid.
    """

    def __init__(self, grid: TTTGrid):
        self.cell_pressed = -1
        self.mouse_pressed_down = False
        self.ignore_release = False
        self.grid = grid
        self.setup_binds()

    def setup_binds(self) -> None:
        """Bind the invisible squares on the grid to the user_clicked() when they
        receive a Button-Release event."""
        for i in range(9):
            # Issues with late binding forced me to define a new function with 'i'
            # as a default argument so each cell would be called with the correct
            # cell number.
            def _user_clicked(event, cell=i):
                self.user_clicked(event, cell)
            def _button_press(event, cell=i):
                self.button_press(event, cell)
            def _mouse_enter_cell(event, cell=i):
                self.mouse_enter_cell(event, cell)

            cell = self.grid.squares[i]
            self.grid.tag_bind(cell, sequence="<Button1-ButtonRelease>", func=_user_clicked)
            self.grid.tag_bind(cell, sequence="<Button-1>", func=_button_press)
            self.grid.tag_bind(cell, sequence="<Enter>", func=_mouse_enter_cell)
            self.grid.tag_bind(cell, sequence="<Leave>", func=self.mouse_leave_cell)

    def user_clicked(self, event: Event, cell: int) -> None:
        """Function called when the mouse of a user is released."""
        self.mouse_pressed_down = False
        self.cell_pressed = -1
        if self.ignore_release:
            self.ignore_release = False
            return
        
        print(event, f"Cell {cell}")

    def button_press(self, event: Event, cell: int) -> None:
        """Function called when the mouse of a user is pressed."""
        self.mouse_pressed_down = True
        self.cell_pressed = cell

    def mouse_enter_cell(self, event: Event, cell: int) -> None:
        """Function called when the pointer enters a cell."""
        # If mouse reenters the cell it was originally pressed in while still being
        # pressed down, do not ignore release event.
        if cell == self.cell_pressed:
            self.ignore_release = False

    def mouse_leave_cell(self, event: Event) -> None:
        """Function called when pointer leaves a cell."""
        # If the mouse is pressed in a cell then leaves that cell before releasing,
        # ignore the release event that occurs (unless they reenter the cell they left).
        if self.mouse_pressed_down:
            self.ignore_release = True