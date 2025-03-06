
import unittest

from conta import Conta

class TestContaMethods(unittest.TestCase):

    def setUp(self):
        self.Conta = Conta("Edu", 1000, "Santander")

    # 14
    def test_identificador_valido(self):
        # IMPLICIT FIXTURE SETUP
        # EXERCISE SUT
        identificador = self.Conta.obter_identificador()
        # RESULT VERIFICATION
        self.assertEqual("1000-3", identificador)
        # Fixture Teardown
    

if __name__ == '__main__':
    unittest.main()