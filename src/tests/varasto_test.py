import unittest
from varasto import Varasto

class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_negatiivinen_tilavuus(self):
        varasto = Varasto(-1)
        self.assertEqual(varasto.tilavuus, 0)

    def test_negatiivinen_alkusaldo(self):
        varasto = Varasto(10, -1)
        self.assertEqual(varasto.saldo, 0)
    
    def test_sopiva_alkusaldo(self):
        varasto = Varasto(10, 5)
        self.assertEqual(varasto.saldo, 5)

        varasto = Varasto(10, 12)
        self.assertEqual(varasto.saldo, 10)
    
    def test_negatiivinen_lisays(self):
        saldo = self.varasto.saldo

        self.varasto.lisaa_varastoon(-1)

        self.assertEqual(saldo, self.varasto.saldo)
    
    def test_sopiva_lisays(self):
        self.varasto.lisaa_varastoon(3)
        self.assertEqual(self.varasto.saldo, 3)

        self.varasto.lisaa_varastoon(10)
        self.assertEqual(self.varasto.tilavuus, self.varasto.saldo)
    
    def test_negatiivinen_otto(self):
        saldo = self.varasto.saldo
        self.varasto.ota_varastosta(-1)
        self.assertEqual(self.varasto.saldo, saldo)

    def test_sopiva_otto(self):
        self.varasto.lisaa_varastoon(8)
        saldo = self.varasto.saldo
        self.varasto.ota_varastosta(5)

        self.assertEqual(self.varasto.saldo, 3)
        self.assertEqual(self.varasto.ota_varastosta(5), 3)
        self.assertEqual(self.varasto.saldo, 0)

    def test_tulostus(self):
        self.varasto.lisaa_varastoon(3)
        self.assertEqual(str(self.varasto), "saldo = 3, vielä tilaa 7")