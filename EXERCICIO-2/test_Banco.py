import unittest
from banco import Banco
from dinheiro import Moeda
from agencia import Agencia

class TestBanco(unittest.TestCase):

    def setUp(self):
        #  FIXTURE SETUP
        self.nome = "Itaú"
        self.moeda = Moeda.BRL
        self.banco = Banco(self.nome, self.moeda)

    # 6
    def test_get_nome(self):
        # IMPLICIT FIXTURE SETUP
        # EXERCISE SUT
        nome = self.banco.nome
        # RESULT VERIFICATION
        self.assertEqual(nome, self.nome)
    # 7
    def test_get_moeda(self):
        # IMPLICIT FIXTURE SETUP
        # EXERCISE SUT
        moeda = self.banco.moeda
        # RESULT VERIFICATION
        self.assertEqual(moeda, self.moeda)

    # 8
    def test_criar_agencia(self):
        # IMPLICIT FIXTURE SETUP
        # INLINE FIXTURE SETUP
        nome = "Carvoeira"
        # EXERCISE SUT
        agencia = self.banco.criar_agencia(nome)
        # RESULT VERIFICATION
        self.assertTrue(isinstance(agencia, Agencia))
        self.assertTrue(agencia.nome, nome)
    # 9
    def test_obter_agencias(self):
        # IMPLICIT FIXTURE SETUP
        # INLINE FIXTURE SETUP
        nome = "Carvoeira"
        self.banco.criar_agencia(nome)
        # EXERCISE SUT
        agencias = self.banco.obter_agencias()
        # RESULT VERIFICATION
        self.assertTrue(agencias)
    # 10
    def test_obter_agencias_com_3_agencias(self):
        # IMPLICIT FIXTURE SETUP
        # INLINE FIXTURE SETUP
        self.banco.criar_agencia("Carvoeira")
        self.banco.criar_agencia("Pantanal")
        self.banco.criar_agencia("Itacorubi")
        # EXERCISE SUT
        agencias = self.banco.obter_agencias()
        # RESULT VERIFICATION
        self.assertTrue(len(agencias) == 3)

    # 11
    def test_obter_agencias_com_0_agencias(self):
        # IMPLICIT FIXTURE SETUP
        # EXERCISE SUT
        agencias = self.banco.obter_agencias()
        # RESULT VERIFICATION
        self.assertFalse(agencias)
    # 12
    def test_obter_agencia(self):
        # IMPLICIT FIXTURE SETUP
        # INLINE FIXTURE SETUP
        nome = "Carvoeira"
        self.banco.criar_agencia(nome)
        # EXERCISE SUT
        agencia = self.banco.obter_agencia(nome)
        # RESULT VERIFICATION
        self.assertTrue(agencia)

    # 13
    def test_obter_agencia_com_nome_inexistente(self):
        # IMPLICIT FIXTURE SETUP
        # INLINE FIXTURE SETUP
        nome = "Carvoeira"
        self.banco.criar_agencia(nome)
        outroNome = "Trindade"
        # EXERCISE SUT
        agencia = self.banco.obter_agencia(outroNome)
        # RESULT VERIFICATION
        self.assertFalse(agencia)

if __name__ == '__main__':
    unittest.main()