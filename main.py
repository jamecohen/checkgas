from web3 import Web3

#RPC list
eth_rpc = 'https://1rpc.io/eth'

#connect
web3 = Web3(Web3.HTTPProvider(eth_rpc))
print(web3.is_connected())

#check gas
gas_price = web3.eth.gas_price
gas_price_gwei = web3.from_wei(gas_price, 'gwei')
print(gas_price_gwei)
