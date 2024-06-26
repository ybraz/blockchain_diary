from web3 import Web3
from solcx import compile_standard
import json
import os

# Conexão com o nó Ethereum (Infura, Ganache, etc.)
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

# Compilar o contrato
with open(os.path.join(os.path.dirname(__file__), '../contracts/Diary.sol'), 'r') as file:
    diary_contract = file.read()

compiled_sol = compile_standard({
    "language": "Solidity",
    "sources": {"Diary.sol": {"content": diary_contract}},
    "settings": {"outputSelection": {"*": {"*": ["abi", "evm.bytecode"]}}}
})

bytecode = compiled_sol['contracts']['Diary.sol']['Diary']['evm']['bytecode']['object']
abi = compiled_sol['contracts']['Diary.sol']['Diary']['abi']

# Salvar ABI em um arquivo
with open(os.path.join(os.path.dirname(__file__), 'DiaryABI.json'), 'w') as abi_file:
    json.dump(abi, abi_file)

# Implantar o contrato
diary_contract = w3.eth.contract(abi=abi, bytecode=bytecode)
tx_hash = diary_contract.constructor().transact({'from': w3.eth.accounts[0], 'gas': 410000})
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
contract_address = tx_receipt.contractAddress
print(f"Contract deployed at address: {contract_address}")
