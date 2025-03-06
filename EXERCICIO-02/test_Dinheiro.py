
import unittest

from dinheiro import Dinheiro, Moeda

class TestDinheiroMethods(unittest.TestCase):

    # 15
    def test_zero(self):
        # INLINE FIXTURE SETUP
        zero = Dinheiro(Moeda.BRL, 0, 0)
        # EXERCISE SUT
        isZero = zero.zero()
        # RESULT VERIFICATION
        self.assertEqual(True, isZero)

    # 16
    def test_formatar_sem_zero_cem_reais_dez_centavos(self):
        # INLINE FIXTURE SETUP
        dinheiro = Dinheiro(Moeda.BRL, 100, 10)
        # EXERCISE SUT
        quantia_formatada_sem_zero = dinheiro.formatar_sem_moeda()
        # RESULT VERIFICATION
        self.assertEqual("100,10", quantia_formatada_sem_zero)
        # TEARDOWN   

    # 17
    def test_formatar_com_zero_cem_reais_dez_centavos(self):
        # INLINE FIXTURE SETUP
        dinheiro = Dinheiro(Moeda.BRL, 100, 10)
        # EXERCISE SUT
        quantia_formatada_com_zero = dinheiro.formatar_com_moeda()
        # RESULT VERIFICATION
        self.assertEqual("100,10 BRL", quantia_formatada_com_zero)
        # TEARDOWN

    # 18
    def test_positivo_de_dez_reais (self):
        # INLINE FIXTURE SETUP
        dez_reais = Dinheiro(Moeda.BRL, 10, 0)
        # EXERCISE SUT
        valor_dez_positivo = dez_reais.positivo() #retorna um valor monetario
        # RESULT VERIFICATION
        self.assertTrue(valor_dez_positivo.formatar_positivo())
        self.assertEqual(1000, int(valor_dez_positivo.obter_quantia().obter_quantia_em_escala()))     


if __name__ == '__main__':
    unittest.main()