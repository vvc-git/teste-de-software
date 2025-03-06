from behave import *
from unittest import TestCase

from solcx import compile_standard, install_solc
import json
from web3 import Web3

address = "0xf386A3De954ED035DF1Dd1fC77ECb133986d81ce"
private_key = "0xda148e36e243278e8a2f66d6d75ee015323220b328d13a9e298eb2d3a12f5f9b"

smart_contract = None
w3 = None
chain_id = 1337

def __deploy_contract(landlord, tenant, tenantAddress, contractTotalValue, monthlyValue,
                        monthsQuantity, actualDay, dayToBeEffective):

    global smart_contract
    global w3

    # Endereço do diretório onde está o smart contract RentContract
    with open("/home/vvc/EXERCICIO-11/Implementation-SmartContract-Rent-Python-10-06-25 (3)/src/resources/RentContract.sol", "r") as file:
        smart_contract_file = file.read()
    _solc_version = "0.8.0"
    install_solc(_solc_version)
    # Considerando o smart contract RentContract
    compiled_sol = compile_standard({"language": "Solidity", "sources": {"RentContract.sol": {"content": smart_contract_file}},
            "settings": {"outputSelection": {"*": {"*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]} } }, },
            solc_version=_solc_version,)
    with open("compiled_code.json", "w") as file:
        json.dump(compiled_sol, file)
    bytecode = compiled_sol["contracts"]["RentContract.sol"]["RentContract"]["evm"]["bytecode"]["object"]
    abi = json.loads(compiled_sol["contracts"]["RentContract.sol"]["RentContract"]["metadata"])["output"]["abi"]
    # Rodando o ganache localmente...
    w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
    smart_contract = w3.eth.contract(abi=abi, bytecode=bytecode)
    nonce = w3.eth.get_transaction_count(address)
    # Parâmetros do construtor do smart contract
    transaction = smart_contract.constructor(landlord, tenant, tenantAddress, contractTotalValue, monthlyValue,
                      monthsQuantity, actualDay, dayToBeEffective).build_transaction(
        {"chainId": chain_id, "gasPrice": w3.eth.gas_price, "from": address, "nonce": nonce})
    sign_transaction = w3.eth.account.sign_transaction(transaction, private_key=private_key)
    transaction_hash = w3.eth.send_raw_transaction(sign_transaction.raw_transaction)
    transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)
    # Referência para o smart contract
    smart_contract = w3.eth.contract(address=transaction_receipt.contractAddress, abi=abi)


@given("the landlord {landlord}")
def step_impl(context, landlord):
     context.landlord = landlord

@step("the tenant address {tenant_address}")
def step_impl(context, tenant_address):
    context.tenant_address = tenant_address


@step("the tenant {tenant}")
def step_impl(context, tenant):
    context.tenant = tenant

@step("the effective date of the contract {effective_date}")
def step_impl(context, effective_date):
    context.effective_date = effective_date


@given("the contract total value {total_value}")
def step_impl(context, total_value):
    context.total_value = total_value


@step("the monthly value {monthly_value}")
def step_impl(context, monthly_value):
    context.monthly_value = monthly_value


@step("the months quantity {quantity}")
def step_impl(context, quantity):
    context.quantity = quantity


@step("today is {today}")
def step_impl(context, today):
    context.today = today


@when("the contract is created")
def step_impl(context):
    __deploy_contract(context.landlord, context.tenant, context.tenant_address,
                      int(context.total_value), int(context.monthly_value), int(context.quantity),
                      int(context.creation_day), int(context.effective_date))


@then("the contract landlord must be {landlord}")
def step_impl(context, landlord):
    TestCase.assertEqual(TestCase(), landlord, smart_contract.functions.getLandlord().call())


@step("the contract tenant must be {tenant}")
def step_impl(context, tenant):
    TestCase.assertEqual(TestCase(), tenant, smart_contract.functions.getTenant().call())


@step("the contract tenant address must be {address}")
def step_impl(context, address):
    TestCase.assertEqual(TestCase(), address, smart_contract.functions.getTenantAddress().call())


@step("the contract total value must be {total_value}")
def step_impl(context, total_value):
    TestCase.assertEqual(TestCase(), int(total_value), smart_contract.functions.getContractTotalValue().call())


@step("the contract monthly value must be {monthly_value}")
def step_impl(context, monthly_value):
    TestCase.assertEqual(TestCase(), int(monthly_value), smart_contract.functions.getMonthlyValue().call())


@step("the contract months quantity must be {months_quantity}")
def step_impl(context, months_quantity):
    TestCase.assertEqual(TestCase(), int(months_quantity), smart_contract.functions.getMonthsQuantity().call())


@step("the contract creation day must be {creation_day}")
def step_impl(context, creation_day):
    TestCase.assertEqual(TestCase(), int(creation_day), smart_contract.functions.getCreationDay().call())


@step("the contract effective day must be {effective_day}")
def step_impl(context, effective_day):
    TestCase.assertEqual(TestCase(), int(effective_day), smart_contract.functions.getEffectiveDay().call())


@step("the contract status must be {status_value}")
def step_impl(context, status_value):
    contract_status = smart_contract.functions.getStatus().call()
    if status_value == "Created":
        TestCase.assertEqual(TestCase(), 0, contract_status)
    elif status_value == "InEffect":
        TestCase.assertEqual(TestCase(), 1, contract_status)
    elif status_value == "SuccessfulTermination":
        TestCase.assertEqual(TestCase(), 2, contract_status)
    elif status_value == "UnsuccessfulTermination":
        TestCase.assertEqual(TestCase(), 3, contract_status)
    else:
        TestCase.fail("Unknown status " + status_value)


@step("the creation date {creation_date}")
def step_impl(context, creation_date):
    context.creation_date = creation_date


@step("the contract is created")
def step_impl(context):
    __deploy_contract(context.landlord, context.tenant, context.tenant_address,
                      int(context.total_value), int(context.monthly_value), int(context.quantity),
                      int(context.creation_date), int(context.effective_date))


@step("the contract is activated")
def step_impl(context):
    transaction = smart_contract.functions.activate(int(context.effective_date)).build_transaction({"chainId": chain_id,
                                                                         "gasPrice": w3.eth.gas_price,
                                                                         "from": address,
                                                                         "nonce": w3.eth.get_transaction_count(address)})
    sign_transaction = w3.eth.account.sign_transaction(transaction, private_key=private_key)
    transaction_hash = w3.eth.send_raw_transaction(sign_transaction.raw_transaction)


@when("the contract is created today")
def step_impl(context):
    __deploy_contract(context.landlord, context.tenant, context.tenant_address,
                      int(context.total_value), int(context.monthly_value), int(context.quantity),
                      int(context.today), int(context.effective_date))


@step("the contract is activated today")
def step_impl(context):
    transaction = smart_contract.functions.activate(int(context.today)).build_transaction({"chainId": chain_id,
                                                                         "gasPrice": w3.eth.gas_price,
                                                                         "from": address,
                                                                         "nonce": w3.eth.get_transaction_count(address)})
    sign_transaction = w3.eth.account.sign_transaction(transaction, private_key=private_key)
    transaction_hash = w3.eth.send_raw_transaction(sign_transaction.raw_transaction)


# ==========================================

@step("a monthly payment is done on day {day}")
def step_impl(context, day):
    transaction = smart_contract.functions.make_payment(int(day)).build_transaction({"chainId": chain_id,
                                                                         "gasPrice": w3.eth.gas_price,
                                                                         "from": address,
                                                                         "nonce": w3.eth.get_transaction_count(address)})
    sign_transaction = w3.eth.account.sign_transaction(transaction, private_key=private_key)
    transaction_hash = w3.eth.send_raw_transaction(sign_transaction.raw_transaction)


@step("{quantity} payments have been done")
def step_impl(context, quantity):
    TestCase.assertEqual(TestCase(), int(quantity), smart_contract.functions.getPaidMonthsQuantity().call())


@step("payment month {month} was on day {day}")
def step_impl(context, month, day):
    TestCase.assertEqual(TestCase(), int(int(day)), smart_contract.functions.getPaidDay(int(month)).call())


@step("the local availability is {availability}")
def step_impl(context, availability):
    TestCase.assertEqual(TestCase(), True, smart_contract.functions.getLocalIsAvailable().call())


# =========================================

@step("missed the water bill payment")
def step_impl(context):
    transaction = smart_contract.functions.waterNotPaid().build_transaction({"chainId": chain_id,
                                                                        "gasPrice": w3.eth.gas_price,
                                                                        "from": address,
                                                                        "nonce": w3.eth.get_transaction_count(address)})
    sign_transaction = w3.eth.account.sign_transaction(transaction, private_key=private_key)
    transaction_hash = w3.eth.send_raw_transaction(sign_transaction.raw_transaction)

@step("missed the tax payment")
def step_impl(context):
    transaction = smart_contract.functions.taxNotPaid().build_transaction({"chainId": chain_id,
                                                                        "gasPrice": w3.eth.gas_price,
                                                                        "from": address,
                                                                        "nonce": w3.eth.get_transaction_count(address)})
    sign_transaction = w3.eth.account.sign_transaction(transaction, private_key=private_key)
    transaction_hash = w3.eth.send_raw_transaction(sign_transaction.raw_transaction)