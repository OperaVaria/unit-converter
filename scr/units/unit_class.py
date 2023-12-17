"""
unit_class.py

Part of the "Unit Converter for Historical Studies" project by OperaVaria.

Measurement unit class.

Sources for unit values and background information are cited in list files.
List of cited works can be found in "docs/Sources.md".
"""


class Unit:
    """ A single object of a single measurement unit."""

    # Creates a list for selectable unit systems.
    act_sys_list = []

    # Creates a list for active Unit objects.
    act_unit_list = []

    def __init__(self, name, info, symbol, system, category, inter_val):
        """ Gives unit necessary attributes and appends it to the active object lst."""
        self.name = name
        self.info = info
        self.symbol = symbol
        self.system = system
        self.category = category
        self.inter_val = inter_val
        Unit.act_unit_list.append(self)
