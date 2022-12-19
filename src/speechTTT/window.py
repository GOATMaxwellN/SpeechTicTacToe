"""
Module that handles the application window.
"""

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
