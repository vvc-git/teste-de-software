import datetime
import unittest

# SUT (System under test): O que está sendo testado. No teste de unidade é uma classe ou um método.
# Fixture: O que é necessário para o teste.

class TestDateMethods(unittest.TestCase):
    def test_cria_data_natal_2023(self):
        # Fixture Setup
        # Exercise SUT
        natal_2023 = datetime.date(2023, 12, 25)
        # Result Verification
        self.assertEqual(2023, natal_2023.year)
        self.assertEqual(12, natal_2023.month)
        self.assertEqual(25, natal_2023.day)
        # Fixture Teardown


    def test_cria_data_dia_negativo_invalido(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError):
            data_invalida = datetime.date(2024, 3, -1)
        # Result Verification
        # Fixture Teardown


    def test_cria_data_de_ano_bissexto_invalido(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError):
            dia_29_fevereiro = datetime.date(2023, 2, 29)
        # Result Verification
        # Fixture Teardown

if __name__ == '__main__':
    unittest.main()