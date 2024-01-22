"""
container_class.py

Part of the "Unit Converter for Historical Studies" project by OperaVaria.

Tkinter GUI container frame as a class.
"""

# Built-in module imports:
from tkinter import ttk
from platform import system


class Container(ttk.Frame):
    """Ttk GUI container as a class.
       General purpose, multi-platform, optimized for 1080p resolution."""
    def __init__(self, window, width, height, fill, expand, background,
                 foreground, textcolor, font):
        """Creates a container (frame) object, placed into parent window."""
        super().__init__(window)
        self.cont = ttk.Frame(window, width=width, height=height)
        self.cont.pack(fill=fill, expand=expand)
        # Set ttk style:
        self.style = ttk.Style(self)
        # Ttk theme selection for different OSs:
        if system() == "Windows":
            self.style.theme_use("vista")
        elif system() == "Linux":
            self.style.theme_use("clam")
        # Ttk style configuration for application widgets (1080p):
        self.style.configure("TFrame", background=background)
        self.style.configure("TLabel", background=background, foreground=foreground,
                             font=(font, 18))
        self.style.configure("LF.TLabel", background=background, foreground=foreground,
                             font=(font, 16, "italic"))
        self.style.configure("TLabelframe.Label", background=background, foreground=foreground,
                             font=(font, 18))
        self.style.configure("TLabelframe", background=background, bordercolor=foreground,
                             labeloutside=True, labelmargins=12)
        self.style.configure("TMenubutton", background=foreground, foreground=textcolor,
                             font=(font, 12), width=35)
        self.style.configure("TEntry", foreground=textcolor, selectbackground=textcolor,
                             padding=2)
        self.style.configure("TSeparator", background=textcolor)
        # Button setting for different themes:
        if self.style.theme_use() == "vista":
            self.style.configure("TButton",  background=background, foreground=textcolor,
                                 font=(font, 24), width=20, height=12, padding=30)
            self.style.configure("S.TButton", background=background, foreground=textcolor,
                                 font=(font, 20), width=10, height=6, padding=15)
        elif self.style.theme_use() == "clam":
            self.style.configure("TButton",  background=foreground, foreground=textcolor,
                                 font=(font, 24), width=20, height=12, padding=30)
            self.style.configure("S.TButton", background=foreground, foreground=textcolor,
                                 font=(font, 20), width=10, height=6, padding=15)


# Display message when accidentally run:
if __name__ == "__main__":
    print("This file is a module of the \"Unit Converter for Historical Studies\" project."
          "Launch \"main.pyw\" to start the app.")
