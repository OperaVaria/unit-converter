"""
unit_list_length.py

Part of the "Unit Converter for Historical Studies" project by OperaVaria.

List of units for length measurement, in Unit class object form, nested in a function.
Used by set_act_lists function to populate lists.

TODO: add more units.
"""

# Unit class import:
from units.unit_class import Unit


def populate_length():

    # Sets the unit system list for length unit category
    Unit.act_sys_list = ["metrikus", "angolszász",
                         "attikai", "római",
                         "osztrák/bécsi",
                         "magyar királyi", "pozsonyi", "erdélyi",
                         "bányamérték (középkor)", "bányamérték (kora újkor)", "bányamérték (18. sz. köz.–)"]

    ########################################
    # Units of length, intermediary: metre #
    ########################################

    # Metric
    Unit("milliméter", "SI mértékegység\n10⁻³m", "mm",
         "SI", "length", 1E-03)
    Unit("centiméter", "SI mértékegység\n10⁻²m", "cm",
         "SI", "length", 1E-02)
    Unit("deciméter", "SI mértékegység\n10⁻¹m", "dm",
         "SI", "length", 1E-01)
    Unit("méter", "A hosszúság\nSI-alapegysége", "m",
         "SI", "length", 1)
    Unit("kilométer", "SI mértékegység\n10³m", "km",
         "SI", "length", 1E03)
    # Based on SI 2009.

    # Imperial and US customary
    Unit("inch", "ang. hüvelyk\n1/32 yd", "in",
         "Imperial", "length", 0.0254)
    Unit("hand", "ang. kéz\n4 in", "h",
         "Imperial", "length", 0.1016)
    Unit("foot", "ang. láb\n12 in", "ft",
         "Imperial", "length", 0.3048)
    Unit("yard", "a yardstick hosszúsága\n3 ft", "yd",
         "Imperial", "length", 0.9144)
    Unit("fathom", "ang. öl\n6 ft", "fth",
         "Imperial", "length", 1.8288)
    Unit("rod", "ang. rúd\naka perch v. pole\n16.5 ft", "rd",
         "Imperial", "length", 5.0292)   # Cardarelli 2003, 560–561.
    Unit("chain", "ang. lánc\n22 yd", "ch",
         "Imperial", "length", 20.1168)
    Unit("furlong", "ang. stadion\n10 ch", "fur",
         "Imperial", "length", 201.168)
    Unit("mile", "ang. mérföld\n1760 yd", "mi",
         "Imperial", "length", 1609.344)
    Unit("nautical mile", "tengeri mérföld\negy szögpercnyi távolság", "nmi",
         "Imperial", "length", 1853)
    # Based on 1995 No. 1804 unless otherwise indicated.

    # Attic
    Unit("δάκτυλος (daktylos)", "att. ujj\n1/16 p.", "dak.",
         "Attic", "length", 0.01927)
    Unit("κόνδυλος (kondylos)", "jel. \"ököl\" v. \"izület\"\n2 dak.", "kon.",
         "Attic", "length", 0.03854)
    Unit("παλαιστή (palaisté)", "att. tenyér\naka δῶρον (dóron)\n4 dak.", "pal.",
         "Attic", "length", 0.07708)
    Unit("διχάς (dichas)", "1/2 p.\naka ἡμιπόδιον (hémipodion)\n8 dak.", "dich.",
         "Attic", "length", 0.15415)
    Unit("λιχάς (lichas)", "att. kisarasz\n10 dak.", "lich.",
         "Attic", "length", 0.1927)
    Unit("ὀρθόδωρον (orthodóron)", "a tenyér hosszúsága\n11 dak.", "orth.",
         "Attic", "length", 0.21197)
    Unit("σπιθαμή (spithamé)", "att. nagyarasz\n12 dak.", "spi.",
         "Attic", "length", 0.23123)
    Unit("πούς (pus)", "att. láb\n16 dak.", "p.",
         "Attic", "length", 0.3083)
    Unit("πυγμή (pygmé)", "az alkar hosszúsága\n18 dak.", "pyg.",
         "Attic", "length", 0.34686)
    Unit("πυγών (pygón)", "alkar és ököl\n20 dak.", "pyg.",
         "Attic", "length", 0.3854)
    Unit("πῆχυς (péchys)", "att. könyök\n24 dak.", "pech.",
         "Attic", "length", 0.46245)
    Unit("ἁπλοῦν βῆμα (haplun béma)", "att. lépés\n2 1/2 p.", "béma",
         "Attic", "length", 0.77075)
    Unit("διπλοῦν βῆμα (diplun béma)", "att. kettős lépés\n5 p.", "dbm",
         "Attic", "length", 1.5415)
    Unit("ὄργυια (orgyia)", "att. öl\n1/100 stadion\n6 p.", "org.",
         "Attic", "length", 1.8498)
    Unit("κάλαμος (kalamos)", "aka ἄκαινα (akaina)\nv. δεκάπους (dekapus)\n10 p.", "kal.",
         "Attic", "length", 3.083)
    Unit("πλέθρον (plethron)", "egy barázda hossza\n100 p.", "pleth.",
         "Attic", "length", 30.83)
    Unit("στάδιον (stadion)", "egy versenypálya hossza\n600 p.", "stad.",
         "Attic", "length", 184.98)
    Unit("δίαυλος (diaulos)", "dupla versenytáv\n2 stad.", "diau.",
         "Attic", "length", 369.96)
    Unit("ἱππικόν (hippikon)", "egy hippodróm hossza\n4 stad.", "hip.",
         "Attic", "length", 739.92)
    Unit("δόλιχος (dolichos)", "hosszú versenytáv\n12 stad.", "dol.",
         "Attic", "length", 2219.76)
    # Based on Egger, Jochen, and Smart 2010, 459, with additional information from Vilmos 1984.

    # Roman
    Unit("digitus", "róm. ujj\n1/16 p.", "dig.",
         "Roman", "length", 0.0185)
    Unit("uncia", "róm. hüvelyk\naka pollex\n1/12 p.", "un.",
         "Roman", "length", 0.0247)
    Unit("palmus", "róm. tenyér\n4 dig.", "pal.",
         "Roman", "length", 0.074)
    Unit("palmus maior", "róm. nagyobb tenyér\nazaz arasz\n3 pal.", "pal. mai.",
         "Roman", "length", 0.222)
    Unit("pes", "róm. láb\nalapmérték\n4 pal.", "p.",
         "Roman", "length", 0.296)
    Unit("palmipes", "jel. \"tenyér és láb\"\n5 pal.", "plp.",
         "Roman", "length", 0.370)
    Unit("cubitus", "róm. könyök\n6 pal.", "cub.",
         "Roman", "length", 0.444)
    Unit("gradius", "róm. lépés\naka grassus v. pes sestertius\n2 1/2 p., 10 pal.", "gra.",
         "Roman", "length", 0.74)
    Unit("passus", "róm. kettős lépés\n(2 gradius)\n5 p.", "pass.",
         "Roman", "length", 1.48)
    Unit("decempeda", "tíz lépés\naka pertica\n(10 p.)", "dped.",
         "Roman", "length", 2.96)
    Unit("actus", "egy barázda hossza\n12 dped.\n24 pass.", "act.",
         "Roman", "length", 35.52)
    Unit("mille passus", "róm. mérföld\n1000 pass.", "mille",
         "Roman", "length", 1480)
    # Based on Vilmos 1984, with additional information from Györkösy 2014.

    # Austrian/Viennese
    Unit("Wiener Punkt", "bécsi pont\n1/144 Zoll", "Punkt",
         "Viennese", "length", 0.1829E-3)
    Unit("Wiener Linie", "bécsi vonal\n12 Punkt", "Lin.",
         "Viennese", "length", 2.195E-3)
    Unit("Wiener Zoll", "bécsi hüvelyk\n12 Lin.", "Zoll",
         "Viennese", "length", 0.02634)
    Unit("Wiener Fuß", "bécsi láb\n12 Zoll", "Fuß",
         "Viennese", "length", 0.31608)
    Unit("Wiener Elle", "bécsi rőf\n(nem illeszkedik\na hatos számrendszerbe)", "Elle",
         "Viennese", "length", 0.77755)
    Unit("Wiener Klafter", "bécsi öl\n6 Fuß", "Klaf.",
         "Viennese", "length", 1.8964)
    Unit("Wiener Rute", "bécsi rúd\n12 Fuß", "Rute",
         "Viennese", "length", 3.793)
    Unit("Wiener Meile", "bécsi mérföld\n2400 Fuß\n4000 Klaf.", "Mei.",
         "Viennese", "length", 7585.9)
    # Based on Bogdán 1990, 35.

    # Hungarian Royal
    Unit("királyi ujj", "lat. digitus\n1/16 láb", "ujj",
         "Hungarian Royal", "length", 0.01953)
    Unit("királyi hüvelyk", "lat. pollex\n1/12 láb", "hüv.",
         "Hungarian Royal", "length", 0.02605)
    Unit("királyi tenyér", "lat. palmus\n4 ujj", "teny.",
         "Hungarian Royal", "length", 0.07815)
    Unit("királyi arasz", "lat. spithama\n10 ujj", "ar.",
         "Hungarian Royal", "length", 0.1954)
    Unit("királyi láb", "lat. pes\n4 teny.", "láb",
         "Hungarian Royal", "length", 0.3126)
    Unit("királyi rőf", "lat. cubitus v. ulna\n2 láb", "rőf",
         "Hungarian Royal", "length", 0.6252)
    Unit("királyi lépés", "lat. gressus\n3 láb", "lép.",
         "Hungarian Royal", "length", 0.9378)
    Unit("királyi kettős lépés", "lat. passus\n6 láb", "ket. lép.",
         "Hungarian Royal", "length", 1.875)
    Unit("királyi öl", "lat. orgia\n5 rőf\n10 láb", "öl",
         "Hungarian Royal", "length", 3.126)
    # Based on Bogdán 1978, 34–35, and Bogdán 1990, 34.

    # Pressburg
    Unit("pozsonyi hüvelyk", "10 1/5 láb", "hüv.",
         "Pressburg", "length", 0.0318)
    Unit("pozsonyi tenyér", "3 hüvelyk", "teny.",
         "Pressburg", "length", 0.0930)
    Unit("pozsonyi arasz", "3 tenyér", "ar.",
         "Pressburg", "length", 0.2660)
    Unit("pozsonyi láb", "10 1/5 hüvelyk\n1 1/5 arasz", "láb",
         "Pressburg", "length", 0.3168)
    Unit("pozsonyi rőf", "3 arasz", "rőf",
         "Pressburg", "length", 0.7830)
    Unit("pozsonyi öl", "a bécsivel\nmajdnem megegyező\n6 arasz", "öl",
         "Pressburg", "length", 1.901)
    # Based on Bogdán 1978, 34–35, and Bogdán 1990, 34–35.

    # Transylvanian
    Unit("erdélyi vonal", "1/144 láb", "ujj",
         "Transylvanian", "length", 0.00215)
    Unit("erdélyi hüvelyk", "12 vonal", "hüv.",
         "Transylvanian", "length", 0.02591)
    Unit("erdélyi láb", "12 hüvelyk", "láb",
         "Transylvanian", "length", 0.3110)
    Unit("erdélyi rőf", "2 láb", "rőf",
         "Transylvanian", "length", 0.6220)
    Unit("erdélyi öl", "3 rőf", "öl",
         "Transylvanian", "length", 1.866)
    # Based on Bogdán 1990, 34.

    # Selmecbánya (Medieval)
    # Name collision avoided with invisible character U+1D173 at the end of self.name.
    Unit("bányahüvelyk𝅳", "selmeci bányahüvelyk\n1/72 öl", "hüv.",
         "Selmec (Medieval)", "length", 0.028)
    Unit("bányaláb𝅳", "selmeci bányaláb\n12 hüv.", "láb",
         "Selmec (Medieval)", "length", 0.3369)
    Unit("bányarőf𝅳", "selmeci bányarőf\n2 láb", "rőf",
         "Selmec (Medieval)", "length", 0.6738)
    Unit("bányaöl𝅳", "selmeci bányaöl\n3 rőf", "öl",
         "Selmec (Medieval)", "length", 2.0215)
    Unit("bányakötél𝅳", "selmeci bányakötél\n7 öl", "köt.",
         "Selmec (Medieval)", "length", 14.1511)
    # Bogdán 1978, 38.

    # Selmecbánya (Early Modern)
    # Name collision avoided with invisible character U+1D174 at the end of self.name.
    Unit("bányavonal𝅴", "selmeci bányavonal\n1/10 hüv.", "von.",
         "Selmec (Early Modern)", "length", 2.79E-3)
    Unit("bányahüvelyk𝅴", "selmeci bányahüvelyk\n1/72 öl", "hüv.",
         "Selmec (Early Modern)", "length", 0.0279)
    Unit("bányaláb𝅴", "selmeci bányaláb\n12 hüv.", "láb",
         "Selmec (Early Modern)", "length", 0.3368)
    Unit("bányaöl𝅴", "selmeci bányaöl\n6 láb", "öl",
         "Selmec (Early Modern)", "length", 2.021)
    Unit("bányakötél𝅴", "selmeci bányakötél\n7 öl", "köt.",
         "Selmec (Early Modern)", "length", 14.157)
    # Bogdán 1990, 41.

    # Decimal mining units (mid 18th century-)
    # Name collision avoided with invisible character U+1D175 at the end of self.name.
    Unit("bányavonal𝅵", "tízes rendszerű\nbányavonal\n1/100 láb", "von.",
         "Selmec (mid18th c.-)", "length", 2.02E-3)
    Unit("bányahüvelyk𝅵", "tízes rendszerű\nbányahüvelyk\n10 von.", "hüv.",
         "Selmec (mid18th c.-)", "length", 0.02021)
    Unit("bányaláb𝅵", "tízes rendszerű\nbányaláb\n10 hüv.", "láb",
         "Selmec (mid18th c.-)", "length", 0.2021)
    Unit("bányaöl𝅵", "tízes rendszerű\nbányaöl\n10 láb", "öl",
         "Selmec (mid18th c.-)", "length", 2.021)
    # Bogdán 1990, 41–42.
    return
