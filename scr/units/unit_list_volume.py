"""
unit_list_volume.py

Part of the "Unit Converter for Historical Studies" project by OperaVaria.

List of units for volume measurement, in Unit class object form, nested in functions (common, dry, liquid).
Used by set_act_lists function to populate lists.

TODO: Add more units. Possibly merge dry and liquid measures.
"""

# Unit class import:
from units.unit_class import Unit


def shared_units():
    """Modern cubic and imperial units. Passed to both liquid and dry volume category."""

    # (Intermediary: litre. SI base unit is m³, but most values are given in litre in the literature.)

    # SI
    Unit("köbmilliméter", "SI mértékegység\n10⁻⁹m³\nazonos a mikroliterrel", "mm³",
         "SI", "volume", 1E-6)
    Unit("köbcentiméter", "SI mértékegység\n10⁻⁶m³\nazonos a milliliterrel", "cm³",
         "SI", "volume", 1E-3)
    Unit("köbdeciméter", "SI mértékegység\n10⁻³m³\nazonos a literrel", "dm³",
         "SI", "volume", 1)
    Unit("köbméter", "A térfogat\nSI-alapegysége\n10³l", "m³",
         "SI", "volume", 1E3)
    # Based on SI 2009.

    # Litre-based metric
    Unit("mikroliter", "Engedélyezett\nnem SI-mértékegység\n10⁻⁶l", "µl",
         "litre based metric", "volume", 1E-6)
    Unit("milliliter", "Engedélyezett\nnem SI-mértékegység\n10⁻³l", "ml",
         "litre based metric", "volume", 1E-3)
    Unit("centiliter", "Engedélyezett\nnem SI-mértékegység\n10⁻²l", "cl",
         "litre based metric", "volume", 1E-2)
    Unit("deciliter", "Engedélyezett\nnem SI-mértékegység\n10⁻¹l", "dl",
         "litre based metric", "volume", 1E-1)
    Unit("liter", "Engedélyezett\nnem SI-mértékegység\n10⁻³m³", "l",
         "litre based metric", "volume", 1)
    # Based on SI 2009.

    # Anglo-American cubic
    Unit("cubic inch", "ang. köbhüvelyk", "cu in",
         "AngAm cubic", "volume", 0.016387064)
    Unit("cubic foot", "ang. köbláb", "cu ft",
         "AngAm cubic", "volume", 28.316846592)
    Unit("cubic yard", "ang. köbyard", "cu yd",
         "AngAm cubic", "volume", 764.554857984)
    # Based on 1995 No. 1804.

    # Imperial liquid and dry
    Unit("minim (UK)", "brit minim\nlegkisebb űrmérték\n1/480 fl oz", "min",
         "Imperial", "volume", 0.05919390625E-3)
    Unit("fluid dram (UK)", "brit folyadék dram\n60 min", "fl dr",
         "Imperial", "volume", 3.551634375E-3)
    Unit("fluid ounce (UK)", "brit folyadék uncia\n8 fl dr", "fl oz",
         "Imperial", "volume", 28.4130625E-3)
    Unit("gill (UK)", "brit gill\n5 fl oz", "gi",
         "Imperial", "volume", 0.1420653125)
    Unit("pint (UK)", "brit pint\n4 gi", "pt",
         "Imperial", "volume", 0.56826125)
    Unit("quart (UK)", "brit quart\njel. \"negyed\" gallon)\n2 pt", "qt",
         "Imperial", "volume", 1.1365225)
    Unit("gallon (UK)", "brit gallon\n4 qt", "gal",
         "Imperial", "volume", 4.54609)
    Unit("peck (UK)", "brit peck\n(régi szárazmérték)\n2 gl", "pk",
         "Imperial", "volume", 9.092184)
    Unit("bushel (UK)", "brit bushel\n(régi szárazmérték)\n4 pk", "bu",
         "Imperial", "volume", 36.36872)
    # Based on 1995 No. 1804 and Cardarelli 2003, 36–38.
    return


