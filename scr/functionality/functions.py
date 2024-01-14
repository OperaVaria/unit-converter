"""
functions.py

Part of the "Unit Converter for Historical Studies" project by OperaVaria.

Functions related to backend processes.

GUI switching functions can be found at the end of gui.py
to avoid excessive and circular importing.
"""

# Built-in module imports:
import sqlite3
from tkinter import TclError
from decimal import Decimal, getcontext, Overflow, InvalidOperation

# Local imports:
from units.system_class import System
from units.unit_class import Unit


def set_act_objs(calc_page):
    """Build active unit system and active unit object lists from the database."""
    # Clear lists.
    System.act_obj_list.clear()
    Unit.act_obj_list.clear()
    # Declare matched_cat so the IDE won't complain.
    matched_cat = ("n/a", "n/a")
    # Category variable selector (sqlite needs a tuple).
    match calc_page.act_cat:
        case "Hosszúság":
            matched_cat = ("length", None)
        case "Terület":
            matched_cat = ("area", None)
        case "Súly":
            matched_cat = ("weight", None)
        case "Darabmérték":
            matched_cat = ("dimensionless", None)
        case "Szárazmérték":
            matched_cat = ("volume (general)", "volume (dry)")
        case "Folyadékmérték":
            matched_cat = ("volume (general)", "volume (liquid)")
    # SQLite connection.
    con = sqlite3.connect("units/unit_database.db")
    cur = con.cursor()
    # Create active system objects.
    for row in cur.execute("SELECT * FROM system_list WHERE category = ? OR category = ?", matched_cat):
        System(*row)
    # Create active unit objects.
    for row in cur.execute("SELECT * FROM unit_list WHERE category = ? OR category = ?", matched_cat):
        Unit(*row)
    # Close connection.
    con.close()
    return


def set_sys_name_list(calc_page):
    """Populate system name list for menu functionality."""
    # Clear system name list.
    calc_page.sys_name_list.clear()
    # Fill system name list form object.name attributes.
    for i in System.act_obj_list:
        calc_page.sys_name_list.append(i.name)
    return calc_page.sys_name_list


def set_input_menu(selection, calc_page):
    """Setup input unit menu after unit system selection."""
    # Clear input unit name list.
    calc_page.input_name_list.clear()
    # Fill name list form object.name attributes.
    for i in Unit.act_obj_list:
        if i.system == selection:
            calc_page.input_name_list.append(i.name)
    # Menus need to be reset because of ttk limitations.
    calc_page.mnu_input.set_menu("Kérem válasszon", *calc_page.input_name_list)
    calc_page.mnu_input.state(["!disabled"])
    # Dimensionless units: input system = output system.
    if calc_page.act_cat == "Darabmérték":
        calc_page.mnu_output.set_menu("Kérem válasszon", *calc_page.input_name_list)
        calc_page.mnu_output.state(["!disabled"])
    return calc_page.input_name_list


def set_output_menu(selection, calc_page):
    """Setup output unit menu after unit system selection."""
    # Clear output unit name list.
    calc_page.output_name_list.clear()
    # Fill name list form object attributes.
    for i in Unit.act_obj_list:
        if i.system == selection:
            calc_page.output_name_list.append(i.name)
    # Menus need to be reset because of ttk limitations.
    calc_page.mnu_output.set_menu("Kérem válasszon", *calc_page.output_name_list)
    calc_page.mnu_output.state(["!disabled"])
    return calc_page.output_name_list


def set_input_sys_info(selection, calc_page):
    """Update input system info widget and reset previous unit data."""
    # Set input system info box from object data.
    for i in System.act_obj_list:
        if i.name == selection:
            calc_page.input_sys_info.set(i.info)
    # Reset input unit info box, symbol, and intermediary.
    calc_page.input_unit_info.set("–––")
    calc_page.input_symbol = "n/a"
    calc_page.input_inter = "n/a"
    return calc_page.input_sys_info


def set_output_sys_info(selection, calc_page):
    """Update output system info widget and reset previous unit data."""
    # Set output system info box from object data.
    for i in System.act_obj_list:
        if i.name == selection:
            calc_page.output_sys_info.set(i.info)
    # Reset output unit info box, symbol, and intermediary.
    calc_page.output_unit_info.set("–––")
    calc_page.output_symbol = "n/a"
    calc_page.output_inter = "n/a"
    return calc_page.output_sys_info


def drop_menu_config(option_menu):
    """Ttk.OptionMenu's drop-down menu needs to be configured every time.
       Done with a function for brevity’s sake."""
    option_menu["menu"].config(bg="#E4E7EB", fg="#3E4C59", activebackground="#3E4C59", activeforeground="#E4E7EB",
                               font=("Helvetica", 12))
    return


def calculate(calc_page):
    """Performs final calculation with error handling and rounding."""
    # Calculation with the decimal module.
    try:
        solution = (Decimal(calc_page.input_value.get())
                    * Decimal(calc_page.input_inter)
                    / Decimal(calc_page.output_inter))
        # Final result rounded to 10 decimals and normalized to the simplest form.
        getcontext().prec = 10
        calc_page.result_value.set(solution.normalize())
    # Zero division, overflow, incomplete selection, or passing an empty field displays an error.
    except (ZeroDivisionError, Overflow, InvalidOperation, TclError):
        solution = "Error"
        calc_page.result_value.set(solution)
        calc_page.bell()
    return solution


# Display message when accidentally run:
if __name__ == "__main__":
    print("This file is a module of the \"Unit Converter for Historical Studies\" project. Launch \"main.pyw\" to "
          "start the app.")
