"""
window_class.py

Part of the "Unit Converter for Historical Studies" project by OperaVaria.

Tkinter GUI window as a class.
"""

# Tkinter import:
import tkinter as tk


class Window(tk.Tk):
    def __init__(self, title, geometry, resizable_x, resizable_y, background):
        """Creates a window object."""
        super().__init__()
        self.title(title)
        self.geometry(geometry)
        self.resizable(resizable_x, resizable_y)
        self["bg"] = background
