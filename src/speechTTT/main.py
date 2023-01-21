"""
Starts the application.
"""
from window import Window
import speech_rec


def start() -> None:
    """Starts the application.
    
    Creates a Window instance which sets up the GUI and game logic and starts
    its event loop.
    """
    win = Window()
    speech_rec.init()
    win.mainloop()


if __name__ == "__main__":
    start()