def populate_volume_dry():

    # Sets the unit system list for dry volume unit category
    Unit.act_sys_list = ["SI", "liter alapú metrikus",
                         "angolszász köbmérték", "brit (Imperial)", "amerikai (US customary)",
                         "attikai", "római",
                         "bécsi (1593-1638)", "bécsi (1639-1687)", "bécsi (1688-1755)", "bécsi (1756-1871)",
                         "budai (–17. sz.)"]

    ############################################
    # Units of dry volume, intermediary: litre #
    ############################################

    # Pass modern units.
    shared_units()

    # US customary dry
    Unit("dry pint (US)", "am. száraz pint\n4 gi", "pt (dry)",
         "US customary", "volume",  0.550610471358)
    Unit("dry quart (US)", "am. száraz quart\n(jel. \"negyed\" gallon)\n2 pt", "qt (dry)",
         "US customary", "volume", 1.10122094272)
    Unit("dry gallon (US)", "am. száraz gallon\n4 qt", "gal (dry)",
         "US customary", "volume", 4.40488377086)
    Unit("peck (US)", "am. peck\n2 gl", "pk",
         "US customary", "volume",  8.80976754172)
    Unit("bushel (US)", "am. bushel\n4 pk", "bu",
         "US customary", "volume", 35.2390701669)
    # Based on Cardarelli 2003, 42–44.

    # Attic
    Unit("κύαθος (kyathos)", "gör. hosszú fülű,\nkis méretű\nmerítőpohár", "kyth.",
         "Attic", "volume", 0.0456)
    Unit("κοτύλη (kotylé)", "gör. csésze\n6 kyth.", "kot.",
         "Attic", "volume", 0.274)
    Unit("ξέστης (xestés)", "róm. sextariusból\nazzal megegyező\n2 kot.", "xes.",
         "Attic", "volume", 0.547)
    Unit("χοῖνιξ (choinix)", "egy napi gabona\n2 xes.", "choi.",
         "Attic", "volume", 1.094)
    Unit("ἡμίεκτον (hémiekton)", "jel. \"félhatod\" (medimnos)\n4 choi.", "hhek.",
         "Attic", "volume", 4.377)
    Unit("ἑκτεύς (hekteus)", "jel. \"hatod\" (medimnos)\n2 hémiekton", "hek.",
         "Attic", "volume", 8.754)
    Unit("μέδιμνος (medimnos)", "gör. gabonamérő\n6 hek.", "med.",
         "Attic", "volume", 52.53)
    # Based on Hultsch 1862, 305.

    # Roman
    Unit("cyathus", "att. kyathosból\nazzal megegyező", "cyth.",
         "Roman", "volume", 0.0456)
    Unit("acetabulum", "att. oxybaphonból\nazzal megegyező\n1 1/2 cyth.", "actb.",
         "Roman", "volume", 0.0684)
    Unit("quartarius", "jel. \"negyed\" (sextarius)\n3 cyth.", "quart.",
         "Roman", "volume", 0.137)
    Unit("hemina", "att. kothyléból\nazzal megegyező\n6 cyth.", "hem.",
         "Roman", "volume", 0.274)
    Unit("sextarius", "jel. \"hatod\" (congius)\n2 hem.", "sext.",
         "Roman", "volume", 0.547)
    Unit("semimodius", "jel. \"fél modius\"\n8 sext.", "smod.",
         "Roman", "volume", 4.377)
    Unit("modius", "római gabonamérő\n16 sext.", "mod.",
         "Roman", "volume", 8.754)
    # Based on Hultsch 1862, 306.

    # Viennese (1593-1638)
    # Name collision avoided with invisible character U+1D173 at the end of self.name.
    Unit("Wiener Becher𝅳", "bécsi pohár\n1/128 Metz.", "Bech.",
         "Viennese (1593-1638)", "volume", 0.3295)
    Unit("Wiener Futtermassel𝅳", "jel. \"takarmánymesszely\"\n1/64 Metz.", "FM",
         "Viennese (1593-1638)", "volume", 0.6590)
    Unit("Wiener Kleines Massel𝅳", "jel. \"kis messzely\"\n1/32 Metz.", "KM",
         "Viennese (1593-1638)", "volume", 1.3181)
    Unit("Wiener Müllermassel𝅳", "jel. \"molnármesszely\"\n1/16 Metz.", "MM",
         "Viennese (1593-1638)", "volume", 2.6362)
    Unit("Wiener Achtel𝅳", "bécsi nyolcadmérős\n(1/8 Metz.)", "Acht.",
         "Viennese (1593-1638)", "volume", 5.2725)
    Unit("Wiener Viertel𝅳", "bécsi negyedmérős\n(1/4 Metz.)", "Vier.",
         "Viennese (1593-1638)", "volume", 10.545)
    Unit("Wiener Halbe𝅳", "bécsi félmérős\n(1/2 Metz.)", "Hal.",
         "Viennese (1593-1638)", "volume", 21.09)
    Unit("Wiener Metzen𝅳", "bécsi mérő\nalapmérték𝅳", "Metz.",
         "Viennese (1593-1638)", "volume", 42.18)
    Unit("Wiener Muth𝅳", "bécsi mut\nnagyker. egység\n30 Metz.𝅳", "Mut",
         "Viennese (1593-1638)", "volume", 1265.40)
    # Based on Bogdán 1991, 40–42.

    # Viennese (1639-1687)
    # Name collision avoided with invisible character U+1D174 at the end of self.name.
    Unit("Wiener Becher𝅴", "bécsi pohár\n1/128 Metz.", "Bech.",
         "Viennese (1639-1687)", "volume", 0.3592)
    Unit("Wiener Futtermassel𝅴", "jel. \"takarmánymesszely\"\n1/64 Metz.", "FM",
         "Viennese (1639-1687)", "volume", 0.7190)
    Unit("Wiener Kleines Massel𝅴", "jel. \"kis messzely\"\n1/32 Metz.", "KM",
         "Viennese (1639-1687)", "volume", 1.4381)
    Unit("Wiener Müllermassel𝅴", "jel. \"molnármesszely\"\n1/16 Metz.", "MM",
         "Viennese (1639-1687)", "volume", 2.8762)
    Unit("Wiener Achtel𝅴", "bécsi nyolcadmérős\n(1/8 Metz.)", "Acht.",
         "Viennese (1639-1687)", "volume", 5.7525)
    Unit("Wiener Viertel𝅴", "bécsi negyedmérős\n(1/4 Metz.)", "Vier.",
         "Viennese (1639-1687)", "volume", 11.505)
    Unit("Wiener Halbe𝅴", "bécsi félmérős\n(1/2 Metz.)", "Hal.",
         "Viennese (1639-1687)", "volume", 23.01)
    Unit("Wiener Metzen𝅴", "bécsi mérő\nalapmérték𝅳", "Metz.",
         "Viennese (1639-1687)", "volume", 46.02)
    Unit("Wiener Muth𝅴", "bécsi mut\nnagyker. egység\n30 Metz.𝅳", "Mut",
         "Viennese (1639-1687)", "volume", 1380.60)
    # Based on Bogdán 1991, 40–42.

    # Viennese (1688-1755)
    # Name collision avoided with invisible character U+1D175 at the end of self.name.
    Unit("Wiener Becher𝅵", "bécsi pohár\n1/128 Metz.", "Bech.",
         "Viennese (1688-1755)", "volume", 0.3577)
    Unit("Wiener Futtermassel𝅵", "jel. \"takarmánymesszely\"\n1/64 Metz.", "FM",
         "Viennese (1688-1755)", "volume", 0.7154)
    Unit("Wiener Kleines Massel𝅵", "jel. \"kis messzely\"\n1/32 Metz.", "KM",
         "Viennese (1688-1755)", "volume", 1.4309)
    Unit("Wiener Müllermassel𝅵", "jel. \"molnármesszely\"\n1/16 Metz.", "MM",
         "Viennese (1688-1755)", "volume", 2.8618)
    Unit("Wiener Achtel𝅵", "bécsi nyolcadmérős\n(1/8 Metz.)", "Acht.",
         "Viennese (1688-1755)", "volume", 5.7237)
    Unit("Wiener Viertel𝅵", "bécsi negyedmérős\n(1/4 Metz.)", "Vier.",
         "Viennese (1688-1755)", "volume", 11.447)
    Unit("Wiener Halbe𝅵", "bécsi félmérős\n(1/2 Metz.)", "Hal.",
         "Viennese (1688-1755)", "volume", 22.895)
    Unit("Wiener Metzen𝅵", "bécsi mérő\nalapmérték𝅳", "Metz.",
         "Viennese (1688-1755)", "volume", 45.79)
    Unit("Wiener Muth𝅵", "bécsi mut\nnagyker. egység\n30 Metz.𝅳", "Mut",
         "Viennese (1688-1755)", "volume", 1373.70)
    # Based on Bogdán 1991, 40–42.

    # Viennese (1756-1871)
    # Name collision avoided with invisible character U+1D176 at the end of self.name.
    Unit("Wiener Becher𝅶", "bécsi pohár\n1/128 Metz.", "Bech.",
         "Viennese (1756-1871)", "volume", 0.4803)
    Unit("Wiener Futtermassel𝅶", "jel. \"takarmánymesszely\"\n1/64 Metz.", "FM",
         "Viennese (1756-1871)", "volume", 0.9607)
    Unit("Wiener Kleines Massel𝅶", "jel. \"kis messzely\"\n1/32 Metz.", "KM",
         "Viennese (1756-1871)", "volume", 1.9214)
    Unit("Wiener Müllermassel𝅶", "jel. \"molnármesszely\"\n1/16 Metz.", "MM",
         "Viennese (1756-1871)", "volume", 3.8429)
    Unit("Wiener Achtel𝅶", "bécsi nyolcadmérős\n(1/8 Metz.)", "Acht.",
         "Viennese (1756-1871)", "volume", 7.6858)
    Unit("Wiener Viertel𝅶", "bécsi negyedmérős\n(1/4 Metz.)", "Vier.",
         "Viennese (1756-1871)", "volume", 15.3714)
    Unit("Wiener Halbe𝅶", "bécsi félmérős\n(1/2 Metz.)", "Hal.",
         "Viennese (1756-1871)", "volume", 30.7434)
    Unit("Wiener Metzen𝅶", "bécsi mérő\nalapmérték𝅳", "Metz.",
         "Viennese (1756-1871)", "volume", 61.4768)
    Unit("Wiener Muth𝅶", "bécsi mut\nnagyker. egység\n30 Metz.𝅳", "Mut",
         "Viennese (1756-1871)", "volume", 1844.60)
    # Based on Bogdán 1991, 40–42.

    # Buda (-17th century)
    Unit("budai száraz icce", "1 1/4 híg icce", "icce",
         "Buda (-17th c.)", "volume", 1.0491)
    Unit("budai véka", "16 híg icce", "véka",
         "Buda (-17th c.)", "volume", 13.43)
    Unit("budai mérő", "4 véka", "mérő",
         "Buda (-17th c.)", "volume", 53.72)
    # Based on Bogdán 1991, 42.
    return


