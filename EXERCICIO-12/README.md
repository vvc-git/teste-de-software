# Para rodar os testes: 

Minha versão:
 ```
PYTHONPATH=./src python3 -m unittest testes.test_da_lance
 ```


Versão IA:

```
PYTHONPATH=./src python3 -m unittest testes.test_da_lance_IA
```


## Exercício - Parte 2:

Especifique testes de unidade usando a IA generativa Claude.ai (https://claude.ai/). Peça a
geração de testes de unidade para o método da_lance da classe MercadoLeilao.

**2.1 - Descreva o prompt inicial utilizado. Caso uma outra IA tenha sido utilizada, indique-a.**

> Crie testes de unidade para da_lance em mercado_leilao

(Com os arquivos anexados)

**2.2 - Inclua os testes gerados inicialmente pela IA.**

```python

import unittest
from datetime import date
from mercado_leilao import MercadoLeilao
from usuario import Usuario
from produto_leilao import ProdutoLeilao
from lance import Lance

class TestDaLance(unittest.TestCase):

    def test_da_lance_com_sucesso_sem_lances_anteriores(self):
        # Cenário: Produto em leilão sem lances anteriores
        mercado = MercadoLeilao()
        
        # Criação e cadastro do leiloador
        leiloador_cpf = "111.111.111-11"
        mercado.cadastra_usuario("Leiloador", "Rua A", "leiloador@email.com", leiloador_cpf)
        
        # Criação e cadastro do comprador
        comprador_cpf = "222.222.222-22"
        mercado.cadastra_usuario("Comprador", "Rua B", "comprador@email.com", comprador_cpf)
        
        # Cadastro do produto em leilão
        nome_produto = "Celular XYZ"
        data_limite = date(2025, 12, 31)
        mercado.cadastra_produto(nome_produto, "Descrição do celular", 500.00, leiloador_cpf, data_limite)
        
        # Execução do método a ser testado
        valor_lance = 600.00
        data_hoje = date(2025, 6, 1)
        mercado.da_lance(nome_produto, comprador_cpf, valor_lance, data_hoje)
        
        # Verificação do resultado
        produtos_em_leilao = mercado.get_produtos_em_leilao(data_hoje)
        self.assertEqual(len(produtos_em_leilao), 1)
        
        produto = produtos_em_leilao[0]
        self.assertEqual(len(produto.lances_efetuados), 1)
        self.assertEqual(produto.get_valor_ultimo_lance(), valor_lance)
        self.assertEqual(produto.lances_efetuados[0].dono.cpf, comprador_cpf)

    def test_da_lance_com_sucesso_com_lances_anteriores(self):
        # Cenário: Produto em leilão com lances anteriores
        mercado = MercadoLeilao()
        
        # Criação e cadastro do leiloador
        leiloador_cpf = "111.111.111-11"
        mercado.cadastra_usuario("Leiloador", "Rua A", "leiloador@email.com", leiloador_cpf)
        
        # Criação e cadastro dos compradores
        comprador1_cpf = "222.222.222-22"
        mercado.cadastra_usuario("Comprador 1", "Rua B", "comprador1@email.com", comprador1_cpf)
        
        comprador2_cpf = "333.333.333-33"
        mercado.cadastra_usuario("Comprador 2", "Rua C", "comprador2@email.com", comprador2_cpf)
        
        # Cadastro do produto em leilão
        nome_produto = "Geladeira X"
        data_limite = date(2025, 12, 31)
        mercado.cadastra_produto(nome_produto, "Descrição da geladeira", 1000.00, leiloador_cpf, data_limite)
        
        data_hoje = date(2025, 6, 1)

        # Primeiro lance
        mercado.da_lance(nome_produto, comprador1_cpf, 1100.00, data_hoje)
        
        # Execução do método a ser testado (segundo lance)
        valor_lance = 1200.00
        mercado.da_lance(nome_produto, comprador2_cpf, valor_lance, data_hoje)
        
        # Verificação do resultado
        produtos_em_leilao = mercado.get_produtos_em_leilao(data_hoje)
        self.assertEqual(len(produtos_em_leilao), 1)
        
        produto = produtos_em_leilao[0]
        self.assertEqual(len(produto.lances_efetuados), 2)
        self.assertEqual(produto.get_valor_ultimo_lance(), valor_lance)
        self.assertEqual(produto.lances_efetuados[1].dono.cpf, comprador2_cpf)

    def test_da_lance_com_valor_inferior_ao_minimo(self):
        # Cenário: Lance com valor inferior ao lance mínimo
        mercado = MercadoLeilao()
        
        # Criação e cadastro do leiloador
        leiloador_cpf = "111.111.111-11"
        mercado.cadastra_usuario("Leiloador", "Rua A", "leiloador@email.com", leiloador_cpf)
        
        # Criação e cadastro do comprador
        comprador_cpf = "222.222.222-22"
        mercado.cadastra_usuario("Comprador", "Rua B", "comprador@email.com", comprador_cpf)
        
        # Cadastro do produto em leilão
        nome_produto = "Livro Fantasia"
        data_limite = date(2025, 12, 31)
        mercado.cadastra_produto(nome_produto, "Descrição do livro", 50.00, leiloador_cpf, data_limite)
        
        # Execução do método a ser testado e verificação da exceção
        valor_lance = 40.00  # Menor que o lance mínimo
        data_hoje = date(2025, 6, 1)
        with self.assertRaisesRegex(Exception, "O valor do lance eh inferior ao necessario ou o comprador nao esta cadastrado."):
            mercado.da_lance(nome_produto, comprador_cpf, valor_lance, data_hoje)
        
        # Verificação de que nenhum lance foi adicionado
        produtos_em_leilao = mercado.get_produtos_em_leilao(data_hoje)
        produto = produtos_em_leilao[0]
        self.assertEqual(len(produto.lances_efetuados), 0)


    def test_da_lance_para_comprador_nao_cadastrado(self):
        # Cenário: Comprador não cadastrado
        mercado = MercadoLeilao()
        
        # Criação e cadastro do leiloador
        leiloador_cpf = "111.111.111-11"
        mercado.cadastra_usuario("Leiloador", "Rua A", "leiloador@email.com", leiloador_cpf)
        
        # Cadastro do produto em leilão
        nome_produto = "Carro Antigo"
        data_limite = date(2025, 12, 31)
        mercado.cadastra_produto(nome_produto, "Descrição do carro", 10000.00, leiloador_cpf, data_limite)
        
        # Execução do método a ser testado e verificação da exceção
        comprador_cpf_nao_cadastrado = "999.999.999-99"
        valor_lance = 11000.00
        data_hoje = date(2025, 6, 1)
        with self.assertRaisesRegex(Exception, "O usuario nao esta cadastrado."):
            mercado.da_lance(nome_produto, comprador_cpf_nao_cadastrado, valor_lance, data_hoje)
        
        # Verificação de que nenhum lance foi adicionado
        produtos_em_leilao = mercado.get_produtos_em_leilao(data_hoje)
        produto = produtos_em_leilao[0]
        self.assertEqual(len(produto.lances_efetuados), 0)

    def test_da_lance_para_produto_nao_existente(self):
        # Cenário: Produto não existe no leilão
        mercado = MercadoLeilao()
        
        # Criação e cadastro do comprador
        comprador_cpf = "222.222.222-22"
        mercado.cadastra_usuario("Comprador", "Rua B", "comprador@email.com", comprador_cpf)
        
        # Execução do método a ser testado e verificação da exceção
        nome_produto_nao_existente = "Moto Velocidade"
        valor_lance = 5000.00
        data_hoje = date(2025, 6, 1)
        with self.assertRaisesRegex(Exception, "Nao existe produto cadastrado com esse nome."):
            mercado.da_lance(nome_produto_nao_existente, comprador_cpf, valor_lance, data_hoje)
        
        # Verificação de que não há produtos em leilão
        self.assertEqual(len(mercado.get_produtos_em_leilao(data_hoje)), 0)
        
    def test_da_lance_com_produto_expirado_e_nao_vendido(self):
        # Cenário: Tentar dar lance em produto expirado e não vendido
        mercado = MercadoLeilao()

        leiloador_cpf = "111.111.111-11"
        mercado.cadastra_usuario("Leiloador", "Rua A", "leiloador@email.com", leiloador_cpf)
        
        comprador_cpf = "222.222.222-22"
        mercado.cadastra_usuario("Comprador", "Rua B", "comprador@email.com", comprador_cpf)
        
        nome_produto = "Objeto Antigo"
        data_limite = date(2024, 1, 1)  # Data limite no passado
        mercado.cadastra_produto(nome_produto, "Descrição", 100.00, leiloador_cpf, data_limite)
        
        data_hoje = date(2025, 6, 1) # Data atual após a expiração

        # Chama __atualiza_lista_de_produtos para mover o produto para vencidos_e_nao_vendidos
        mercado.get_produtos_em_leilao(data_hoje) 

        with self.assertRaisesRegex(Exception, "Nao existe produto cadastrado com esse nome."):
            mercado.da_lance(nome_produto, comprador_cpf, 150.00, data_hoje)

        self.assertEqual(len(mercado.get_produtos_vencidos_e_nao_vendidos(data_hoje)), 1)
        self.assertEqual(len(mercado.get_produtos_em_leilao(data_hoje)), 0)

    def test_da_lance_com_produto_expirado_e_vendido(self):
        # Cenário: Tentar dar lance em produto expirado e já vendido
        mercado = MercadoLeilao()

        leiloador_cpf = "111.111.111-11"
        mercado.cadastra_usuario("Leiloador", "Rua A", "leiloador@email.com", leiloador_cpf)
        
        comprador1_cpf = "222.222.222-22"
        mercado.cadastra_usuario("Comprador 1", "Rua B", "comprador1@email.com", comprador1_cpf)

        comprador2_cpf = "333.333.333-33"
        mercado.cadastra_usuario("Comprador 2", "Rua C", "comprador2@email.com", comprador2_cpf)
        
        nome_produto = "Joia Rara"
        data_limite = date(2024, 1, 1)  # Data limite no passado
        mercado.cadastra_produto(nome_produto, "Descrição", 1000.00, leiloador_cpf, data_limite)
        
        data_inicial_lance = date(2023, 12, 1)
        mercado.da_lance(nome_produto, comprador1_cpf, 1200.00, data_inicial_lance)

        data_hoje = date(2025, 6, 1) # Data atual após a expiração

        # Chama __atualiza_lista_de_produtos para mover o produto para vendidos
        mercado.get_produtos_em_leilao(data_hoje)

        with self.assertRaisesRegex(Exception, "Nao existe produto cadastrado com esse nome."):
            mercado.da_lance(nome_produto, comprador2_cpf, 1500.00, data_hoje)
        
        self.assertEqual(len(mercado.get_produtos_vendidos(data_hoje)), 1)
        self.assertEqual(len(mercado.get_produtos_em_leilao(data_hoje)), 0)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)



```

**2.3 - Indique quantas iterações de prompt foram necessárias para que os testes fossem gerados da maneira esperada. Caso tenha sido necessário mais de uma iteração de prompt, inclua a descrição de cada novo prompt e os testes gerados no final.**

Mais 1 iteração:

> Utilize setUp para evitar inicializações repetitivas e mock para is_cpf

```python

import unittest
from datetime import date
from unittest.mock import patch

# Importa as classes necessárias do seu projeto
from mercado_leilao import MercadoLeilao
from usuario import Usuario
from produto_leilao import ProdutoLeilao
from lance import Lance

class TestDaLance(unittest.TestCase):

    def setUp(self):
        """
        Configura o ambiente para cada teste.
        Cria uma nova instância de MercadoLeilao e usuários comuns.
        Mocka o método is_cpf para sempre retornar True, simulando CPFs válidos.
        """
        self.mercado = MercadoLeilao()

        # Configura o mock para is_cpf. Ele será iniciado antes de cada teste e parado depois.
        # Por padrão, is_cpf retornará True para simular CPFs válidos.
        self.patcher_is_cpf = patch('mercado_leilao.MercadoLeilao.is_cpf', return_value=True)
        self.mock_is_cpf = self.patcher_is_cpf.start()

        # Dados para o leiloador
        self.leiloador_cpf = "111.111.111-11"
        self.leiloador_nome = "Leiloador Teste"
        self.leiloador_endereco = "Rua do Leilão, 10"
        self.leiloador_email = "leiloador@test.com"
        self.mercado.cadastra_usuario(self.leiloador_nome, self.leiloador_endereco, self.leiloador_email, self.leiloador_cpf)

        # Dados para o comprador 1
        self.comprador1_cpf = "222.222.222-22"
        self.comprador1_nome = "Comprador Um"
        self.comprador1_endereco = "Avenida Principal, 200"
        self.comprador1_email = "comprador1@test.com"
        self.mercado.cadastra_usuario(self.comprador1_nome, self.comprador1_endereco, self.comprador1_email, self.comprador1_cpf)

        # Dados para o comprador 2 (usado em alguns testes)
        self.comprador2_cpf = "333.333.333-33"
        self.comprador2_nome = "Comprador Dois"
        self.comprador2_endereco = "Travessa Secundária, 30"
        self.comprador2_email = "comprador2@test.com"
        self.mercado.cadastra_usuario(self.comprador2_nome, self.comprador2_endereco, self.comprador2_email, self.comprador2_cpf)

        self.data_hoje = date(2025, 6, 1) # Data base para os testes

    def tearDown(self):
        """
        Limpa o ambiente após cada teste, parando o mock de is_cpf.
        """
        self.patcher_is_cpf.stop()

    def test_da_lance_com_sucesso_sem_lances_anteriores(self):
        """
        Testa o cenário onde um lance é dado com sucesso em um produto
        que não tinha lances anteriores.
        """
        # Cadastro do produto em leilão
        nome_produto = "Celular XYZ"
        data_limite = date(2025, 12, 31)
        self.mercado.cadastra_produto(nome_produto, "Descrição do celular", 500.00, self.leiloador_cpf, data_limite)
        
        # Execução do método a ser testado
        valor_lance = 600.00
        self.mercado.da_lance(nome_produto, self.comprador1_cpf, valor_lance, self.data_hoje)
        
        # Verificação do resultado
        produtos_em_leilao = self.mercado.get_produtos_em_leilao(self.data_hoje)
        self.assertEqual(len(produtos_em_leilao), 1)
        
        produto = produtos_em_leilao[0]
        self.assertEqual(len(produto.lances_efetuados), 1)
        self.assertEqual(produto.get_valor_ultimo_lance(), valor_lance)
        self.assertEqual(produto.lances_efetuados[0].dono.cpf, self.comprador1_cpf)
        # Verifica se is_cpf foi chamado para os usuários cadastrados
        self.assertEqual(self.mock_is_cpf.call_count, 3) # Leiloador + Comprador1 + Comprador2

    def test_da_lance_com_sucesso_com_lances_anteriores(self):
        """
        Testa a adição de um novo lance em um produto que já possuía lances,
        garantindo que o novo lance é maior.
        """
        # Cadastro do produto em leilão
        nome_produto = "Geladeira X"
        data_limite = date(2025, 12, 31)
        self.mercado.cadastra_produto(nome_produto, "Descrição da geladeira", 1000.00, self.leiloador_cpf, data_limite)
        
        # Primeiro lance
        self.mercado.da_lance(nome_produto, self.comprador1_cpf, 1100.00, self.data_hoje)
        
        # Execução do método a ser testado (segundo lance)
        valor_lance = 1200.00
        self.mercado.da_lance(nome_produto, self.comprador2_cpf, valor_lance, self.data_hoje)
        
        # Verificação do resultado
        produtos_em_leilao = self.mercado.get_produtos_em_leilao(self.data_hoje)
        self.assertEqual(len(produtos_em_leilao), 1)
        
        produto = produtos_em_leilao[0]
        self.assertEqual(len(produto.lances_efetuados), 2)
        self.assertEqual(produto.get_valor_ultimo_lance(), valor_lance)
        self.assertEqual(produto.lances_efetuados[1].dono.cpf, self.comprador2_cpf)
        self.assertEqual(self.mock_is_cpf.call_count, 3) # Ainda 3 chamadas do setup

    def test_da_lance_com_valor_inferior_ao_minimo(self):
        """
        Verifica se uma exceção é levantada e nenhum lance é adicionado
        se o valor do lance for menor que o lance mínimo do produto.
        """
        # Cadastro do produto em leilão
        nome_produto = "Livro Fantasia"
        data_limite = date(2025, 12, 31)
        self.mercado.cadastra_produto(nome_produto, "Descrição do livro", 50.00, self.leiloador_cpf, data_limite)
        
        # Execução do método a ser testado e verificação da exceção
        valor_lance = 40.00  # Menor que o lance mínimo
        with self.assertRaisesRegex(Exception, "O valor do lance eh inferior ao necessario ou o comprador nao esta cadastrado."):
            self.mercado.da_lance(nome_produto, self.comprador1_cpf, valor_lance, self.data_hoje)
        
        # Verificação de que nenhum lance foi adicionado
        produtos_em_leilao = self.mercado.get_produtos_em_leilao(self.data_hoje)
        produto = produtos_em_leilao[0]
        self.assertEqual(len(produto.lances_efetuados), 0)
        self.assertEqual(self.mock_is_cpf.call_count, 3)

    def test_da_lance_para_comprador_nao_cadastrado(self):
        """
        Assegura que uma exceção é levantada se o comprador que tenta dar o lance
        não estiver cadastrado no sistema.
        """
        # Cadastro do produto em leilão
        nome_produto = "Carro Antigo"
        data_limite = date(2025, 12, 31)
        self.mercado.cadastra_produto(nome_produto, "Descrição do carro", 10000.00, self.leiloador_cpf, data_limite)
        
        # Execução do método a ser testado e verificação da exceção
        comprador_cpf_nao_cadastrado = "999.999.999-99"
        valor_lance = 11000.00
        with self.assertRaisesRegex(Exception, "O usuario nao esta cadastrado."):
            self.mercado.da_lance(nome_produto, comprador_cpf_nao_cadastrado, valor_lance, self.data_hoje)
        
        # Verificação de que nenhum lance foi adicionado
        produtos_em_leilao = self.mercado.get_produtos_em_leilao(self.data_hoje)
        produto = produtos_em_leilao[0]
        self.assertEqual(len(produto.lances_efetuados), 0)
        self.assertEqual(self.mock_is_cpf.call_count, 3)

    def test_da_lance_para_produto_nao_existente(self):
        """
        Confirma que uma exceção é levantada se o produto para o qual
        o lance está sendo dado não existir na lista de produtos em leilão.
        """
        # Execução do método a ser testado e verificação da exceção
        nome_produto_nao_existente = "Moto Velocidade"
        valor_lance = 5000.00
        with self.assertRaisesRegex(Exception, "Nao existe produto cadastrado com esse nome."):
            self.mercado.da_lance(nome_produto_nao_existente, self.comprador1_cpf, valor_lance, self.data_hoje)
        
        # Verificação de que não há produtos em leilão
        self.assertEqual(len(self.mercado.get_produtos_em_leilao(self.data_hoje)), 0)
        self.assertEqual(self.mock_is_cpf.call_count, 3)
        
    def test_da_lance_com_produto_expirado_e_nao_vendido(self):
        """
        Cenário: Tentar dar lance em produto expirado e não vendido.
        O comportamento de __atualiza_lista_de_produtos é testado aqui, não mockado.
        """
        nome_produto = "Objeto Antigo"
        data_limite = date(2024, 1, 1)  # Data limite no passado
        self.mercado.cadastra_produto(nome_produto, "Descrição", 100.00, self.leiloador_cpf, data_limite)
        
        # Chama __atualiza_lista_de_produtos para mover o produto para vencidos_e_nao_vendidos
        # Isso é feito indiretamente ao chamar get_produtos_em_leilao com a data atual
        self.mercado.get_produtos_em_leilao(self.data_hoje) 

        with self.assertRaisesRegex(Exception, "Nao existe produto cadastrado com esse nome."):
            self.mercado.da_lance(nome_produto, self.comprador1_cpf, 150.00, self.data_hoje)

        self.assertEqual(len(self.mercado.get_produtos_vencidos_e_nao_vendidos(self.data_hoje)), 1)
        self.assertEqual(len(self.mercado.get_produtos_em_leilao(self.data_hoje)), 0)
        self.assertEqual(self.mock_is_cpf.call_count, 3)

    def test_da_lance_com_produto_expirado_e_vendido(self):
        """
        Cenário: Tentar dar lance em produto expirado e já vendido.
        O comportamento de __atualiza_lista_de_produtos é testado aqui, não mockado.
        """
        nome_produto = "Joia Rara"
        data_limite = date(2024, 1, 1)  # Data limite no passado
        self.mercado.cadastra_produto(nome_produto, "Descrição", 1000.00, self.leiloador_cpf, data_limite)
        
        data_inicial_lance = date(2023, 12, 1)
        # O lance abaixo irá simular um cenário onde o produto é vendido antes da data limite
        self.mercado.da_lance(nome_produto, self.comprador1_cpf, 1200.00, data_inicial_lance)

        # Chama __atualiza_lista_de_produtos para mover o produto para vendidos
        # Isso é feito indiretamente ao chamar get_produtos_em_leilao com a data atual
        self.mercado.get_produtos_em_leilao(self.data_hoje)

        with self.assertRaisesRegex(Exception, "Nao existe produto cadastrado com esse nome."):
            self.mercado.da_lance(nome_produto, self.comprador2_cpf, 1500.00, self.data_hoje)
        
        self.assertEqual(len(self.mercado.get_produtos_vendidos(self.data_hoje)), 1)
        self.assertEqual(len(self.mercado.get_produtos_em_leilao(self.data_hoje)), 0)
        self.assertEqual(self.mock_is_cpf.call_count, 3)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)



```

Responda às seguintes perguntas:

**2.4 - Você acha que os testes gerados pela IA foram bem definidos? Você mudaria alguma coisa nestes testes para que eles ficassem mais bem especificados?**

Sim, eram bem definidos, o que foi bom de início. No entanto, observei que eram frequentemente redundantes, testando a mesma funcionalidade múltiplas vezes. Para otimizá-los, eu manteria a boa especificação, mas focaria em adicionar mais testes para cenários não cobertos, como condições de erro quando o lance é feito com um valor menor que o ultimo lance, em vez de replicar testes já existentes. 

**2.5 - Você acha que o seu conhecimento adquirido nesta disciplina sobre testes ajudou na definição de um prompt adequado? Como esse conhecimento foi aplicado no prompt?**

Sim, meu conhecimento em testes foi fundamental para distinguir entre testes eficazes e ineficazes. Isso me permitiu otimizar os resultados, solicitando à IA a geração de testes mais robustos e organizados — por exemplo, utilizando setUp para evitar repetições e aplicando mocks em cenários específicos, como na validação de CPF (`is_cpf`), onde a funcionalidade não era o foco do teste.

**2.6 - Você pretende, caso trabalhe com testes de software, utilizar a geração automática de testes? Por quê?**

Com certeza, é um bom ponto de partida, mas vem com algumas ressalvas importantes. Por exemplo, embora os testes estejam geralmente corretos, muitas vezes não validam os cenários mais importantes do sistema e acabam sendo repetitivos.


