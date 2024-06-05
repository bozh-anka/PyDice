import unittest
from DiceFunctions import check_type


class TestDiceFunctions(unittest.TestCase):
    def test_check_type(self):
        psix = ["6", "Positive"]
        nsix = ["6", "Negative"]
        peight = ["8", "Positive"]
        neight = ["8", "Negative"]
        ptwelve = ["12", "Positive"]
        ntwelve = ["12", "Negative"]
        btest = ["13", "Toodaloo"]

        self.assertEqual(check_type(psix), "psix")
        self.assertEqual(check_type(nsix), "nsix")
        self.assertEqual(check_type(peight), "peight")
        self.assertEqual(check_type(neight), "neight")
        self.assertEqual(check_type(ptwelve), "ptwelve")
        self.assertEqual(check_type(ntwelve), "ntwelve")
        self.assertEqual(check_type(btest), "Wrong input")
