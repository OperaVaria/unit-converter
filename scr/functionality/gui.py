"""
gui.py

Part of the "Unit Converter for Historical Studies" project by OperaVaria.

Classes, methods, functions related to GUI functionality.

GUI switching functions are placed here to avoid import loops.
"""

###########
# Imports #
###########

# Built-in module imports:
import tkinter as tk
from tkinter import ttk

# Local imports:
from units.unit_class import Unit
from functionality.window_class import Window
from functionality.container_class import Container
from functionality.functions import set_unit_lists
from functionality.functions import set_act_lists
from functionality.functions import calculate
from functionality.functions import menu_color_config


###########
# Classes #
###########


class Menu(ttk.Frame):
    def __init__(self, window, parent):
        """Main menu widget structure to be placed into a parent container (frame)."""
        super().__init__(parent)

        # Grid weight setup (6 rows, 3 columns)
        parent.grid_rowconfigure(0, weight=2)
        parent.grid_rowconfigure(1, weight=1)
        parent.grid_rowconfigure(2, weight=1)
        parent.grid_rowconfigure(3, weight=1)
        parent.grid_rowconfigure(4, weight=1)
        parent.grid_rowconfigure(5, weight=2)
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_columnconfigure(1, weight=1)
        parent.grid_columnconfigure(2, weight=1)

        # Titles
        self.lbl_title = ttk.Label(parent, text="Mértékegységváltó a történeti tudományok\nszámára",
                                   font=("Helvetica", 40))
        self.lbl_title.grid(row=0, column=0, columnspan=3)

        self.lbl_subtitle = ttk.Label(parent, text="Metrikus, angolszász, hagyományos, történelmi\n",
                                      font=("Helvetica", 20))
        self.lbl_subtitle.grid(row=1, column=0, columnspan=3)

        # Buttons
        self.btn_length = ttk.Button(parent, text="Hosszúság",
                                     command=lambda: switch_to_calculator(window, parent, "Hosszúság"))
        self.btn_length.grid(row=2, column=0, columnspan=1)

        self.btn_mass = ttk.Button(parent, text="Terület",
                                   command=lambda: switch_to_calculator(window, parent, "Terület"))
        self.btn_mass.grid(row=2, column=1, columnspan=1)

        self.btn_area = ttk.Button(parent, text="Súly",
                                   command=lambda: switch_to_calculator(window, parent, "Súly"))
        self.btn_area.grid(row=2, column=2, columnspan=1)

        self.btn_dimensionless = ttk.Button(parent, text="Darabmérték",
                                            command=lambda: switch_to_calculator(window, parent, "Darabmérték"))
        self.btn_dimensionless.grid(row=3, column=0, columnspan=1)

        self.btn_volume = ttk.Button(parent, text="Szárazmérték",
                                     command=lambda: switch_to_calculator(window, parent, "Szárazmérték"))
        self.btn_volume.grid(row=3, column=1, columnspan=1)

        self.btn_capacity = ttk.Button(parent, text="Folyadékmérték",
                                       command=lambda: switch_to_calculator(window, parent, "Folyadékmérték"))
        self.btn_capacity.grid(row=3, column=2, columnspan=1)

        self.btn_exit = ttk.Button(parent, text="Kilépés", command=window.destroy)
        self.btn_exit.grid(row=4, column=0, columnspan=3)

        # Version number widget
        self.lbl_version = ttk.Label(parent, text="v0.0.1 - Alpha", font=("Helvetica", 14))
        self.lbl_version.grid(row=5, column=0, columnspan=3)


