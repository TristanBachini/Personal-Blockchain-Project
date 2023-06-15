from web3 import Web3

ganache_url = "http://127.0.0.1:7545"

web3 = Web3(Web3.HTTPProvider(ganache_url))

# Set Address of Sender
account_1 = "0x08b70f7CF2a5fACaCC2A4F4c71d219A45B636341"

# Set Address of Receiver
account_2 = "0xC6d90A9f15d03D3565cC67EC815D6aF0C0febFAC"

# Private Key of Sender (Account 1)
# This informs the blockchain that this transaction is signed by the sender.
private_key = "0xd768f0556f3b6197552682be1e65a192510ce3ebb3dfb8a778fe3bf58ff02ccf"

# Get Nonce from Sender's Account
# Nonce is a number that is only used once per account. Transaction counts always go up
# after every transaction so it is a good source of nonce.
nonce = web3.eth.get_transaction_count(account_1)

#Then, we build the transaction.
tx = {
    'nonce':nonce,                          
    'to': account_2,                        
    'value': web3.to_wei(1,'ether'),        
    'gas':2000000,                          
    'gasPrice':web3.to_wei('50','gwei')

}

# Signing Transaction using Private Key
signed_tx = web3.eth.account.sign_transaction(tx,private_key)

# Sending Transaction
tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

# Printing Transaction Hash as a Receipt
print(tx_hash)