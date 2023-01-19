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
        super().__init__(root, **options)

    def draw_grid(self) -> None:
        """Draws an empty ttt grid for the start of the game.
        
        First creates the bounding square for the grid then makes
        the lines."""
        self.square_id = self.draw_bounding_square()
        self.draw_grid_lines()

        # These are the squares that will detect clicks, if user chooses to click.
        self.squares = self.draw_squares()

    def draw_bounding_square(self) -> int:
        """Draws the bounding square of the tic-tac-toe grid.
        
        AKA the border of the grid."""
        # Get height and width of canvas.
        w, h = self.winfo_width(), self.winfo_height()

        # When setting dimensions for the grid, the screen's height will
        # be the main factor. Height will be offset from canvas by a constant
        # amount, then width will be offset from canvas to match heigth length.
        grid_y = 0 + self.Y_OFFSET, h - self.Y_OFFSET
        # Required width offset to match height
        x_offset = self._get_required_width_offset(w, (grid_y[1] - grid_y[0]))
        grid_x = 0 + x_offset, w - x_offset

        # Draw the bounding square and return its id
        return self.create_rectangle(grid_x[0], grid_y[0], grid_x[1], grid_y[1], outline="black")

    def draw_grid_lines(self) -> None:
        """Draws the grid lines in the bounding square, completing the tic-tac-toe grid."""
        # The top left coords of the bounding square will be treated like the origin.
        o = self.coords(self.square_id)
        # Get gap between each row and column line: (width) / 3.
        gap = round((o[2] - o[0]) / 3)
        
        # Draw the vertical lines.
        self.create_line(o[0] + gap, o[1], o[0] + gap, o[3])
        self.create_line(o[0] + 2*gap, o[1], o[0] + 2*gap, o[3])

        # Draw the horizontal lines
        self.create_line(o[0], o[1] + gap, o[2], o[1] + gap)
        self.create_line(o[0], o[1] + 2*gap, o[2], o[1] + 2*gap)

    def draw_squares(self):
        """Draws invisible squares that will be used to detect when user clicks on a
        cell on the tic-tac-toe grid.
        
        They're invisible because the border and grid lines already create the
        effect of a tic-tac-toe grid, so there is no need to give them any
        appearance."""
        # The top left coords of the bounding will be treated like the origin.
        o = self.coords(self.square_id)
        # Get side lengths of the squares
        side_length = round((o[2] - o[0]) / 3)

        squares = []
        row = col = 0
        # Squares are created from the top left, row by row.
        for i in range(9): 
            w_offset, h_offset = col*side_length, row*side_length
            rect_id = self.create_rectangle(
                o[0] + w_offset, o[1] + h_offset, 
                o[0] + w_offset + side_length, o[1] + h_offset + side_length,
                outline="")  # outline="" gives no outline to the rectangle, would default to black.
            squares.append(rect_id)

            row += 1
            if row % 3 == 0:
                row = 0
                col += 1
        
        return squares

    def _get_required_width_offset(self, width: int, height_to_match: int) -> int:
        """Gets required offset (margins) to place on the width of the
        tic-toe-toe grid so the width is the same as the height."""
        return round((width - height_to_match) / 2)

    def add_x(self, cell: int) -> None:
        """Adds an X to the specified cell."""
        pass

    def add_o(self, cell: int) -> None:
        """Adds an O to the specified cell."""
        pass

    def grid(self, **options) -> None:
        """Adds TTTGrid to root element with grid geometry manager and 
        draws the tic-tac-toe grid on the canvas.
        
        Overrides the original grid() method, but only difference is 
        the added call to TTTGrid.draw_grid().
        """
        super().grid(**options)
        # Makes sure draw_grid() has the correct width and height for canvas
        self.update_idletasks()
        self.draw_grid()

    def create_line(self, *args, **options) -> int:
        """Overrides Canvas.create_line() to make black the default line color."""
        if "fill" in options:
            return super().create_line(*args, **options)

        return super().create_line(*args, **options, fill="black")


if __name__ == "__main__":
    root = Tk()
    root.geometry('500x500')
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    grid = TTTGrid(root)
    root.mainloop()
