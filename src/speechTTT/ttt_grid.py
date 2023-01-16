"""Module containing the TTTBoard class."""
from tkinter import Canvas, Tk, Button

class TTTGrid(Canvas):
    """
    A Canvas widget with a tic-tac-toe grid drawn on it, along with methods to 
    modify the board, add x's and o's to the board, and just overall represent
    a game of tic-tac-toe.
    """

    # Y offset from canvas
    Y_OFFSET = 30

    def __init__(self, root, **options):
        super().__init__(root, options)

    def draw_grid(self):
        """Draws an empty ttt grid for the start of the game."""
        # Get height and width of canvas.
        w, h = self.winfo_width(), self.winfo_height()

        # When setting dimensions for the grid, the screen's height will
        # be the main factor. Height will be offset from canvas by a constant
        # amount, and width will be offset from canvas to match heigth.
        grid_y = 0 + self.Y_OFFSET, h - self.Y_OFFSET
        # Required width offset to match height
        x_offset = self._get_required_width_offset(w, (grid_y[1] - grid_y[0]))
        grid_x = 0 + x_offset, w - x_offset

        self.create_rectangle(grid_x[0], grid_y[0], grid_x[1], grid_y[1], outline='black')

    def _get_required_width_offset(self, width: int, height_to_match: int) -> int:
        """Gets required offset (margins) to place on the width of the
        tic-toe-toe grid so the width is the same as the height."""
        return round((width - height_to_match) / 2)

    def add_x(self, cell: int):
        """Adds an X to the specified cell."""
        pass

    def add_o(self, cell: int):
        """Adds an O to the specified cell."""
        pass

    def grid(self, **options):
        """Adds TTTGrid to root element with grid geometry manager and 
        draws the tic-tac-toe grid on the canvas.
        
        Overrides the original grid() method, but only difference is 
        the added call to TTTGrid.draw_grid().
        """
        super().grid(options)
        # Makes sure draw_grid() has the correct width and height for canvas
        self.update_idletasks()
        self.draw_grid()


if __name__ == "__main__":
    root = Tk()
    root.geometry('500x500')
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    grid = TTTGrid(root)
    root.mainloop()