class CalculatorPage(ttk.Frame):
    def __init__(self, window, parent, unit_cat):
        """Calculator widget structure to be placed into a container (frame)."""
        super().__init__(parent)

        # Populate active unit list with function.
        set_act_lists(unit_cat)

        # Grid weight setup (7 rows, 3 columns)
        parent.grid_rowconfigure(0, weight=2)
        parent.grid_rowconfigure(1, weight=0)
        parent.grid_rowconfigure(2, weight=0)
        parent.grid_rowconfigure(3, weight=0)
        parent.grid_rowconfigure(4, weight=1)
        parent.grid_rowconfigure(5, weight=1)
        parent.grid_rowconfigure(6, weight=2)
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_columnconfigure(1, weight=1)
        parent.grid_columnconfigure(2, weight=1)

        # Lists for menu functionality
        self.input_name_list = []
        self.output_name_list = []

        # Tkinter DoubleVars and StringVar
        self.input_value = tk.DoubleVar(parent, 0)
        self.result_value = tk.DoubleVar(parent, 0)
        self.input_sys = tk.StringVar(parent, "n/a")
        self.output_sys = tk.StringVar(parent, "n/a")
        self.input_unit = tk.StringVar(parent, "n/a")
        self.output_unit = tk.StringVar(parent, "n/a")
        self.input_info = tk.StringVar(parent, "-")
        self.output_info = tk.StringVar(parent, "-")
        self.displayed_unit_symbol = tk.StringVar(parent, "n/a")

        # Storing active unit category to variable
        self.act_cat = unit_cat

        # Unit symbol variables
        self.output_symbol = "n/a"
        self.input_symbol = "n/a"

        # Variables for calculation
        self.input_inter = 0.0
        self.output_inter = 0.0

        """CALCULATOR WIDGETS"""

        # Row 0 (Title)
        self.lbl_title = ttk.Label(parent, text=unit_cat, font=("Helvetica", 40))
        self.lbl_title.grid(row=0, column=1)

        # Row 1 (Input and output labels)
        self.lbl_input = ttk.Label(parent, text="Bemenet:")
        self.lbl_input.grid(row=1, column=1)

        self.lbl_output = ttk.Label(parent, text="Kimenet:")
        self.lbl_output.grid(row=1, column=2)

        # Row 2 (Unit system selection)
        self.lbl_unit_sys = ttk.Label(parent, text="Mértékegységrendszer:")
        self.lbl_unit_sys.grid(row=2, column=0)

        self.mnu_input_sys = ttk.OptionMenu(parent, self.input_sys, "Kérem válasszon",
                                            *Unit.act_sys_list, command=self.set_input_list)
        menu_color_config(self.mnu_input_sys)
        self.mnu_input_sys.grid(row=2, column=1)

        self.mnu_output_sys = ttk.OptionMenu(parent, self.output_sys, "Kérem válasszon",
                                             *Unit.act_sys_list, command=self.set_output_list)
        menu_color_config(self.mnu_output_sys)
        self.mnu_output_sys.grid(row=2, column=2)

        # Row 3 (Input and output unit selection)
        self.lbl_unit = ttk.Label(parent, text="Mértékegységek:")
        self.lbl_unit.grid(row=3, column=0)

        self.mnu_input = ttk.OptionMenu(parent, self.input_unit, "Kérem válasszon",
                                        *self.input_name_list, command=self.set_input_int)
        menu_color_config(self.mnu_input)
        self.mnu_input.state(["disabled"])
        self.mnu_input.grid(row=3, column=1)

        self.mnu_output = ttk.OptionMenu(parent, self.output_unit, "Kérem válasszon",
                                         *self.output_name_list, command=self.set_output_int)
        menu_color_config(self.mnu_output)
        self.mnu_output.state(["disabled"])
        self.mnu_output.grid(row=3, column=2)

        # Row 4 (Entry field, unit info widgets)

        # Container for entry label and field.
        self.lbl_value_cont = ttk.Label(parent)
        self.lbl_value_cont.grid(row=4, column=0)

        self.lbl_value = ttk.Label(self.lbl_value_cont, text="Érték:")
        self.lbl_value.pack()

        val_ent_value = (self.register(self.validate), '%P')
        self.ent_value = ttk.Entry(self.lbl_value_cont, textvariable=self.input_value, font=("Helvetica", 14),
                                   validate="all", validatecommand=val_ent_value)
        self.ent_value.pack()
        self.ent_value.bind("<1>", self.click_delete)

        # Container for info widgets.
        self.lbf_info = ttk.LabelFrame(parent, text="Rövid információ:", labelanchor="n")
        self.lbf_info.grid(row=4, column=1, columnspan=2)

        self.lbf_info.grid_rowconfigure(0, weight=1, minsize=100)
        self.lbf_info.grid_columnconfigure(0, weight=1, minsize=250)
        self.lbf_info.grid_columnconfigure(1, weight=1)
        self.lbf_info.grid_columnconfigure(2, weight=1, minsize=250)  # Internal grid of self.lbf_info.

        self.lbl_input_info = ttk.Label(self.lbf_info, textvariable=self.input_info, font=("Helvetica", 12, "italic"))
        self.lbl_input_info.grid(row=0, column=0)

        self.sep_info = ttk.Separator(self.lbf_info, orient="vertical")
        self.sep_info.grid(row=0, column=1, sticky="ns")

        self.lbl_output_info = ttk.Label(self.lbf_info, textvariable=self.output_info, font=("Helvetica", 12, "italic"))
        self.lbl_output_info.grid(row=0, column=2)

        # Row 5 (Convert buttons and result)
        self.btn_convert = ttk.Button(parent, text="Váltás", command=self.calculate_button)
        self.btn_convert.grid(row=5, column=0)

        # Container for result label and field.
        self.lbl_result_cont = ttk.Label(parent)
        self.lbl_result_cont.grid(row=5, column=1)

        self.lbl_result = ttk.Label(self.lbl_result_cont, text="Eredmény:")
        self.lbl_result.pack()

        self.ent_result = ttk.Entry(self.lbl_result_cont, textvariable=self.result_value, justify="center",
                                    font=("Helvetica", 14), state="disabled")
        self.ent_result.pack()

        self.lbl_unit_symbol = ttk.Label(self.lbl_result_cont, textvariable=self.displayed_unit_symbol)
        self.lbl_unit_symbol.pack()

        self.btn_swap = ttk.Button(parent, text="↑↓", style="TButton", command=self.swap_button, state="disabled")
        self.btn_swap.grid(row=5, column=2)

        # Row 6 (Back, Reset, Exit buttons)
        self.btn_return = ttk.Button(parent, text="Vissza", style="S.TButton",
                                     command=lambda: back_to_menu(window, parent))
        self.btn_return.grid(row=6, column=0)

        self.btn_reset = ttk.Button(parent, text="Reset", style="S.TButton",
                                    command=lambda: switch_to_calculator(window, parent, unit_cat))
        self.btn_reset.grid(row=6, column=1)

        self.btn_exit = ttk.Button(parent, text="Kilépés", style="S.TButton", command=window.destroy)
        self.btn_exit.grid(row=6, column=2)

        # Special GUI modifications for dimensionless units.
        if unit_cat == "Darab":
            self.dimensionless_changes()

    """ CalculatorPage CLASS METHODS """

    def validate(self, value):
        """Entry validation (allow only empty field or float)."""
        if value == "":
            return True
        try:
            float(value)
            return True
        except ValueError:
            self.bell()
            return False

    def click_delete(self, event):
        """Delete value when clicking in entry field."""
        self.ent_value.delete(0, "end")
        return event

    def set_input_list(self, selection):
        """Method to pass correct 'side' argument ('input') to set_unit_lists function.
           Needed because of Ttk.OptionMenu's strange behavior."""
        set_unit_lists(selection, "input", self)
        return

    def set_output_list(self, selection):
        """Method to pass correct 'side' argument ('output') to set_unit_lists function.
           Needed because of Ttk.OptionMenu's strange behavior."""
        set_unit_lists(selection, "output", self)
        return

    def set_input_int(self, selection):
        """Method for input unit variable setup."""
        for i in Unit.act_unit_list:
            if i.name == selection:
                # Intermediary value set.
                self.input_inter = i.inter_val
                # Symbol stored into variable.
                self.input_symbol = i.symbol
                # Info widget updated.
                self.input_info.set(i.info)
                return self.input_inter

    def set_output_int(self, selection):
        """Method for output unit variable setup."""
        for i in Unit.act_unit_list:
            if i.name == selection:
                # Intermediary value set.
                self.output_inter = i.inter_val
                # Symbol stored into variable.
                self.output_symbol = i.symbol
                # Info widget updated.
                self.output_info.set(i.info)
                return self.output_inter

    def dimensionless_changes(self):
        """Changes for dimensionless units: output system select disabled."""
        self.mnu_output_sys.state(["disabled"])
        self.mnu_output_sys.set_menu("(inaktív)")
        return

    def swap_button(self):
        """'Swap' button functionality: swap-calculate-symbol.set-restore-disable."""
        self.input_inter, self.output_inter = self.output_inter, self.input_inter
        calculate(self)
        self.displayed_unit_symbol.set(self.input_symbol)
        self.input_inter, self.output_inter = self.output_inter, self.input_inter
        self.btn_swap.config(state="disabled")
        return

    def calculate_button(self):
        """'Calculate' button functionality: calculate-symbol.set-enable swap button."""
        calculate(self)
        self.displayed_unit_symbol.set(self.output_symbol)
        self.btn_swap.config(state="!disabled")
        return


###########################
# GUI switching functions #
###########################

def launch_main():
    """Launch app (main window, container, and menu)."""
    wdw_main = Window("Unit Converter - Mértékegységváltó", "1280x720",
                      True, True, "grey")
    frm_menu = Container(wdw_main, 1280, 720, "#E4E7EB", "#1F2933", "#151C23",
                         "both", True)
    main_menu = Menu(wdw_main, frm_menu.cont)
    wdw_main.mainloop()
    return wdw_main, frm_menu, main_menu


def switch_to_calculator(window, parent, unit_cat):
    """Calculator GUI frame launching function."""
    parent.destroy()
    frm_gui = Container(window, 1280, 720, "#E4E7EB", "#1F2933", "#151C23",
                        "both", True)
    gui_calculator = CalculatorPage(window, frm_gui.cont, unit_cat)
    return frm_gui, gui_calculator


def back_to_menu(window, parent):
    """Return to main menu frame function."""
    parent.destroy()
    frm_menu = Container(window, 1280, 720, "#E4E7EB", "#1F2933", "#151C23",
                         "both", True)
    main_menu = Menu(window, frm_menu.cont)
    return frm_menu, main_menu
