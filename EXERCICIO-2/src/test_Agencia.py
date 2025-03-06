import unittest
from agencia import Agencia  # Importando a classe Agencia

class TestAgencia(unittest.TestCase):

    def setUp(self):
        # Implicit Fixture Setup
        self.agencia = Agencia(nome="Agência Trindade", codigo=123, banco="Itau")

    # 1
    def test_agencia_inicializacao(self):
        # Implicit Fixture Setup
        # Exercise SUT
        # Result Verification
        self.assertEqual(self.agencia.nome, "Agência Trindade")
        self.assertEqual(self.agencia.banco, "Itau")
        self.assertEqual(self.agencia.obter_identificador(), "123")
        # Fixture Teardown

    # 2
    def test_criar_conta(self):
        # Implicit Fixture Setup
        # Exercise SUT
        conta1 = self.agencia.criar_conta("Paulo")
        conta2 = self.agencia.criar_conta("Ricardo")
        # Exercise SUT
        # Result Verification
        self.assertEqual(len(self.agencia.obter_contas()), 2)
        self.assertEqual(conta1.titular, "Paulo")
        self.assertEqual(conta2.titular, "Ricardo")
        self.assertEqual(conta1.obter_identificador(), "0001-5")
        self.assertEqual(conta2.obter_identificador(), "0002-7")
        # Fixture Teardown

    # 3    
    def test_obter_conta_valida(self):
        # Inline Fixture Setup
        # Implicit Fixture Setup
        conta1 = self.agencia.criar_conta("Paulo")
        # Exercise SUT
        conta = self.agencia.obter_conta("0001-5")
        # Result Verification
        self.assertIsNotNone(conta)
        self.assertEqual(conta.titular, "Paulo")
        # Fixture Teardown

    # 4 
    def test_obter_conta_invalida(self):
        # Inline Fixture Setup
        # Implicit Fixture Setup
        # Exercise SUT
        conta = self.agencia.obter_conta("999")
        # Result Verification
        self.assertIsNone(conta)
        # Fixture Teardown

    # 5
    def test_obter_contas(self):
        # Inline Fixture Setup
        # Implicit Fixture Setup
        conta1 = self.agencia.criar_conta("Paulo")
        conta2 = self.agencia.criar_conta("Ricardo")
        # Exercise SUT
        contas = self.agencia.obter_contas()
        # Verificar se a quantidade de contas está correta
        self.assertEqual(len(contas), 2)
        self.assertEqual(contas[0].titular, "Paulo")
        self.assertEqual(contas[1].titular, "Ricardo")
        # Fixture Teardown

if __name__ == "__main__":
    unittest.main()
