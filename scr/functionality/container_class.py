"""
container_class.py

Part of the "Unit Converter for Historical Studies" project by OperaVaria.

Tkinter GUI container frame as a class.
"""

# Built-in module import
from tkinter import ttk


class Container(ttk.Frame):
    def __init__(self, window, width, height, foreground, background, textcolor, fill, expand):
        """Creates a container (frame) object, placed into parent window."""
        super().__init__(window)
        self.cont = ttk.Frame(window, width=width, height=height)
        self.cont.pack(fill=fill, expand=expand)

        # Basic ttk style configuration for application widgets
        self.style = ttk.Style(self)
        self.style.configure("TFrame", background=background)
        self.style.configure("TLabel", foreground=foreground, background=background, font=("Helvetica", 16),
                             justify="center", anchor="center")
        self.style.configure("TLabelframe.Label", font=("Helvetica", 16), foreground=background,
                             background=foreground)
        self.style.configure("TLabelframe", background=background, bordercolor=foreground)
        self.style.configure("TButton", font=("Helvetica", 20), foreground=textcolor, background=background,
                             width=16, height=2, padding=20)
        self.style.configure("S.TButton", width=8, height=2, padding=10)
        self.style.configure("TMenubutton", width=30)
