"""
window_class.py

Part of the "Unit Converter for Historical Studies" project by OperaVaria.

Tkinter GUI window as a class.
"""

# Tkinter import:
import tkinter as tk
from platform import system


class Window(tk.Tk):
    """Tkinter GUI window as a class.
       General purpose, multi-platform, optimized for 1080p resolution."""
    def __init__(self, title, geometry, resizable_x, resizable_y, background, start_maximized):
        """Creates a window object."""
        super().__init__()
        self.title(title)
        self.geometry(geometry)
        self.resizable(resizable_x, resizable_y)
        self["bg"] = background
        # Maximized settings.
        if start_maximized and system() == "Windows":
            self.state("zoomed")  # On Windows, start with maximized window.
        elif start_maximized and system() == "Linux":
            self.state("normal")  # On Linux, start "normal" (no "zoomed" mode available).


# Display message when accidentally run:
if __name__ == "__main__":
    print("This file is a module of the \"Unit Converter for Historical Studies\" project."
          "Launch \"main.pyw\" to start the app.")
