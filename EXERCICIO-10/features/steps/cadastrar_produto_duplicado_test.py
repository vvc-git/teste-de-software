from behave import *
from src.mercado_leilao import MercadoLeilao

@given('o cadastro do usuario Ernani Cesar foi realizado')
def step_impl(context):
    context.mercado = MercadoLeilao()
    context.mercado.cadastra_usuario(
        "Ernani Cesar",
        "Endereço Exemplo",
        "ernani@email.com",
        "055.761.919-00"
    )

@given('o nome do produto {nome_produto}')
def step_impl(context, nome_produto):
    context.nome_produto = nome_produto

@given('a descricao do produto {descricao}')
def step_impl(context, descricao):
    context.descricao = descricao

@given('e o lance {lance}')
def step_impl(context, lance):
    context.lance = float(lance)

@given('e o cpf do leiloador {cpf}')
def step_impl(context, cpf):
    context.cpf_leiloador = cpf

@when('cadastrar o produto')
def step_impl(context):
    try:
        context.mercado.cadastra_produto(context.nome_produto, context.descricao, context.lance, context.cpf_leiloador, 12)
    except Exception as e:
        context.mensagem = "O produto ja existe ou o leiloador nao esta cadastrado."

@given('{nome_produto} {descricao} ja foi cadastrado')
def step_impl(context, nome_produto, descricao):
    context.mercado.cadastra_produto(nome_produto, descricao, 1000, "055.761.919-00", 12)

@then('o sistema cadastra com sucesso')
def step_impl(context):
    assert context.mercado.possui_produto() == True

@then('o sistema mostra a mensagem {mensagem_esperada}')
def step_impl(context, mensagem_esperada):
    assert context.mensagem == mensagem_esperada