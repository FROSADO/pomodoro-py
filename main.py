"""
Main entry point for the Pomodoro Timer application.
"""
import tkinter as tk
from pomopy.gui import PomodoroApp
from pomopy.config import Config


def main():
    """Main function that starts the application."""
    root = tk.Tk()
    config = Config()
    app = PomodoroApp(root, config)
    app.run()


if __name__ == '__main__':
    main()
