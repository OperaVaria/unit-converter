"""
unit_class.py

Part of the "Unit Converter for Historical Studies" project by OperaVaria.

Measurement unit class.

The sources of unit values and background information are cited
in the database file (unit_database.db).

The list of cited works can be found in "docs/Sources.md".
"""


class Unit:
    """All needed information about a measurement unit in Python object form."""

    # Creates a list for active Unit objects.
    act_obj_list = []

    def __init__(self, name, info, symbol, sys_dat, sys_gui, category, source, inter_val):
        """Gives a Unit instance the necessary attributes,
           and appends it to the active object list."""
        self.name = name
        self.info = info
        self.symbol = symbol
        self.system_data = sys_dat
        self.system = sys_gui
        self.category = category
        self.source = source
        self.inter_val = inter_val
        Unit.act_obj_list.append(self)


# Display message when accidentally run:
if __name__ == "__main__":
    print("This file is a module of the \"Unit Converter for Historical Studies\" project."
          "Launch \"main.pyw\" to start the app.")
