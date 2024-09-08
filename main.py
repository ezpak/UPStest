import tkinter as tk
from gui.app import Application
from logger import setup_logger

def main():
    # Set up logging
    logger = setup_logger()

    # Create the main application window
    root = tk.Tk()
    app = Application(master=root, logger=logger)
    app.mainloop()

if __name__ == "__main__":
    main()
