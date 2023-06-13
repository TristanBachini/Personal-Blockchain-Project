from web3 import Web3

ganache_url = "http://127.0.0.1:7545"

web3 = Web3(Web3.HTTPProvider(ganache_url))

#address of account 1
account_1 = "0x08b70f7CF2a5fACaCC2A4F4c71d219A45B636341"

#address of account 2
account_2 = "0xC6d90A9f15d03D3565cC67EC815D6aF0C0febFAC"

#private key of account 1
#We need pkey of account 1, so that the blockchain knows that it is okay to send funds 
#from account 1.
#Kind of like a password.
#Allows us to authorize or "sign" transactions.
private_key = "0xd768f0556f3b6197552682be1e65a192510ce3ebb3dfb8a778fe3bf58ff02ccf"

#we want to send funds from account 1 to account 2


#Next, we get the nonce
nonce = web3.eth.get_transaction_count(account_1)
#Then, we build the transaction.
tx = {
    'nonce':nonce,
    'to': account_2,
    'value': web3.to_wei(1,'ether'),
    'gas':2000000,
    'gasPrice':web3.to_wei('50','gwei')

}
#Then, we sign it.
signed_tx = web3.eth.account.sign_transaction(tx,private_key)
#Then, we send it.
tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
#Then, we get the transaction hash.

print(tx_hash)