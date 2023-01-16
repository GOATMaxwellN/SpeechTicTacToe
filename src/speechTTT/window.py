"""
Module that handles the application window.
"""

from ttt_grid import TTTGrid
from tkinter import *
from tkinter.ttk import *


class Window(Tk):
    """
    Class representing the window of the application.
    """

    # Test sizes
    WIN_HEIGHT = 500
    WIN_WIDTH = 500

    def __init__(self) -> None:
        super().__init__()

        # Set window size
        self.geometry(f"{self.WIN_WIDTH}x{self.WIN_HEIGHT}")

        # Setup grid weights to 1
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Show start screen
        self.show_start_screen()
    
    def show_start_screen(self) -> None:
        """Shows start screen to user.
        
        Screen presents options like 1-2 player and settings"""

        # Create start screen frame that covers entire window.
        start_screen = Frame(self)
        # Setup its grid weights: 1 column, 2 rows.
        start_screen.columnconfigure(0, weight=1)
        start_screen.rowconfigure(0, weight=1)
        start_screen.rowconfigure(1, weight=1)
        start_screen.rowconfigure(2, weight=1)
        start_screen.grid(column=0, row=0, sticky="NSEW")

        # Buttons frame that holds single and two player button.
        btns_frame = Frame(start_screen)
        btns_frame.columnconfigure(0, weight=1)
        btns_frame.rowconfigure(0, weight=1)
        btns_frame.rowconfigure(1, weight=1)
        btns_frame.grid(column=0, row=1, sticky="NSEW")

        # Two main buttons. Single and 2 player.
        single_player_btn = Button(btns_frame, text="Single Player", width=30)
        two_player_btn = Button(
            btns_frame, text="2 Player", command=self.show_game_screen, width=30)
        ipadx, ipady = 30, 10  # Padding used when adding them to grid.
        # Add them to grid
        single_player_btn.grid(
            column=0, row=0, 
            ipadx=ipadx, ipady=ipady)

        two_player_btn.grid(
            column=0, row=1,
            ipadx=ipadx, ipady=ipady)

        # Bottom spacer label crediting OpenAI's Whisper.
        label = Label(start_screen, text="Speech recognition powered by OpenAI's Whisper")
        label.grid(column=0, row=2, sticky="S", pady=(0, 5))  # pady keeps it off the bottom.
    
    def show_game_screen(self) -> None:
        """Shows the game screen with the TicTacToe board"""
        # Create game screen that covers entire window
        game_screen = Frame(self)
        # Setup grid weights
        game_screen.columnconfigure(0, weight=1)
        game_screen.rowconfigure(0, weight=5)
        game_screen.rowconfigure(1, weight=1)
        game_screen.grid(column=0, row=0, sticky="NSEW")

        # Add the tic-tac-toe grid
        self.ttt_grid = TTTGrid(game_screen, background='pink')
        self.ttt_grid.grid(column=0, row=0, sticky="NSEW")
        