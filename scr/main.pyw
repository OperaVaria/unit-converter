"""
main.py

Unit Converter for Historical Studies

This Python app is a simple converter for historical measurement units. At the moment it has a Hungarian UI,
and features historical unit systems mainly associated with Austria and Hungary, as well as the Ancien Greek
and Roman measurements. However, any unit system can be implemented. All modern metric and Anglo-American units are
added for reference. The converter uses the Tkinter GUI toolkit with ttk widgets.

NB. This is my first ever coding project in any language.

TODO: 1. Lost of testing, bug hunting, typo fixing.
      2. Add more unit systems, especially volume.
      3. Possibly implement an info page for more background information on
         units and unit systems.
      4. Possibly add coin weights.
      5. Convert the unit database to a more suitable file type.
      6. More appealing ttk theming.
      7. Implement multi-language GUI.
"""

# Metadata variables:
__author__ = "OperaVaria"
__contact__ = "lcs_it@gmail.com"
__version__ = "0.0.1"
__date__ = "2023.12.17"

# Written in: Python 3.11
# Tcl/Tk version 8.6
# Encoding: UTF-8
# Tested on Windows 10, 11, and Lubuntu 22.04 LTS (Tkinter looks absolutely hideous on LXQt)

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
