"""
system_class.py

Part of the "Unit Converter for Historical Studies" project by OperaVaria.

Measurement unit system class.

The sources of unit values and background information are cited
in the database file (unit_database.db).

The list of cited works can be found in "docs/Sources.md".
"""


class System:
    """All needed information about a unit system in Python object form."""

    # Creates a list for active System objects.
    act_obj_list = []

    def __init__(self, name_dat, name_gui, info, source, category):
        """Gives a System instance the necessary attributes,
           and appends it to the active object list."""
        self.name_data = name_dat
        self.name = name_gui
        self.info = info
        self.source = source
        self.category = category
        System.act_obj_list.append(self)


# Display message when accidentally run:
if __name__ == "__main__":
    print("This file is a module of the \"Unit Converter for Historical Studies\" project."
          "Launch \"main.pyw\" to start the app.")
