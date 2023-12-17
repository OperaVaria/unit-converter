"""
functions.py

Part of the "Unit Converter for Historical Studies" project by OperaVaria.

Functions related to backend processes.

GUI switching functions can be found at the end of gui.py
to avoid excessive and circular importing.
"""

# Tk.TclError import:
from tkinter import TclError

# Local imports:
from units.unit_class import Unit
from units.unit_list_length import populate_length
from units.unit_list_area import populate_area
from units.unit_list_weight import populate_weight
from units.unit_list_dimensionless import populate_dimensionless
from units.unit_list_volume import populate_volume_dry
from units.unit_list_volume import populate_volume_liq


def set_act_lists(unit_cat):
    """Function to populate active unit system and active unit object lists.
    Unit objets are nested in functions by category, each in own file."""

    # Clear lists.
    Unit.act_sys_list.clear()
    Unit.act_unit_list.clear()

    # Category selector
    match unit_cat:
        case "Hosszúság":
            populate_length()
        case "Terület":
            populate_area()
        case "Súly":
            populate_weight()
        case "Darabmérték":
            populate_dimensionless()
        case "Szárazmérték":
            populate_volume_dry()
        case "Folyadékmérték":
            populate_volume_liq()
    return


def set_unit_lists(selection, side, gui_page):
    """Setup to populate unit name menu lists with proper units, based on unit system choice."""

    # Clear lists.
    if side == "input":
        gui_page.input_name_list.clear()
    if side == "output":
        gui_page.output_name_list.clear()

    # Unit system selector
    match selection:
        # Metric
        case "metrikus":
            name_lists_append(("SI", "accepted non-SI", "historical metric"), side, gui_page)
        case "SI":
            name_lists_append("SI", side, gui_page)
        case "liter alapú metrikus":
            name_lists_append("litre based metric", side, gui_page)
        # Imperial and US customary
        case "angolszász":
            name_lists_append(("Imperial", "US customary"), side, gui_page)
        case "angolszász avoirdupois":
            name_lists_append("Avoirdupois", side, gui_page)
        case "angolszász troy":
            name_lists_append("Troy", side, gui_page)
        case "angolszász patikai":
            name_lists_append("Apothecaries", side, gui_page)
        case "angolszász köbmérték":
            name_lists_append("AngAm cubic", side, gui_page)
        case "brit (Imperial)":
            name_lists_append("Imperial", side, gui_page)
        case "amerikai (US customary)":
            name_lists_append("US customary", side, gui_page)
        # Greek
        case "attikai":
            name_lists_append("Attic", side, gui_page)
        case "attikai (\"solóni\")":
            name_lists_append("Attic Solonic", side, gui_page)
        case "attikai (késő klasszikus)":
            name_lists_append("Attic LC", side, gui_page)
        case "hellenisztikus":
            name_lists_append("Early Hellenistic", side, gui_page)
        case "késő hellenisztikus":
            name_lists_append("Late Hellenistic", side, gui_page)
        # Roman
        case "római":
            name_lists_append("Roman", side, gui_page)
        case "római (uncia törtrészei)":
            name_lists_append("Roman (uncia fraction)", side, gui_page)
        case "római (uncia-libra)":
            name_lists_append("Roman (uncia-libra)", side, gui_page)
        case "római (libra többszörösei)":
            name_lists_append("Roman (libra multiple)", side, gui_page)
        # Viennese
        case "osztrák/bécsi":
            name_lists_append("Viennese", side, gui_page)
        case "bécsi (15-16. sz.)":
            name_lists_append("Viennese (15-16th c.)", side, gui_page)
        case "bécsi (17. sz.-1756)":
            name_lists_append("Viennese (17th c.-1756)", side, gui_page)
        case "bécsi (1756-1874)":
            name_lists_append("Viennese (1756-1874)", side, gui_page)
        case "bécsi vámsúly (1851-1874)":
            name_lists_append("Viennese customs", side, gui_page)
        case "bécsi (1593-1638)":
            name_lists_append("Viennese (1593-1638)", side, gui_page)
        case "bécsi (1639-1687)":
            name_lists_append("Viennese (1639-1687)", side, gui_page)
        case "bécsi (1688-1755)":
            name_lists_append("Viennese (1688-1755)", side, gui_page)
        case "bécsi (1756-1871)":
            name_lists_append("Viennese (1756-1871)", side, gui_page)
        case "bécsi kisker. (-1359)":
            name_lists_append("Viennese small (-1359)", side, gui_page)
        case "bécsi kisker. (1359-1556)":
            name_lists_append("Viennese small (1359-1556)", side, gui_page)
        case "bécsi kisker. (1557-1568)":
            name_lists_append("Viennese small (1557-1568)", side, gui_page)
        case "bécsi kisker. (1569-1761)":
            name_lists_append("Viennese small (1569-1761)", side, gui_page)
        case "bécsi kisker. (1762-1871)":
            name_lists_append("Viennese small (1762-1871)", side, gui_page)
        case "bécsi nagyker. (-1761)":
            name_lists_append("Viennese wholesale (-1761)", side, gui_page)
        case "bécsi nagyker. (1762-1871)":
            name_lists_append("Viennese wholesale (1762-1871)", side, gui_page)
        # Hungary
        case "magyar (16-18. sz.)":
            name_lists_append("Hungarian (16-18th c.)", side, gui_page)
        case "magyar királyi":
            name_lists_append("Hungarian Royal", side, gui_page)
        case "(osztrák-)magyar":
            name_lists_append("(Austro-)Hungarian", side, gui_page)
        case "katasztrális":
            name_lists_append("Cadastral", side, gui_page)
        case "általános (magyarországi)":
            name_lists_append("General (Hungary)", side, gui_page)
        case "magyarországi török":
            name_lists_append("Turkish", side, gui_page)
        # Buda
        case "budai (-13. sz.)":
            name_lists_append("Buda (-13th c.)", side, gui_page)
        case "budai (14. sz.-1686)":
            name_lists_append("Buda (14th c.-1686)", side, gui_page)
        case "budai (-17. sz.)":
            name_lists_append("Buda (-17th c.)", side, gui_page)
        # Pressburg
        case "pozsonyi":
            name_lists_append("Pressburg", side, gui_page)
        case "pozsonyi (-1854)":
            name_lists_append("Pressburg (-1854)", side, gui_page)
        case "pozsonyi (1854-1874)":
            name_lists_append("Pressburg (1854-1874)", side, gui_page)
        # Selmecbánya/Hungarian mining units
        case "bányamérték (középkor)":
            name_lists_append("Selmec (Medieval)", side, gui_page)
        case "bányamérték (kora újkor)":
            name_lists_append("Selmec (Early Modern)", side, gui_page)
        case "bányamérték (18. sz. köz.-)":
            name_lists_append("Selmec (mid18th c.-)", side, gui_page)
        # Transylvania
        case "erdélyi":
            name_lists_append("Transylvanian", side, gui_page)
        case "erdélyi (1680köz.-1690köz.)":
            name_lists_append("Transylvanian (mid1680s-mid1690s)", side, gui_page)
        case "erdélyi (1690köz.-1721)":
            name_lists_append("Transylvanian (mid1690s-1721)", side, gui_page)
        case "erdélyi (1721-1874)":
            name_lists_append("Transylvanian (1721-1874)", side, gui_page)
        case "erdélyi (-1823)":
            name_lists_append("Transylvanian (-1823)", side, gui_page)
        case "erdélyi (1823-1874)":
            name_lists_append("Transylvanian (1823-1874)", side, gui_page)
        # Other
        case "írópapír":
            name_lists_append("writing paper", side, gui_page)
        case "nyomópapír":
            name_lists_append("printing paper", side, gui_page)

    # The menus need to be reset because of Ttk limitations.
    if side == "input":
        gui_page.mnu_input.set_menu("Kérem válasszon", *gui_page.input_name_list)
        gui_page.mnu_input.state(["!disabled"])
        # Dimensionless units: input system = output system.
        if gui_page.act_cat == "Darab":
            gui_page.mnu_output.set_menu("Kérem válasszon", *gui_page.input_name_list)
            gui_page.mnu_output.state(["!disabled"])
    if side == "output":
        gui_page.mnu_output.set_menu("Kérem válasszon", *gui_page.output_name_list)
        gui_page.mnu_output.state(["!disabled"])
    return


def name_lists_append(unit_system, side, gui_page):
    """Used by 'set_unit_lists' function to append unit name lists."""
    for i in Unit.act_unit_list:
        if i.system in unit_system:
            if side == "input":
                gui_page.input_name_list.append(i.name)
            if side == "output":
                gui_page.output_name_list.append(i.name)
    return


def menu_color_config(menu_name):
    """Ttk.OptionMenus' drop-down menu colors need to be set every time.
    Done with a function for brevity’s sake."""
    menu_name["menu"].config(fg="#3E4C59", bg="#E4E7EB", activeforeground="#E4E7EB", activebackground="#3E4C59")
    return


def calculate(gui_page):
    """Performs final calculation with error handling and rounding."""
    try:
        solution = gui_page.input_value.get() * gui_page.input_inter / gui_page.output_inter
    # Zero division or passing an empty field equals 0 and an error bell.
    except (ZeroDivisionError, TclError):
        solution = 0
        gui_page.bell()
    # The Result is rounded.
    if solution % 1 == 0:
        gui_page.result_value.set(round(solution))
    else:
        gui_page.result_value.set(round(solution, 10))
    return solution
