"""
Starts the application.
"""
from window import Window


def start() -> None:
    """Starts the application.
    
    Creates a Window instance which sets up the GUI and game logic and starts
    its event loop.
    """
    win = Window()
    win.mainloop()


if __name__ == "__main__":
    start()