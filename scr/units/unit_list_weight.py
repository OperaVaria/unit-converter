"""
unit_list_weight.py

Part of the "Unit Converter for Historical Studies" project by OperaVaria.

List of units for weight measurement, in Unit class object form, nested in a function.
Used by set_act_lists function to populate lists.

TODO: add more units.
"""

# Unit class import
from units.unit_class import Unit


def populate_weight():

    # Sets the unit system list for weight unit category
    Unit.act_sys_list = ["metrikus",
                         "angolszász avoirdupois", "angolszász troy", "angolszász patikai",
                         "attikai (\"solóni\")", "attikai (késő klasszikus)", "hellenisztikus", "késő hellenisztikus",
                         "római (uncia törtrészei)", "római (uncia–libra)", "római (libra többszörösei)",
                         "bécsi (15–16. sz.)", "bécsi (17. sz.–1756)", "bécsi (1756–1874)", "bécsi vámsúly (1851–1874)",
                         "budai (–13. sz.)", "budai (14. sz.–1686)",
                         "pozsonyi (–1854)", "pozsonyi (1854–1874)",
                         "magyar (16–18. sz.)",
                         "erdélyi (1680köz.–1690köz.)", "erdélyi (1690köz.–1721)", "erdélyi (1721–1874)",
                         "magyarországi török"]

    #########################################
    # Units of mass, intermediary: kilogram #
    #########################################

    # Metric
    Unit("gramm", "SI mértékegység\n10⁻³kg", "g",
         "SI", "mass", 1E-3)
    Unit("dekagramm", "SI mértékegység\n10⁻²kg", "dag",
         "SI", "mass", 1E-2)
    Unit("kilogramm", "A súly\nSI-alapegysége", "kg",
         "SI", "mass", 1)
    Unit("tonna", "Engedélyezett\nnem SI-mértékegység\n10³kg", "t",
         "accepted non-SI", "mass", 1E3)
    # Based on SI 2009.

    # Avoirdupois
    Unit("grain", "egy gabonaszem\nsúlya\n1/7000 lb av.", "gr av.",
         "Avoirdupois", "mass", 0.06479891E-3)
    Unit("dram", "a drachma szóból\n1/256 lb av.", "dr av.",
         "Avoirdupois", "mass", 1.7718451953125E-3)
    Unit("ounce", "av. uncia\n16 dr av.", "oz av.",
         "Avoirdupois", "mass", 0.028349523125)
    Unit("pound", "av. font\n16 oz av.", "lb av.",
         "Avoirdupois", "mass", 0.45359237)
    Unit("stone", "av. mérőkő\n14 lb av.", "st av.",
         "Avoirdupois", "mass", 6.35029318)
    Unit("quarter", "\"negyed\" hundredweight\n 2 st av.\n28 lb av.", "qr av.",
         "Avoirdupois", "mass", 12.70058636)
    Unit("hundredweight (USA)", "am. un. \"short\"\nhundredweight\n100 lb av.", "CH",
         "Avoirdupois", "mass", 45.359237)
    Unit("hundredweight (UK)", "brit un. \"long\"\nhundredweight\n112 lb av.", "cwt (long)",
         "Avoirdupois", "mass", 50.80234544)
    Unit("ton (USA)", "am. un. \"short\" ton\n2000 lb av.", "ton (short)",
         "Avoirdupois", "mass", 907.184740)
    Unit("ton (UK)", "brit un. \"long\" ton\n2240 lb av.", "ton (long)",
         "Avoirdupois", "mass", 1016.0469088)
    # Based on 1995 No. 1804 and Cardarelli 2003, 37–38.

    # Troy
    Unit("grain (troy)", "egy gabonaszem\nsúlya\n1/5760 lb t.", "gr t.",
         "Troy", "mass", 0.12959782E-3)
    Unit("pennyweight (troy)", "régi ezüstpenny súlya\n24 gr t.", "dwt",
         "Troy", "mass", 1.7718451953125E-3)
    Unit("ounce (troy)", "troy uncia\n20 dwt t.", "oz t.",
         "Troy", "mass", 0.0311034768)
    Unit("pound (troy)", "troy font\n12 oz t.", "lb t.",
         "Troy", "mass", 0.3732417216)
    # Based on 1995 No. 1804 and Cardarelli 2003, 38-39.

    # Apothecaries'
    Unit("grain (apoth.)", "egy gabonaszem\nsúlya\n1/5760 lb ap.", "gr ap.",
         "Apothecaries", "mass", 0.06479891E-3)
    Unit("scruple (apoth.)", "lat. scrupulum szóból\n20 gr ap.", "scr ap.",
         "Apothecaries", "mass", 1.2959782E-3)
    Unit("dram (apoth.)", "a drachma szóból\n3 scr ap.", "dr ap.",
         "Apothecaries", "mass", 3.8879346E-3)
    Unit("ounce (apoth.)", "ang. gyógyszertári\nuncia\n8 dr ap.", "oz ap.",
         "Apothecaries", "mass", 0.0311034768)
    Unit("pound (apoth.)", "ang. gyógyszertári\nfont\n12 oz ap.", "lb ap.",
         "Apothecaries", "mass", 0.3732417216)
    # Based on Cardarelli 2003, 38.

    # Attic 'Solonic'
    # Name collision avoided with invisible character U+1D173 at the end of self.name.
    Unit("δραχμή (drachmé)𝅳", "végig változatlan súly\naz arány igazodik\n1/6300 tal.", "drach.",
         "Attic Solonic", "mass", 4.366E-3)
    Unit("ἡμιστάτηρον (hémistatéron)𝅳", "jel. \"félstatéros\"\n105 drach.", "hstat.",
         "Attic Solonic", "mass", 458.43E-3)
    Unit("στατήρ (statér)𝅳", "2 hstat.\n210 drach.", "stat.",
         "Attic Solonic", "mass", 916.86E-3)
    Unit("τάλαντον (talanton)𝅳", "alapmérték\n30 stat.", "tal.",
         "Attic Solonic", "mass", 27.506)
    # Based on Egger, Jochen, and Smart 2010, 462.

    # Attic Late Classical
    # Name collision avoided with invisible character U+1D174 at the end of self.name.
    Unit("δραχμή (drachmé)𝅴", "végig változatlan súly\naz arány igazodik\n1/6600 tal.", "drach.",
         "Attic LC", "mass", 4.366E-3)
    Unit("μνᾶ (mina)𝅴", "110 drach.", "mna",
         "Attic LC", "mass", 480.26E-3)
    Unit("στατήρ (statér)𝅴", "2 mna\n220 drach.", "stat.",
         "Attic LC", "mass", 960.52E-3)
    Unit("τάλαντον (talanton)𝅴", "alapmérték\n30 stat.", "tal.",
         "Attic LC", "mass", 28.816)
    # Based on Egger, Jochen, and Smart 2010, 462.

    # Hellenistic
    # Name collision avoided with invisible character U+1D175 at the end of self.name.
    Unit("δραχμή (drachmé)𝅵", "végig változatlan súly\naz arány igazodik\n1/8280 tal.", "drach.",
         "Early Hellenistic", "mass", 4.366E-3)
    Unit("μνᾶ (mina)𝅵", "138 drach.", "mna",
         "Early Hellenistic", "mass", 602.508E-3)
    Unit("στατήρ (statér)𝅵", "2 mna\n276 drach.", "stat.",
         "Early Hellenistic", "mass", 1.205016)
    Unit("τάλαντον (talanton)𝅵", "alapmérték\n30 stat.", "tal.",
         "Early Hellenistic", "mass", 36.150)
    # Based on Egger, Jochen, and Smart 2010, 463.

    # Late Hellenistic
    # Name collision avoided with invisible character U+1D176 at the end of self.name.
    Unit("δραχμή (drachmé)𝅶", "végig változatlan súly\naz arány igazodik\n1/9000 tal.", "drach.",
         "Late Hellenistic", "mass", 4.366E-3)
    Unit("μνᾶ (mina)𝅶", "150 drach.", "mna",
         "Late Hellenistic", "mass", 654.9E-3)
    Unit("két mina [n.n.]𝅶", "a mérték korabeli\nneve ismeretlen\n300 drach.", "stat.",
         "Late Hellenistic", "mass", 1.3098)
    Unit("τάλαντον (talanton)𝅶", "alapmérték\n60 mna", "tal.",
         "Late Hellenistic", "mass", 39.294)
    # Based on Egger, Jochen, and Smart 2010, 463.

    # Roman (fractions of uncia)
    Unit("siliqua", "jel. \"hüvely\"\n1/6 scr.", "sil.",
         "Roman (uncia fraction)", "mass", 0.189E-3)
    Unit("lupinus", "jel. \"farkasbab\"\n1/4 scr.", "lup.",
         "Roman (uncia fraction)", "mass", 0.284E-3)
    Unit("obolus", "gör. obolosból\n1/6 drach.\n1/2 scr.", "ob.",
         "Roman (uncia fraction)", "mass", 0.568E-3)
    Unit("scripulum", "1/24 un.", "scr.",
         "Roman (uncia fraction)", "mass", 1.137E-3)
    Unit("dimidia sextula", "1/2 sext.\n1/12 un.", "dsext.",
         "Roman (uncia fraction)", "mass", 2.274E-3)
    Unit("drachma", "gör. drachméból\n1/8 un.", "darch.",
         "Roman (uncia fraction)", "mass", 3.411E-3)
    Unit("sextula", "1/6 un.", "sext.",
         "Roman (uncia fraction)", "mass", 4.548E-3)
    Unit("sicilicus", "aka quartuncia\n1/4 un.", "sic.",
         "Roman (uncia fraction)", "mass", 6.822E-3)
    Unit("binae sextulae", "2 sext.\naka duella\n1/3 un.", "bsext.",
         "Roman (uncia fraction)", "mass", 9.096E-3)
    Unit("semuncia", "1/2 un.", "semun.",
         "Roman (uncia fraction)", "mass", 13.644E-3)
    Unit("uncia", "róm. uncia\n1/12 lib.", "un.",
         "Roman (uncia fraction)", "mass", 27.288E-3)
    # Based on Vilmos 1984 and Egger, Jochen, and Smart 2010, 463.

    # Roman (from uncia to libra)
    Unit("uncia", "róm. uncia\n1/12 lib.", "un.",
         "Roman (uncia-libra)", "mass", 27.288E-3)
    Unit("sescuncia", "1 1/2 un.", "seun.",
         "Roman (uncia-libra)", "mass", 40.931E-3)
    Unit("sextans", "1/6 lib.\n2 un.", "sexta.",
         "Roman (uncia-libra)", "mass", 54.575E-3)
    Unit("quadrans", "1/4 lib.\n3 un.", "quad.",
         "Roman (uncia-libra)", "mass", 81.863E-3)
    Unit("triens", "1/3 lib.\n4 un.", "tri.",
         "Roman (uncia-libra)", "mass", 109.150E-3)
    Unit("quincunx", "5 un.", "quix.",
         "Roman (uncia-libra)", "mass", 136.438E-3)
    Unit("semis", "jel. \"fél\" (libra)\n6 un.", "semi.",
         "Roman (uncia-libra)", "mass", 163.725E-3)
    Unit("septunx", "7 un.", "sept.",
         "Roman (uncia-libra)", "mass", 191.013E-3)
    Unit("bes", "2/3 lib.\n8 un.", "bes",
         "Roman (uncia-libra)", "mass", 218.30E-3)
    Unit("dodrans", "3/4 lib.\n9 un.", "dod.",
         "Roman (uncia-libra)", "mass", 245.588E-3)
    Unit("dextans", "5/6 lib.\n10 un.", "dex.",
         "Roman (uncia-libra)", "mass", 272.875E-3)
    Unit("deunx", "11 un.", "deu.",
         "Roman (uncia-libra)", "mass", 300.163E-3)
    Unit("libra", "róm. font\n12 un.", "lib.",
         "Roman (uncia-libra)", "mass", 0.32745)
    # Based on Vilmos 1984 and Egger, Jochen, and Smart 2010, 464.

    # Roman (libra multiples)
    Unit("libra", "róm. font\n12 un.", "lib.",
         "Roman (libra multiple)", "mass", 0.32745)
    Unit("dupondius", "aka dussis\n2 lib.", "dup.",
         "Roman (libra multiple)", "mass", 0.6549)
    Unit("tressis", "3 lib.", "tres.",
         "Roman (libra multiple)", "mass", 0.98235)
    Unit("quincussis", "5 lib.", "quinc.",
         "Roman (libra multiple)", "mass", 1.63725)
    Unit("decussis", "10 lib.", "dec.",
         "Roman (libra multiple)", "mass", 3.2745)
    # Based on Vilmos 1984 and Egger, Jochen, and Smart 2010, 464.

    # Viennese (15-16th century)
    # Name collision avoided with invisible character U+1D173 at the end of self.name.
    Unit("Wiener Loth𝅳", "bécsi lat\n1/32 Pfund", "Loth",
         "Viennese (15-16th c.)", "mass", 0.0173687)
    Unit("Wiener Unzen𝅳", "bécsi nehezék\nv. uncia\n2 Loth", "Unz.",
         "Viennese (15-16th c.)", "mass", 0.0347375)
    Unit("Wiener Pfund𝅳", "bécsi font\n16 Unz.", "Pfund",
         "Viennese (15-16th c.)", "mass", 0.55580)
    Unit("Wiener Zentner𝅳", "bécsi mázsa\n100 Pfund", "Zent.",
         "Viennese (15-16th c.)", "mass", 55.58)
    # Based on Bogdán 1991, 49.

    # Viennese (17th century-1756)
    # Name collision avoided with invisible character U+1D174 at the end of self.name.
    Unit("Wiener Loth𝅴", "bécsi lat\n1/32 Pfund", "Loth",
         "Viennese (17th c.-1756)", "mass", 0.0175381)
    Unit("Wiener Unzen𝅴", "bécsi nehezék\nv. uncia\n2 Loth", "Unz.",
         "Viennese (17th c.-1756)", "mass", 0.0350762)
    Unit("Wiener Pfund𝅴", "bécsi font\n16 Unz.", "Pfund",
         "Viennese (17th c.-1756)", "mass", 0.56122)
    Unit("Wiener Zentner𝅴", "bécsi mázsa\n100 Pfund", "Zent.",
         "Viennese (17th c.-1756)", "mass", 56.122)
    # Based on Bogdán 1991, 49.

    # Viennese (1756-1874)
    # Name collision avoided with invisible character U+1D175 at the end of self.name.
    Unit("Wiener Loth𝅵", "bécsi lat\n1/32 Pfund", "Loth",
         "Viennese (1756-1874)", "mass", 0.0175018)
    Unit("Wiener Unzen𝅵", "bécsi nehezék\nv. uncia\n2 Loth", "Unz.",
         "Viennese (1756-1874)", "mass", 0.035003)
    Unit("Wiener Pfund𝅵", "bécsi font\n16 Unz.", "Pfund",
         "Viennese (1756-1874)", "mass", 0.56)
    Unit("Wiener Zentner𝅵", "bécsi mázsa\n100 Pfund", "Zent.",
         "Viennese (1756-1874)", "mass", 56.006)
    # Based on Bogdán 1991, 49.

    # Viennese customs (1851-1874)
    Unit("Zoll-Loth", "bécsi (német) vámlat\n", "ZLoth",
         "Viennese customs", "mass", 1.666)
    Unit("Zollpfund", "bécsi (német) vámfont\n30 ZLoth\n50 dag-hoz igazítva", "ZPfund",
         "Viennese customs", "mass", 0.50)
    Unit("Zollzentner", "bécsi (német) vámmázsa\n100 ZPfund\n50 kg-hoz igazítva", "ZZent.",
         "Viennese customs", "mass", 50)

    # Buda (-13th century)
    # Name collision avoided with invisible character U+1D173 at the end of self.name.
    Unit("budai ferton𝅳", "jel. \"negyed\" (márka)\n1/880 mázsa", "fert.",
         "Buda (-13th c.)", "mass", 0.061384)
    Unit("budai márka𝅳", "4 fert.", "márka",
         "Buda (-13th c.)", "mass", 0.2455)
    Unit("budai mázsa𝅳", "220 márka", "mázsa",
         "Buda (-13th c.)", "mass", 54.018)
    # Based on Bogdán 1991.

    # Buda (14th century-1686)
    # Name collision avoided with invisible character U+1D174 at the end of self.name.
    Unit("budai lat𝅴", "1/32 font", "lat",
         "Buda (14th c.-1686)", "mass", 0.015347)
    Unit("budai nehezék𝅴", "2 lat", "neh.",
         "Buda (14th c.-1686)", "mass", 0.030694)
    Unit("budai ferton𝅴", "jel. \"negyed\" (márka),\n1/16 font\n2 neh.", "fert.",
         "Buda (14th c.-1686)", "mass", 0.061388)
    Unit("budai font𝅴", "16 fert.", "font",
         "Buda (14th c.-1686)", "mass", 0.4811)
    Unit("budai mázsa (100 font)𝅴", "váltószáma bizonytalan\n100 fontos érték", "mázsa",
         "Buda (14th c.-1686)", "mass", 49.11)
    Unit("budai mázsa (120 font)𝅴", "váltószáma bizonytalan\n120 fontos érték", "mázsa",
         "Buda (14th c.-1686)", "mass", 58.93)
    # Based on Bogdán 1991, 50.

    # Pressburg (-1854)
    # Name collision avoided with invisible character U+1D173 at the end of self.name.
    Unit("pozsonyi lat𝅳", "1/32 font", "lat",
         "Pressburg (-1854)", "mass", 0.017437)
    Unit("pozsonyi nehezék𝅳", "2 lat", "neh.",
         "Pressburg (-1854)", "mass", 0.034875)
    Unit("pozsonyi font𝅳", "16 neh.", "font",
         "Pressburg (-1854)", "mass", 0.5580)
    Unit("pozsonyi mázsa𝅳", "100 font", "mázsa",
         "Pressburg (-1854)", "mass", 55.80)
    # Based on Bogdán 1991, 52.

    # Pressburg (1854-1874)
    # Name collision avoided with invisible character U+1D174 at the end of self.name.
    Unit("pozsonyi lat𝅴", "1/32 font\na bécsihez igazítva", "lat",
         "Pressburg (1854-1874)", "mass", 0.0175018)
    Unit("pozsonyi nehezék𝅴", "2 lat\na bécsihez igazítva", "neh.",
         "Pressburg (1854-1874)", "mass", 0.035003)
    Unit("pozsonyi font𝅴", "16 neh.\na bécsihez igazítva", "font",
         "Pressburg (1854-1874)", "mass", 0.56)
    Unit("pozsonyi mázsa𝅴", "100 font\na bécsihez igazítva", "mázsa",
         "Pressburg (1854-1874)", "mass", 56)
    # Based on Bogdán 1991, 52.

    # Hungarian (16-18th century)
    Unit("magyar lat", "ném. Lot szóból\n1/120 font", "lat",
         "Hungarian (16-18th c.)", "mass", 0.015312)
    Unit("magyar font", "lat. pondus szóból\n32 lat", "font",
         "Hungarian (16-18th c.)", "mass", 0.49)
    Unit("magyar mázsa", "lat. massa szóból\n120 font", "mázsa",
         "Hungarian (16-18th c.)", "mass", 58.80)
    # Based on Bogdán 1991, 52.

    # Transylvanian (mid 1680s - mid 1690s)
    # Name collision avoided with invisible character U+1D173 at the end of self.name.
    Unit("erdélyi lat𝅳", "1/144 font", "lat",
         "Transylvanian (mid1680s-mid1690s)", "mass", 0.019475)
    Unit("erdélyi font𝅳", "20 lat", "font",
         "Transylvanian (mid1680s-mid1690s)", "mass", 0.3895)
    Unit("erdélyi mázsa𝅳", "144 font", "mázsa",
         "Transylvanian (mid1680s-mid1690s)", "mass", 56.09)
    # Based on Bogdán 1991, 51.

    # Transylvanian (mid 1690s - 1721)
    # Name collision avoided with invisible character U+1D174 at the end of self.name.
    Unit("erdélyi lat𝅴", "1/144 font", "lat",
         "Transylvanian (mid1690s-1721)", "mass", 0.014028)
    Unit("erdélyi font𝅴", "32 lat", "font",
         "Transylvanian (mid1690s-1721)", "mass", 0.4489)
    Unit("erdélyi mázsa𝅴", "144 font", "mázsa",
         "Transylvanian (mid1690s-1721)", "mass", 64.64)
    # Based on Bogdán 1991, 51.

    # Transylvanian (1721-1874)
    # Name collision avoided with invisible character U+1D175 at the end of self.name.
    Unit("erdélyi lat𝅵", "1/100 font", "lat",
         "Transylvanian (1721-1874)", "mass", 0.0175)
    Unit("erdélyi font𝅵", "32 lat", "font",
         "Transylvanian (1721-1874)", "mass", 0.56)
    Unit("erdélyi mázsa𝅵", "100 font", "mázsa",
         "Transylvanian (1721-1874)", "mass", 56.00)
    # Based on Bogdán 1991, 51.

    # Turkish (Hungary)
    Unit("drám", "a drachma szóból", "dram",
         "Turkish", "mass", 0.0031503)
    Unit("litra", "török libra\n100 drám\n18 bécsi lat", "lit.",
         "Turkish", "mass", 0.3150)
    Unit("oka", "4 lit.\n2 1/4 bécsi font", "oka",
         "Turkish", "mass", 1.26)
    Unit("kantár", "44 oka", "kant.",
         "Turkish", "mass", 55.44)
    # Based on Bogdán 1991, 52.
    return