def populate_volume_liq():

    # Sets the unit system list for liquid volume unit category
    Unit.act_sys_list = ["SI", "liter alapú metrikus",
                         "angolszász köbmérték", "brit (Imperial)", "amerikai (US customary)",
                         "attikai", "római",
                         "bécsi kisker. (–1359)", "bécsi kisker. (1359–1556)", "bécsi kisker. (1557–1568)",
                         "bécsi kisker. (1569–1761)", "bécsi kisker. (1762–1871)",
                         "bécsi nagyker. (-1761)", "bécsi nagyker. (1762-1871)",
                         "budai (-17. sz.)",
                         "erdélyi (-1823)", "erdélyi (1823-1874)"]

    ###############################################
    # Units of liquid volume, intermediary: litre #
    ###############################################

    # Pass modern units.
    shared_units()

    # US customary liquid
    Unit("minim (US)", "am. minim\nlegkisebb űrmérték\n1/480 fl oz", "min",
         "US customary", "volume", 0.161151992E-3)
    Unit("fluid dram (US)", "am. folyadék dram\n60 min", "fl dr",
         "US customary", "volume", 3.696691195E-3)
    Unit("fluid ounce (US)", "am. folyadék uncia\n8 fl dr", "fl oz",
         "US customary", "volume", 29.57353E-03)
    Unit("gill (US)", "am. gill\n4 fl oz\n(vö. brit = 5 fl oz)", "gi",
         "US customary", "volume", 0.11829412)
    Unit("pint (US)", "am. (folyadék) pint\n4 gi", "pt (fluid)",
         "US customary", "volume", 0.4731765)
    Unit("quart (US)", "am. (folyadék) quart\n(jel. negyed gallon)\n2 pt", "qt (fluid)",
         "US customary", "volume", 0.9463529)
    Unit("gallon (US)", "am. (folyadék) gallon\n4 qt", "gal (fluid)",
         "US customary", "volume", 3.785412)
    # Based on Butcher et al. 2003, 9-10.

    # Attic
    Unit("κύαθος (kyathos)", "gör. hosszú fülű,\nkis méretű\nmerítőpohár", "kyth.",
         "Attic", "volume", 0.0456)
    Unit("ὀξυβαφον (oxybaphon)", "gör. mártásos\ncsésze\n1 1/2 kyth.", "oxy.",
         "Attic", "volume", 0.0684)
    Unit("τέταρτον (tetarton)", "róm quartaruisból\nazzal megegyező\n3 kyth.", "tetr.",
         "Attic", "volume", 0.137)
    Unit("κοτύλη (kotylé)", "gör. csésze\n6 kyth.", "kot.",
         "Attic", "volume", 0.274)
    Unit("ξέστης (xestés)", "róm. sextariusból\nazzal megegyező\n2 kot.", "xes.",
         "Attic", "volume", 0.547)
    Unit("χοῦς (chus)", "gör. kancsó\n12 kot.", "chus",
         "Attic", "volume", 3.283)
    Unit("μετρητής (metrétés)", "gör. foyladékmérő\n12 choes", "metr.",
         "Attic", "volume", 39.39)
    # Based on Hultsch 1862, 305.

    # Roman
    Unit("cyathus", "att. kyathosból\nazzal megegyező", "cyth.",
         "Roman", "volume", 0.0456)
    Unit("acetabulum", "att. oxybaphonból\nazzal megegyező\n1 1/2 cyth.", "actb.",
         "Roman", "volume", 0.0684)
    Unit("quartarius", "jel. negyed (sextarius)\n3 cyth.", "quart.",
         "Roman", "volume", 0.137)
    Unit("hemina", "att. kothyléból\nazzal megegyező\n6 cyth.", "hem.",
         "Roman", "volume", 0.274)
    Unit("sextarius", "jel. hatod (congius)\n2 hem.", "sext.",
         "Roman", "volume", 0.547)
    Unit("congius", "att. chusból\nazzal megegyező\n12 hem.", "cong.",
         "Roman", "volume", 3.283)
    Unit("urna", "vízmerítő edény\n4 congius\n1/2 amph.", "urna",
         "Roman", "volume", 13.13)
    Unit("amphora", "1 köbláb űrtartalmú\namph.", "amph.",
         "Roman", "volume", 26.26)
    # Based on Hultsch 1862, 306.

    # Viennese small retail (-1359)
    # Name collision avoided with invisible character U+1D173 at the end of self.name.
    Unit("Wiener Pfiff𝅳", "bécsi römpöly\n1/256 Eim.", "Pfi.",
         "Viennese small (-1359)", "volume", 0.22651)
    Unit("Wiener Seidel𝅳", "bécsi messzely\n2 Pfi.", "Sei.",
         "Viennese small (-1359)", "volume", 0.45302)
    Unit("Wiener Halbe𝅳", "bécsi icce\n2 Sei.", "Hal.",
         "Viennese small (-1359)", "volume", 0.90605)
    Unit("Wiener Maß𝅳", "bécsi pint\n2 Hal.", "Maß",
         "Viennese small (-1359)", "volume", 1.8126)
    Unit("Wiener Eimer𝅳", "bécsi akó\n32 Maß𝅳", "Eim.",
         "Viennese small (-1359)", "volume", 58.0037)
    # Based on Bogdán 1991, 29.

    # Viennese small retail (1359-1556)
    # Name collision avoided with invisible character U+1D174 at the end of self.name.
    Unit("Wiener Pfiff𝅴", "bécsi römpöly\n280 Eim.", "Pfi.",
         "Viennese small (1359-1556)", "volume", 0.20715)
    Unit("Wiener Seidel𝅴", "bécsi messzely\n2 Pfi.", "Sei.",
         "Viennese small (1359-1556)", "volume", 0.4143)
    Unit("Wiener Halbe𝅴", "bécsi icce\n2 Sei.", "Hal.",
         "Viennese small (1359-1556)", "volume", 0.8286)
    Unit("Wiener Maß𝅴", "bécsi pint\n2 Hal.", "Maß",
         "Viennese small (1359-1556)", "volume", 1.6572)
    Unit("Wiener Eimer𝅴", "bécsi akó\n35 Maß", "Eim.",
         "Viennese small (1359-1556)", "volume", 58.0037)
    # Based on Bogdán 1991, 29.

    # Viennese small retail (1557-1568)
    # Name collision avoided with invisible character U+1D175 at the end of self.name.
    Unit("Wiener Pfiff𝅵", "bécsi römpöly\n1/304 Eim.", "Pfi.",
         "Viennese small (1557-1568)", "volume", 0.1908)
    Unit("Wiener Seidel𝅵", "bécsi messzely\n2 Pfi.", "Sei.",
         "Viennese small (1557-1568)", "volume", 0.3816)
    Unit("Wiener Halbe𝅵", "bécsi icce\n2 Sei.", "Hal.",
         "Viennese small (1557-1568)", "volume", 0.7632)
    Unit("Wiener Maß𝅵", "bécsi pint\n2 Hal.", "Maß",
         "Viennese small (1557-1568)", "volume", 1.5264)
    Unit("Wiener Eimer𝅵", "bécsi akó\n38 Maß", "Eim.",
         "Viennese small (1557-1568)", "volume", 58.0037)
    # Based on Bogdán 1991, 29.

    # Viennese small retail (1569-1761)
    # Name collision avoided with invisible character U+1D176 at the end of self.name.
    Unit("Wiener Pfiff𝅶", "bécsi römpöly\n1/328 Eim.", "Pfi.",
         "Viennese small (1569-1761)", "volume", 0.17684)
    Unit("Wiener Seidel𝅶", "bécsi messzely\n2 Pfi.", "Sei.",
         "Viennese small (1569-1761)", "volume", 0.35368)
    Unit("Wiener Halbe𝅵𝅶", "bécsi icce\n2 Sei.", "Hal.",
         "Viennese small (1569-1761)", "volume", 0.70736)
    Unit("Wiener Maß𝅶", "bécsi pint\n2 Hal.", "Maß",
         "Viennese small (1569-1761)", "volume", 1.4147)
    Unit("Wiener Eimer𝅶", "bécsi akó\n41 Maß", "Eim.",
         "Viennese small (1569-1761)", "volume", 58.0037)
    # Based on Bogdán 1991, 29.

    # Viennese small retail (1762-1871)
    # Name collision avoided with invisible character U+1D177 at the end of self.name.
    Unit("Wiener Pfiff𝅷", "bécsi römpöly\n1/320 Eim.", "Pfi.",
         "Viennese small (1762-1871)", "volume", 0.17684)
    Unit("Wiener Seidel𝅷", "bécsi messzely\n2 Pfi.", "Sei.",
         "Viennese small (1762-1871)", "volume", 0.35368)
    Unit("Wiener Halbe𝅵𝅷", "bécsi icce\n2 Sei.", "Hal.",
         "Viennese small (1762-1871)", "volume", 0.70736)
    Unit("Wiener Maß𝅷", "bécsi pint\n2 Hal.", "Maß",
         "Viennese small (1762-1871)", "volume", 1.41472)
    Unit("Wiener Eimer𝅷", "bécsi akó\n40 Maß", "Eim.",
         "Viennese small (1762-1871)", "volume", 56.4890)
    # Based on Bogdán 1991, 30.

    # Viennese wholesale (-1761)
    # Name collision avoided with invisible character U+1D173 at the end of self.name.
    Unit("Wiener Eimer (nagyker.)𝅳", "bécsi (nagykereskedelmi) akó", "Eim.",
         "Viennese wholesale (-1761)", "volume", 58)
    Unit("Wiener Dreiling𝅳", "bécsi dreiling\n24 Eim.", "Drei.",
         "Viennese wholesale (-1761)", "volume", 1392)
    Unit("Wiener Fuder𝅳", "bécsi fuder\n32 Eim.", "Fud.",
         "Viennese wholesale (-1761)", "volume", 1856)
    # Based on Bogdán 1991, 30.

    # Viennese wholesale (1762-1871)
    # Name collision avoided with invisible character U+1D174 at the end of self.name.
    Unit("Wiener Eimer (nagyker)𝅴", "bécsi (nagykereskedelmi) akó", "Eim.",
         "Viennese wholesale (1762-1871)", "volume", 56.589)
    Unit("Wiener Bierfaß𝅴", "bécsi söröshordó\n2 Eim.", "Bfaß.",
         "Viennese wholesale (1762-1871)", "volume", 113.18)
    Unit("Wiener Weinfaß𝅴", "bécsi boroshordó\n10 Eim.", "Wfaß.",
         "Viennese wholesale (1762-1871)", "volume", 565.89)
    Unit("Wiener Dreiling𝅴", "bécsi dreiling\n24 Eim.", "Drei.",
         "Viennese wholesale (1762-1871)", "volume", 1697.67)
    Unit("Wiener Fuder𝅴", "bécsi fuder\n32 Eim.", "Fud.",
         "Viennese wholesale (1762-1871)", "volume", 1810.85)
    # Based on Bogdán 1991, 30.

    # Buda (-17th century)
    Unit("budai messzely", "1/32 köböl", "messz.",
         "Buda (-17th c.)", "volume", 0.4197)
    Unit("budai icce", "2 messzely", "icce",
         "Buda (-17th c.)", "volume", 0.8393)
    Unit("budai pint", "2 icce", "pint",
         "Buda (-17th c.)", "volume", 1.6786)
    Unit("budai köböl", "8 pint", "köb.",
         "Buda (-17th c.)", "volume", 13.43)
    Unit("budai kis akó", "44 icce", "k. akó",
         "Buda (-17th c.)", "volume", 36.93)
    Unit("budai nagy akó", "64 icce", "n. akó",
         "Buda (-17th c.)", "volume", 53.72)
    # Based on Bogdán 1991, 31.

    # Transylvanian (-1823)
    # Name collision avoided with invisible character U+1D173 at the end of self.name.
    Unit("erdélyi icce𝅳", "1/16 vöd.", "icce",
         "Transylvanian (-1823)", "volume", 0.6816)
    Unit("erdélyi kupa𝅳", "2 icce", "kupa",
         "Transylvanian (-1823)", "volume", 1.3623)
    Unit("erdélyi vödör𝅳", "8 kupa", "vöd.",
         "Transylvanian (-1823)", "volume", 10.90)
    Unit("erdélyi kis hordó𝅳", "nagykereskedelmi\n20 vöd.", "kihor.",
         "Transylvanian (-1823)", "volume", 218)
    Unit("erdélyi földes hordó𝅳", "nagykereskedelmi\n40 vöd., 2 kihor.", "föhor.",
         "Transylvanian (-1823)", "volume", 436)
    Unit("erdélyi öreg hordó𝅳", "nagykereskedelmi\n80 vöd., 2 föhor.", "örhor.",
         "Transylvanian (-1823)", "volume", 872)
    # Based on Bogdán 1991, 32-33.

    # Transylvanian (1823-1874)
    # Name collision avoided with invisible character U+1D174 at the end of self.name.
    Unit("erdélyi messzely𝅴", "1/32 vöd.", "messz.",
         "Transylvanian (1823-1874)", "volume", 0.3537)
    Unit("erdélyi icce𝅴", "2 messz.", "icce",
         "Transylvanian (1823-1874)", "volume", 0.7074)
    Unit("erdélyi kupa𝅴", "2 icce\na bécsi pint\nadoptálása", "kupa",
         "Transylvanian (1823-1874)", "volume", 1.4147)
    Unit("erdélyi vödör𝅴", "8 kupa", "vöd.",
         "Transylvanian (1823-1874)", "volume", 11.32)
    Unit("erdélyi köböl𝅴", "8 vöd.", "köb.",
         "Transylvanian (1823-1874)", "volume", 90.54)
    Unit("erdélyi kis hordó𝅴", "nagykereskedelmi\n5 vöd.", "kihor.",
         "Transylvanian (1823-1874)", "volume", 56.60)
    Unit("erdélyi közepes hordó𝅴", "nagykereskedelmi\n10 vöd., 2 kihor.", "köhor.",
         "Transylvanian (1823-1874)", "volume", 112.20)
    Unit("erdélyi nagy hordó𝅴", "nagykereskedelmi\n40 vöd., 4 köhor.", "nahor.",
         "Transylvanian (1823-1874)", "volume", 452.80)
    # Based on Bogdán 1991, 32-33.
    return
