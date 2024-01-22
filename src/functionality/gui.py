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
from functionality.functions import (set_act_objs, set_sys_name_list,
                                     set_input_menu, set_output_menu,
                                     set_input_sys_info, set_output_sys_info,
                                     drop_menu_config, calculate)


###########
# Classes #
###########


class Menu(ttk.Frame):
    """Unit converter main menu implemented az a Python class."""
    def __init__(self, window, parent, font):
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
                                   font=(font, 48), justify="center")
        self.lbl_title.grid(row=0, column=0, columnspan=3)

        self.lbl_subtitle = ttk.Label(parent, text="Metrikus, angolszász, hagyományos, történelmi\n",
                                      font=(font, 24))
        self.lbl_subtitle.grid(row=1, column=0, columnspan=3)

        # Buttons
        self.btn_length = ttk.Button(parent, text="Hosszúság",
                                     command=lambda: switch_to_calculator(window, parent,
                                                                          "Hosszúság"))
        self.btn_length.grid(row=2, column=0, columnspan=1)

        self.btn_mass = ttk.Button(parent, text="Terület",
                                   command=lambda: switch_to_calculator(window, parent,
                                                                        "Terület"))
        self.btn_mass.grid(row=2, column=1, columnspan=1)

        self.btn_area = ttk.Button(parent, text="Súly",
                                   command=lambda: switch_to_calculator(window, parent,
                                                                        "Súly"))
        self.btn_area.grid(row=2, column=2, columnspan=1)

        self.btn_dimensionless = ttk.Button(parent, text="Darabmérték",
                                            command=lambda: switch_to_calculator(window, parent,
                                                                                 "Darabmérték"))
        self.btn_dimensionless.grid(row=3, column=0, columnspan=1)

        self.btn_volume = ttk.Button(parent, text="Szárazmérték",
                                     command=lambda: switch_to_calculator(window, parent,
                                                                          "Szárazmérték"))
        self.btn_volume.grid(row=3, column=1, columnspan=1)

        self.btn_capacity = ttk.Button(parent, text="Folyadékmérték",
                                       command=lambda: switch_to_calculator(window, parent,
                                                                            "Folyadékmérték"))
        self.btn_capacity.grid(row=3, column=2, columnspan=1)

        self.btn_exit = ttk.Button(parent, text="Kilépés", command=window.destroy)
        self.btn_exit.grid(row=4, column=0, columnspan=3)

        # Version number widget
        self.lbl_version = ttk.Label(parent, text="v0.1.1 - Alpha", font=(font, 18))
        self.lbl_version.grid(row=5, column=0, columnspan=3)


