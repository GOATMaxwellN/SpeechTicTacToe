"""This module holds the TTTGame class, which handles the logic"""
from ttt_grid import TTTGrid
from tkinter import Event  # For typing purposes.
from decorators import run_on_another_thread
import speech_rec as sr
import threading

class TTTGame:
    """This class handles game logic.
    
    Attributes
    ----------
    cell_pressed : int
        Number of the current cell being pressed.
    mouse_pressed_down : bool
        Indicator to if the mouse button is pressed down (not released).
    ignore_release : bool
        Indicator to whether a release event by the mouse should be ignored.
    grid : TTTGrid
        Canvas class representing the tic-tac-toe grid.
    squares : list[str]
        List representing a tic-tac-toe grid.
    turn : str
        Either 'x' or 'o'. Tells whose turn it is.
    """

    # FOR VOICE COMMANDS
    # Key is the hotword. Value is the cell number
    CELL_HOTWORDS = {
        "center": 4
    }

    def __init__(self, grid: TTTGrid):
        self.grid = grid
        self.setup_binds()

        # Mouse variables.
        self.cell_pressed = -1
        self.mouse_pressed_down = False
        self.ignore_release = False

        # Audio variables.
        self.cell_from_voice = -1

        # Game variables.
        self.squares = ["", "", "", "", "", "", "", "", ""]
        self.turn = "x"

        # Start listening for first turn of the game.
        self.listen()

    def setup_binds(self) -> None:
        """Bind the invisible squares on the grid to the user_clicked() when they
        receive a Button-Release event."""
        for i in range(9):
            # Issues with late binding forced me to define a new function with 'i'
            # as a default argument so each cell would be called with the correct
            # cell number.
            def _button_release(event, cell=i):
                self.button_release(event, cell)
            def _button_press(event, cell=i):
                self.button_press(event, cell)
            def _mouse_enter_cell(event, cell=i):
                self.mouse_enter_cell(event, cell)

            cell = self.grid.squares[i]
            self.grid.tag_bind(cell, sequence="<Button1-ButtonRelease>", func=_button_release)
            self.grid.tag_bind(cell, sequence="<Button-1>", func=_button_press)
            self.grid.tag_bind(cell, sequence="<Enter>", func=_mouse_enter_cell)
            self.grid.tag_bind(cell, sequence="<Leave>", func=self.mouse_leave_cell)
        
        # Bind custom event <<Voice-Command>> to the grid
        self.grid.bind("<<Voice-Command>>", lambda event: self.play_turn(-1))

    def play_turn(self, cell: int) -> None:
        """Depending on whoever's turn it is, adds an X or O to the specified cell."""
        # If cell is -1, that means that user made a voice command
        # and cell number can be found in self.cell_from_voice.
        if cell == -1:
            cell = self.cell_from_voice

        # Check if cell is empty.
        if self.squares[cell] == "":
            self.squares[cell] = self.turn
            if self.turn == "x":
                self.grid.add_x(cell)
                self.turn = "o"
            else:
                self.grid.add_o(cell)
                self.turn = "x"
        else:
            # Cell is not empty, so they can't place a symbol here.
            pass

        print(self.squares)

    def button_release(self, event: Event, cell: int) -> None:
        """Function called when the mouse of a user is released."""
        # Reset mouse variables.
        self.mouse_pressed_down = False
        self.cell_pressed = -1
        if self.ignore_release:
            self.ignore_release = False
            return

        self.play_turn(cell)

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

    @run_on_another_thread
    def listen(self) -> None:
        """Listens to microphone for cell number or description."""
        print("Listening...")
        with sr.mic as source:
            audio = sr.recognizer.listen(source)
        print("Detected word")
        
        with open("src/test_speech/tempAudio.wav", "wb") as f:
            f.write(audio.get_wav_data())
            result = sr.model.transcribe(f.name)
        
        self.voice_command(result["text"])

    def voice_command(self, speech: str) -> None:
        """Function that is called when user says a word."""
        # Remove any trailing whitespace and punctuation.
        speech = speech.strip()
        if speech[-1] in "?!.":
            speech = speech[:-1]

        cell = self.CELL_HOTWORDS.get(speech.lower())
        if cell is not None:
            # This is being run in a seperate thread, so generate an event so that
            # Tk altering code is run on the main thread. The altering code being
            # drawing on the canvas (add_x, add_o).
            self.cell_from_voice = cell
            self.grid.event_generate("<<Voice-Command>>")
        else:
            print("Voice command [{}] not recognized".format(speech))  # TODO:

