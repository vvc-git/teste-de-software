# flake8: noqa
# pylint: disable-all

import unittest
import datetime
from unittest.mock import MagicMock
from src.mercado_leilao import MercadoLeilao


class TestDaLance(unittest.TestCase):

    def setUp(self):
        self.mercado = MercadoLeilao()

        self.mercado.is_cpf = MagicMock(return_value=True)

        self.cpf_leiloador = "123.456.789-00"
        self.cpf_comprador1 = "123.456.789-01"
        self.cpf_comprador2 = "123.456.789-02"

        self.mercado.cadastra_usuario(
            "João Leiloador", "Rua A, 123", "joao@email.com", self.cpf_leiloador
        )
        self.mercado.cadastra_usuario(
            "Maria Compradora", "Rua B, 456", "maria@email.com", self.cpf_comprador1
        )
        self.mercado.cadastra_usuario(
            "Maria Compradora", "Rua B, 456", "maria@email.com", self.cpf_comprador2
        )

        today = datetime.date.today()
        future_date = today + datetime.timedelta(days=5)

        self.data_hoje = int(today.strftime("%Y%m%d"))
        self.data_limite = int(future_date.strftime("%Y%m%d"))

        self.nome_produto = "Smartphone Samsung"
        self.descricao_produto = "Smartphone em ótimo estado"
        self.lance_minimo = 100.0

        self.mercado.cadastra_produto(
            self.nome_produto,
            self.descricao_produto,
            self.lance_minimo,
            self.cpf_leiloador,
            self.data_limite,
        )

    def test_da_lance_sucesso_primeiro_lance(self):
        valor_lance = 150.0

        self.mercado.da_lance(
            self.nome_produto, self.cpf_comprador1, valor_lance, self.data_hoje
        )

        produtos = self.mercado.get_produtos_em_leilao(self.data_hoje)
        produto = produtos[0]

        self.assertEqual(len(produto.lances_efetuados), 1)
        self.assertEqual(produto.lances_efetuados[0].valor, valor_lance)
        self.assertEqual(produto.lances_efetuados[0].dono.cpf, self.cpf_comprador1)
        self.assertEqual(produto.lances_efetuados[0].produto, produto)

    def test_da_lance_valor_igual_ao_minimo(self):
        valor_lance = 100.0

        self.mercado.da_lance(
            self.nome_produto, self.cpf_comprador1, valor_lance, self.data_hoje
        )

        produtos = self.mercado.get_produtos_em_leilao(self.data_hoje)
        produto = produtos[0]

        self.assertEqual(len(produto.lances_efetuados), 1)
        self.assertEqual(produto.lances_efetuados[0].valor, valor_lance)

    def test_da_lance_falha_valor_menor_que_minimo(self):
        valor_lance = 50.0

        with self.assertRaises(Exception) as context:
            self.mercado.da_lance(
                self.nome_produto, self.cpf_comprador1, valor_lance, self.data_hoje
            )

        self.assertEqual(
            str(context.exception),
            "O valor do lance eh inferior ao necessario ou o comprador nao esta cadastrado.",
        )

    def test_da_lance_falha_valor_menor_ao_atual(self):
        self.mercado.da_lance(
            self.nome_produto, self.cpf_comprador1, 150.0, self.data_hoje
        )

        with self.assertRaises(Exception) as context:
            self.mercado.da_lance(
                self.nome_produto, self.cpf_comprador1, 140.0, self.data_hoje
            )

        self.assertEqual(
            str(context.exception),
            "O valor do lance eh inferior ao necessario ou o comprador nao esta cadastrado.",
        )

    def test_da_lance_falha_valor_igual_ao_atual(self):
        self.mercado.da_lance(
            self.nome_produto, self.cpf_comprador1, 150.0, self.data_hoje
        )

        with self.assertRaises(Exception) as context:
            self.mercado.da_lance(
                self.nome_produto, self.cpf_comprador1, 150.0, self.data_hoje
            )

        self.assertEqual(
            str(context.exception),
            "O valor do lance eh inferior ao necessario ou o comprador nao esta cadastrado.",
        )