class CalculatorPage(ttk.Frame):
    """Calculator GUI implemented as a Python class.
    Dynamically set up based upon unit category selection."""
    def __init__(self, window, parent, unit_cat, font):
        """Calculator widget structure to be placed into a container (frame)."""
        super().__init__(parent)

        # Grid weight setup (7 rows, 3 columns).
        parent.grid_rowconfigure(0, weight=2)
        parent.grid_rowconfigure(1, weight=0)
        parent.grid_rowconfigure(2, weight=0)
        parent.grid_rowconfigure(3, weight=0)
        parent.grid_rowconfigure(4, weight=2)
        parent.grid_rowconfigure(5, weight=1)
        parent.grid_rowconfigure(6, weight=2)
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_columnconfigure(1, weight=1)
        parent.grid_columnconfigure(2, weight=1)

        # Lists for menu functionality.
        self.sys_name_list = []
        self.input_name_list = []
        self.output_name_list = []

        # Tkinter DoubleVars and StringVars.
        self.input_value = tk.DoubleVar(parent, 0)
        self.result_value = tk.DoubleVar(parent, 0)
        self.input_sys = tk.StringVar(parent, "n/a")
        self.output_sys = tk.StringVar(parent, "n/a")
        self.input_unit = tk.StringVar(parent, "n/a")
        self.output_unit = tk.StringVar(parent, "n/a")
        self.input_sys_info = tk.StringVar(parent, "–––")
        self.output_sys_info = tk.StringVar(parent, "–––")
        self.input_unit_info = tk.StringVar(parent, "–––")
        self.output_unit_info = tk.StringVar(parent, "–––")
        self.displ_unit_symb = tk.StringVar(parent, "n/a")

        # Storing active unit category to variable.
        self.act_cat = unit_cat

        # Unit symbol variables.
        self.output_symbol = "n/a"
        self.input_symbol = "n/a"

        # Variables for calculation.
        self.input_inter = "n/a"
        self.output_inter = "n/a"

        # Initial backend setup.
        self.init_setup()

        """CALCULATOR WIDGETS"""

        # Row 0 (Title)
        self.lbl_title = ttk.Label(parent, text=unit_cat, font=(font, 48))
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
                                            *self.sys_name_list, command=self.set_input_select)
        drop_menu_config(self.mnu_input_sys)
        self.mnu_input_sys.grid(row=2, column=1)

        self.mnu_output_sys = ttk.OptionMenu(parent, self.output_sys, "Kérem válasszon",
                                             *self.sys_name_list, command=self.set_output_select)
        drop_menu_config(self.mnu_output_sys)
        self.mnu_output_sys.grid(row=2, column=2)

        # Row 3 (Input and output unit selection)
        self.lbl_unit = ttk.Label(parent, text="Mértékegységek:")
        self.lbl_unit.grid(row=3, column=0)

        self.mnu_input = ttk.OptionMenu(parent, self.input_unit, "Kérem válasszon",
                                        *self.input_name_list, command=self.set_input_vars)
        drop_menu_config(self.mnu_input)
        self.mnu_input.state(["disabled"])
        self.mnu_input.grid(row=3, column=1)

        self.mnu_output = ttk.OptionMenu(parent, self.output_unit, "Kérem válasszon",
                                         *self.output_name_list, command=self.set_output_vars)
        drop_menu_config(self.mnu_output)
        self.mnu_output.state(["disabled"])
        self.mnu_output.grid(row=3, column=2)

        # Row 4 (Entry field and unit info widgets)

        # Container for entry label and field.
        self.lbl_value_cont = ttk.Label(parent)
        self.lbl_value_cont.grid(row=4, column=0)
        self.lbl_value = ttk.Label(self.lbl_value_cont, text="Érték:")
        self.lbl_value.pack()

        val_ent_value = (self.register(self.validate), '%P')
        self.ent_value = ttk.Entry(self.lbl_value_cont, font=(font, 16), width=30,
                                   textvariable=self.input_value,
                                   validate="all", validatecommand=val_ent_value)
        self.ent_value.pack()
        self.ent_value.bind("<1>", self.click_delete)  # Left click clears field.

        # Container for info widgets.
        self.lbf_info = ttk.LabelFrame(parent, text="Rövid információ", labelanchor="n")
        # Internal grid of self.lbf_info.
        self.lbf_info.grid(row=4, column=1, columnspan=2)
        self.lbf_info.grid_rowconfigure(0, weight=1, minsize=150)
        self.lbf_info.grid_rowconfigure(1, weight=1)
        self.lbf_info.grid_rowconfigure(2, weight=1, minsize=150)
        self.lbf_info.grid_columnconfigure(0, weight=1, minsize=450)
        self.lbf_info.grid_columnconfigure(1, weight=1)
        self.lbf_info.grid_columnconfigure(2, weight=1, minsize=450)
        # Separators.
        self.sep_info_vert = ttk.Separator(self.lbf_info, orient="vertical")
        self.sep_info_vert.grid(row=0, column=1, rowspan=3, sticky="ns")

        self.sep_info_hor = ttk.Separator(self.lbf_info, orient="horizontal")
        self.sep_info_hor.grid(row=1, column=0, columnspan=3, sticky="we")
        # Labels.
        self.lbl_input_sys_info = ttk.Label(self.lbf_info, textvariable=self.input_sys_info,
                                            style="LF.TLabel", justify="center", wraplength=400)
        self.lbl_input_sys_info.grid(row=0, column=0)

        self.lbl_output_sys_info = ttk.Label(self.lbf_info, textvariable=self.output_sys_info,
                                             style="LF.TLabel", justify="center", wraplength=400)
        self.lbl_output_sys_info.grid(row=0, column=2)

        self.lbl_input_unit_info = ttk.Label(self.lbf_info, textvariable=self.input_unit_info,
                                             style="LF.TLabel", justify="center", wraplength=400)
        self.lbl_input_unit_info.grid(row=2, column=0)

        self.lbl_output_unit_info = ttk.Label(self.lbf_info, textvariable=self.output_unit_info,
                                              style="LF.TLabel", justify="center", wraplength=400)
        self.lbl_output_unit_info.grid(row=2, column=2)

        # Row 5 (Convert buttons and result)
        self.btn_convert = ttk.Button(parent, text="Váltás", command=self.calculate_button)
        self.btn_convert.grid(row=5, column=0)

        # Container for result label and field.
        self.lbl_result_cont = ttk.Label(parent)
        self.lbl_result_cont.grid(row=5, column=1)

        self.lbl_result = ttk.Label(self.lbl_result_cont, text="Eredmény:")
        self.lbl_result.pack()
        self.ent_result = ttk.Entry(self.lbl_result_cont, font=(font, 16, "bold"),
                                    justify="center", width=30,
                                    textvariable=self.result_value, state="readonly")
        self.ent_result.pack()

        self.lbl_unit_symbol = ttk.Label(self.lbl_result_cont, textvariable=self.displ_unit_symb)
        self.lbl_unit_symbol.pack()

        self.btn_swap = ttk.Button(parent, text="↑↓", command=self.swap_button, state="disabled")
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
        if unit_cat == "Darabmérték":
            self.dimensionless_changes()

    """ CalculatorPage CLASS METHODS """

    def init_setup(self):
        """Functions to be called when initiating a CalculatorPage instance."""
        set_act_objs(self)
        set_sys_name_list(self)
        return

    def dimensionless_changes(self):
        """Changes for dimensionless units: output system select disabled, set ditto marks."""
        self.mnu_output_sys.state(["disabled"])
        self.mnu_output_sys.set_menu("''")
        self.output_sys_info.set("''")
        return

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

    def set_input_select(self, selection):
        """Method to pass correct parameters/arguments to input setup functions.
           Needed because of ttk.OptionMenu's strange behavior."""
        set_input_menu(selection, self)
        set_input_sys_info(selection, self)
        return

    def set_output_select(self, selection):
        """Method to pass correct parameters/arguments to output setup functions.
           Needed because of ttk.OptionMenu's strange behavior."""
        set_output_menu(selection, self)
        set_output_sys_info(selection, self)
        return

    def set_input_vars(self, selection):
        """Method for input unit variable setup."""
        for i in Unit.act_obj_list:
            if i.name == selection:
                # Intermediary value set.
                self.input_inter = i.inter_val
                # Symbol stored into variable.
                self.input_symbol = i.symbol
                # Info box updated.
                self.input_unit_info.set(i.info)
        return self.input_inter

    def set_output_vars(self, selection):
        """Method for output unit variable setup."""
        for i in Unit.act_obj_list:
            if i.name == selection:
                # Intermediary value set.
                self.output_inter = i.inter_val
                # Symbol stored into variable.
                self.output_symbol = i.symbol
                # Info box updated.
                self.output_unit_info.set(i.info)
        return self.output_inter

    def swap_button(self):
        """'Swap' button functionality: swap-calculate-symbol.set-restore-disable."""
        self.input_inter, self.output_inter = self.output_inter, self.input_inter
        calculate(self)
        self.displ_unit_symb.set(self.input_symbol)
        self.input_inter, self.output_inter = self.output_inter, self.input_inter
        self.btn_swap.config(state="disabled")
        return self.displ_unit_symb

    def calculate_button(self):
        """'Calculate' button functionality: calculate-symbol.set-enable swap button."""
        calculate(self)
        self.displ_unit_symb.set(self.output_symbol)
        self.btn_swap.config(state="!disabled")
        return self.displ_unit_symb


