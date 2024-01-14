"""
main.py

Unit Converter for Historical Studies

This Python app is a simple converter for historical measurement units. For the moment, the app it is only available
with a Hungarian UI, and features historical unit systems mainly associated with Austria and Hungary, as well as the
Ancient Greek and Roman measurements. However, any unit system can be implemented. All modern metric and Anglo-American
units are added for reference. The converter uses the Tkinter GUI toolkit with ttk widgets, the unit database was
built with the SQLite database engine.

NB. This is my first ever coding project in any language.

TODO: 1. Lost of testing, bug hunting, typo fixing.
      2. Add more unit systems.
      3. Possibly add coin weights.
      4. Implement multi-language GUI.
"""

# Metadata variables:
__author__ = "OperaVaria"
__contact__ = "lcs_it@proton.me"
__version__ = "0.1.0"
__date__ = "2024.01.14"

# Written in: Python 3.12
# Tcl/Tk version 8.6
# SQLite version 3.35.5
# Encoding: UTF-8
# Tested on Windows 10, 11, Ubuntu 23.10, and Lubuntu 22.04 LTS.

# Important NB.: when needed, name collision is avoided with invisible characters U+1D173-77 in the database.

# Licence:
__license__ = "GPLv3"
__copyright__ = "Copyright © 2023, Csaba Latosinszky"

"""
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not,
see <https://www.gnu.org/licenses/>
"""

# Import launching function:
from functionality.gui import launch_main


# Launch main window, menu frame, main menu, and window mainloop:
if __name__ == "__main__":
    launch_main()
