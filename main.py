"""
Main entry point for the Pomodoro Timer application.
"""
import flet as ft
from pomopy.gui_flet import main as flet_main


def main():
    """Main function that starts the application."""
    ft.app(target=flet_main)


if __name__ == '__main__':
    main()
