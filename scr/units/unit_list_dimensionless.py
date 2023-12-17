"""
unit_list_dimensionless.py

Part of the "Unit Converter for Historical Studies" project by OperaVaria.

List of dimensionless units, in Unit class object form, nested in a function.
Used by set_act_lists function to populate lists.

TODO: add more units.
"""

# Unit class import:
from units.unit_class import Unit


def populate_dimensionless():

    # Sets the unit system list for dimensionless unit category
    Unit.act_sys_list = ["írópapír", "nyomópapír", "általános (magyarországi)"]

    #############################################
    # Dimensionless units, intermediary: varies #
    #############################################

    # Writing paper
    Unit("írólap ív", "lat. arcus\nném. Bogen\n1 db papírlap", "ív",
         "writing paper", "dimensionless", 1)
    Unit("írólap konc", "lat. liber\nném. Buch\n24 ív", "konc",
         "writing paper", "dimensionless", 24)
    Unit("írólap rizsma", "lat. ligatura\nném. Ries\n20 konc, 480 ív", "rizsma",
         "Hungary (writing paper)", "dimensionless", 480)
    Unit("írólap bála", "lat. bala\nném. Ballen\n10 rizsma, 4800 ív", "bála",
         "writing paper", "dimensionless", 10)
    # Based on  Bogdán, 1991, 53.

    # Printing paper
    Unit("nyomdai ív", "lat. arcus\nném. Bogen\n1 db papírlap", "ív",
         "printing paper", "dimensionless", 1)
    Unit("nyomdai konc", "lat. liber\nném. Buch\n25 ív", "konc",
         "printing paper", "dimensionless", 25)
    Unit("nyomdai rizsma", "lat. ligatura\nném. Ries\n20 konc, 500 ív", "rizsma",
         "printing paper", "dimensionless", 500)
    Unit("nyomdai bála", "lat. bala\nném. Ballen\n10 bála, 5000 ív", "bála",
         "printing paper", "dimensionless", 5000)
    # Based on Bogdán, 1991, 53.

    # General (Hungary)
    Unit("darab", "lat. numerus\nném. Stück\negy egységnyi", "db",
         "General (Hungary)", "dimensionless", 1)
    Unit("pár", "ném. Paarból\naz a lat. parból\nkét db", "pár",
         "General (Hungary)", "dimensionless", 2)
    Unit("deher", "ném. Decherből\nlat. decuria\nált. prém, 10 db", "deh.",
         "General (Hungary)", "dimensionless", 10)
    Unit("tucat", "ném. Dutzendből\naz a lat. duodecimből\n12 db", "tuc.",
         "General (Hungary)", "dimensionless", 12)
    Unit("mandel", "ném. eredetű szó\n15 db", "man.",
         "General (Hungary)", "dimensionless", 15)
    Unit("stiga", "ném. eredetű szó\n20 db", "sti.",
         "General (Hungary)", "dimensionless", 20)
    Unit("cimmer", "ném. Zimmerből\nlat. timbrium\nált. prém, 4 deher", "cimm.",
         "General (Hungary)", "dimensionless", 40)
    Unit("sokk", "ném. eredetű szó\n4 mandel, 60 db", "sokk",
         "General (Hungary)", "dimensionless", 60)
    Unit("kis százas", "ném. Hundertből\n5 stiga, 100 db", "k. száz.",
         "General (Hungary)", "dimensionless", 100)
    Unit("nagy százas", "ném. Hundertből\n6 stiga, 120 db", "n. száz.",
         "General (Hungary)", "dimensionless", 120)
    Unit("nagy", "ném. Grossból\n12 tucat, 144 db", "nagy",
         "General (Hungary)", "dimensionless", 144)
    Unit("kis ezres", "ném. Tausendből\n50 stiga, 1000 db", "k. ez.",
         "General (Hungary)", "dimensionless", 1000)
    Unit("nagy ezres", "ném. Tausendből\n60 stiga, 1200 db", "n. ez.",
         "General (Hungary)", "dimensionless", 1200)
    # Based on Bogdán, 1991, 53.
    return
