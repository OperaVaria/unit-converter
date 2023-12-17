"""
unit_list_area.py

Part of the "Unit Converter for Historical Studies" project by OperaVaria.

List of units for area measurement, in Unit class object form, nested in a function.
Used by set_act_lists function to populate lists.

TODO: add more units.
"""

# Unit class import:
from units.unit_class import Unit


def populate_area():

    # Sets the unit system list for area unit category
    Unit.act_sys_list = ["metrikus", "angolszász",
                         "attikai", "római",
                         "osztrák/bécsi",
                         "magyar királyi", "(osztrák–)magyar", "katasztrális",
                         "bányamérték (középkor)", "bányamérték (kora újkor)", "bányamérték (18. sz. köz.–)"]

    #############################################
    # Units of area, intermediary: square metre #
    #############################################

    # Metric
    Unit("négyzetmilliméter", "SI mértékegység\n10⁻⁶m²", "mm²",
         "SI", "area", 1E-6)
    Unit("négyzetcentiméter", "SI mértékegység\n10⁻⁴m²", "cm²",
         "SI", "area", 1E-4)
    Unit("négyzetdeciméter", "SI mértékegység\n10⁻²m²", "dm²",
         "SI", "area", 1E-2)
    Unit("négyzetméter", "A terület\nSI-alapegysége", "m²",
         "SI", "area", 1)
    Unit("ár", "történelmi metrikus\nmértékegység\n10²m²", "ar",
         "historical metric", "area", 1E2)
    Unit("hektár", "Engedélyezett\nnem SI-mértékegység\n10⁴m²", "ha",
         "accepted non-SI", "area", 1E4)
    Unit("négyzetkilométer", "SI mértékegység\n10⁶m²", "km²",
         "SI", "area", 1E6)
    # Based on SI 2009.

    # Imperial and US customary
    Unit("square inch", "ang. négyzethüvelyk\n1/1296 sq yd", "sq in",
         "Imperial", "area", 6.4516E-04)
    Unit("square foot", "ang. négyzetláb\n144 sq in", "sq ft",
         "Imperial", "area", 0.09290304)
    Unit("square yard", "ang. négyzetyard\n9 sq ft", "sq yd",
         "Imperial", "area", 0.83612736)
    Unit("square rod", "ang. négyzetrúd\naka sq perch v. pole\n121.25 sq yd", "sq rd",
         "Imperial", "area", 25.29285264)  # Cardarelli 2003, 602.
    Unit("rood", "ang. kereszt\n1/4 acre", "ro",
         "Imperial", "area", 1011.7141056)
    Unit("international acre", "brit un. \"nemzetközi\" hold\n4840 sq yd", "ac (UK)",
         "Imperial", "area", 4046.8564224)
    Unit("US survey acre", "am. (földmérő) hold\n4840 (régi) sq yd", "ac (US)",
         "US customary", "area", 4046.873)  # Butcher et al. 2006, 9.
    Unit("square mile", "ang. négyzetmérföld\n640 ac", "sq mi",
         "Imperial", "area", 2589988.1103366)
    # Based on 1995 No. 1804 unless otherwise indicated.

    # Attic
    Unit("πούς (pus)", "att. négyzetláb\n 1/10.000 plt", "pt",
         "Attic", "area", 0.095)
    Unit("ἑξαπόδης (hexapodés)", "jel. \"hatlábnyi\"\n36 pt", "hxp.",
         "Attic", "area", 3.42)
    Unit("ἄκαινα (akaina)", "attikai négyzetrúd\n100 pt", "akt",
         "Attic", "area", 9.5)
    Unit("ἕκτος (hektos)", "jel. \"hatod\"\n1/6 plt", "hek.",
         "Attic", "area", 158.415)
    Unit("ἄρουρα (arura)", "jel. \"szántóföld\"\n1/4 plt", "aru.",
         "Attic", "area", 237.6225)
    Unit("πλέθρον (plethron)", "att. hold\n100 akt", "plt",
         "Attic", "area", 950.49)
    # Based on Egger, Jochen, and Smart 2010, 460, with additional information from Vilmos 1984.

    # Roman
    Unit("pes quadratus", "róm. négyzetláb\n1/14400 aq", "pq",
         "Roman", "area", 0.09)
    Unit("dimidium scripulum", "1/2 scr.\n1/576 iug.", "dscr.",
         "Roman", "area", 4.38)
    Unit("scripulum", "aka decempeda quadrata\n100 pq", "scr.",
         "Roman", "area", 8.76)
    Unit("uncia", "a iugerum unciája\nazaz 1/12 iug.", "un.",
         "Roman", "area", 210.28)
    Unit("clima", "gör. klima szóból\n60*60 pedes méretű terület\n36 scr.", "clim.",
         "Roman", "area", 315.42)
    Unit("actus quadratus", "actus (120 pedes)\noldalú négyzet\n4 clim.", "aq",
         "Roman", "area", 1261.67)
    Unit("iugerum", "római hold\n2 aq", "iug.",
         "Roman", "area", 2523.34)
    Unit("heredium", "jel. \"öröklött telek\"\n2 iug.", "her.",
         "Roman", "area", 5046.68)
    Unit("centuria", "100 her.", "cent.",
         "Roman", "area", 504700)
    Unit("saltus", "jel. \"legelő\"\n4 cent.", "sal.",
         "Roman", "area", 201.87E4)
    # Based on Egger, Jochen, and Smart 2010, 461, with additional information from Vilmos 1984.

    # Austrian/Viennese
    Unit("Wiener Quadratlinie", "bécsi négyszögvonal", "QLin.",
         "Viennese", "area", 4.8179861E-6)
    Unit("Wiener Quadratzoll", "bécsi négyszöghüvelyk\n144 QLin.", "QZoll",
         "Viennese", "area", 6.9379E-4)
    Unit("Wiener Quadratfuß", "bécsi négyszögláb\n144 QZoll", "QFuß",
         "Viennese", "area", 999.07E-4)
    Unit("Wiener Quadratklafter", "bécsi négyszögöl\n36 QFuß", "QKlaf.",
         "Viennese", "area", 3.59665)
    Unit("Niederösterreiches Joch", "alsó-ausztriai hold\neredetileg 1584 QKlaft.\n1786-tól kerekítés: 1600", "Joch",
         "Viennese", "area", 5754.64)
    Unit("Österreichische Quadratmeile", "osztrák négyszögmérföld\n100 Joch", "QMei.",
         "Viennese", "area", 575464)
    # Based on Bogdán 1990, 37.

    # Hungarian Royal
    Unit("királyi négyszögláb", "lat. pes quadratus\n1/864 hold", "nláb",
         "Hungarian Royal", "area", 0.0977)
    Unit("királyi négyszögöl", "lat. orgia quadrata\n100 nláb", "nöl",
         "Hungarian Royal", "area", 9.772)
    Unit("királyi hold", "lat. iugerum\n12*72 öl", "hold",
         "Hungarian Royal", "area", 8440)
    Unit("királyi ekealja", "lat. aratrum\n150 hold", "ekal.",
         "Hungarian Royal", "area", 126.63E4)
    # Based on Bogdán 1978, 35–36, and Bogdán 1990, 36.

    # (Austro-)Hungarian
    Unit("bécsi négyszöghüvelyk", "az osztrák\nrendszerből", "nhüv.",
         "(Austro-)Hungarian", "area", 6.9379E-4)
    Unit("bécsi négyszögláb", "az osztrák\nrendszerből\n144 nhüvelyk", "nláb",
         "(Austro-)Hungarian", "area", 999.07E-4)
    Unit("bécsi négyszögöl", "az osztrák\nrendszerből\n36 nláb", "nöl",
         "(Austro-)Hungarian", "area", 3.59665)
    Unit("magyar hold", "a magyar rendszerből\na bécsi nölhőz igazítva\n(1200)", "hold",
         "(Austro-)Hungarian", "area", 4316)
    Unit("magyar négyszögmérföld", "utólagos,\nnem illeszkedik:\n161 2/5 hold", "nmérf.",
         "(Austro-)Hungarian", "area", 697800)
    # Based on Bogdán 1990, 37.

    # Cadastral
    Unit("katasztrális négyszögöl", "a bécsi nöl\nadoptálása", "kat. nöl",
         "Cadastral", "area", 3.59665)
    Unit("katasztrális hold", "az alsó-ausztriai\nhold adoptálása\n1600 kat. nöl", "kat. hold",
         "Cadastral", "area", 5754.642)
    # Based on Bogdán 1990, 36.

    # Selmecbánya (Medieval)
    # Name collision avoided with invisible character U+1D173 at the end of self.name.
    Unit("bányakötél𝅳", "selmeci\nbánya(négyszög)kötél\n7*7 öl", "nköt.",
         "Selmec (Medieval)", "area", 200.08)
    Unit("bányatelek𝅳", "selmeci bányatelek\n7*14 öl", "tel.",
         "Selmec (Medieval)", "area", 400.44)
    Unit("két bányatelek𝅳", "két selmeci\nbányatelek\n7*28 öl", "2tel.",
         "Selmec (Medieval)", "area", 800.91)
    Unit("három bányatelek𝅳", "három selmeci\nbányatelek\n7*42 öl", "3tel.",
         "Selmec (Medieval)", "area", 1201.34)
    Unit("három \"régi\" bányatelek𝅳", "három selmeci\nbányatelek (régi, 3 1/2-es)\n7*49 öl", "3tel.",
         "Selmec (Medieval)", "area", 1401.56)
    # Bogdán 1978, 39.

    # Selmecbánya (Early Modern)
    # Name collision avoided with invisible character U+1D174 at the end of self.name.
    Unit("bánya-négyszögláb𝅴", "selmeci\nbánya-négyszögláb\n(1*1 bányaláb)", "nláb",
         "Selmec (Early Modern)", "area", 0.1134)
    Unit("bánya-négyszögöl𝅴", "selmeci\nbánya-négyszögöl\n36 nláb", "nöl",
         "Selmec (Early Modern)", "area", 4.0864)
    Unit("bánya-négyszögkötél𝅴", "selmeci\nbánya-négyszögkötél\n7*7 öl", "nköt.",
         "Selmec (Early Modern)", "area", 200.08)
    Unit("bányatelek𝅴", "selmeci bányatelek\n7*14 öl", "tel.",
         "Selmec (Early Modern)", "area", 400.44)
    Unit("két bányatelek𝅴", "két selmeci\nbányatelek\n7*28 öl", "2tel.",
         "Selmec (Early Modern)", "area", 800.91)
    Unit("három bányatelek𝅴", "három selmeci\nbányatelek\n7*42 öl", "3tel.",
         "Selmec (Early Modern)", "area", 1201.34)
    # Bogdán 1990, 47.

    # Mining units (mid 18th century-)
    Unit("aknatelek", "aknatelek 1753-tól\n84*112 öl\n96 régi tel.", "atel.",
         "Selmec (mid18th c.-)", "area", 38400)
    Unit("\"kis\" tárnatelek", "tárnatelek 1792-től\n56*224 öl\n128 régi tel.", "ttel.",
         "Selmec (mid18th c.-)", "area", 51200)
    Unit("\"nagy\" tárnatelek", "tárnatelek 1753-tól\n112*224 öl\n256 régi tel.", "ttel.",
         "Selmec (mid18th c.-)", "area", 102500)
    # Bogdán 1990, 47.
    return
