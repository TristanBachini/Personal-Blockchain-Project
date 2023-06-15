import pickle
from web3 import Web3, HTTPProvider

ganache_url = "http://127.0.0.1:7545"

web3 = Web3(HTTPProvider(ganache_url))

# request the latest block number
ending_blocknumber = web3.eth.block_number + 1

# defining the first block number
starting_blocknumber = ending_blocknumber - (ending_blocknumber-1)

# filter through blocks and look for transactions involving this address
blockchain_address = "0xC6d90A9f15d03D3565cC67EC815D6aF0C0febFAC"

# create an empty dictionary we will add transaction data to
tx_dictionary = {}

''' This function takes the starting block number, ending block number and an Ethereum address. 
    The function loops over the transactions in each block and checks if the address in the to field 
    matches the Ethereum address that will passed. It exports the transactions into a pickle file. '''

def getTransactions(start, end, address):
    print(f"Scanning from block {start} to {end} for transactions involving the address - {address}")
    for x in range(start, end):
        block = web3.eth.get_block(x, True)
        for transaction in block.transactions:
            if transaction['to'] == address or transaction['from'] == address:
                with open("transactions.pkl", "wb") as f:
                    hashStr = transaction['hash'].hex()
                    tx_dictionary[hashStr] = transaction
                    pickle.dump(tx_dictionary, f)
                f.close()
    print(f"The address has {len(tx_dictionary)} transactions from block {start} to {end}.")
    
getTransactions(starting_blocknumber, ending_blocknumber, blockchain_address)