###########################
# GUI switching functions #
###########################

def launch_main():
    """Launch app (main window, container, and menu)."""
    wdw_main = Window("Unit Converter - Mértékegységváltó", "1920x1080", True, True,
                      "#1F2933", True)
    frm_menu = Container(wdw_main, 1920, 1080, "both", True, "#1F2933",
                         "#E4E7EB", "#151C23", "Helvetica")
    main_menu = Menu(wdw_main, frm_menu.cont, "Helvetica")
    wdw_main.mainloop()
    return wdw_main, frm_menu, main_menu


def switch_to_calculator(window, parent, unit_cat):
    """Calculator GUI page launching function."""
    parent.destroy()
    frm_gui = Container(window, 1920, 1080, "both", True, "#1F2933",
                        "#E4E7EB", "#151C23", "Helvetica")
    gui_calculator = CalculatorPage(window, frm_gui.cont, unit_cat, "Helvetica")
    return frm_gui, gui_calculator


def back_to_menu(window, parent):
    """Return to main menu frame function."""
    parent.destroy()
    frm_menu = Container(window, 1920, 1080, "both", True, "#1F2933",
                         "#E4E7EB", "#151C23", "Helvetica")
    main_menu = Menu(window, frm_menu.cont, "Helvetica")
    return frm_menu, main_menu


# Display message when accidentally run:
if __name__ == "__main__":
    print("This file is a module of the \"Unit Converter for Historical Studies\" project."
          "Launch \"main.pyw\" to start the app.")
