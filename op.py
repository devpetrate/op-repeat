from web3 import Web3
import time

# Connect to the Optimism network via Infura RPC
infura_url = "https://optimism-mainnet.infura.io"
web3 = Web3(Web3.HTTPProvider(infura_url))

# Check if the connection is successful
if not web3.isConnected():
    raise Exception("Failed to connect to Optimism network")

# Constants
CHAIN_ID = 10  # Optimism Chain ID
TO_ADDRESS = "0x51ECd682D0971BCa6F58A7d39869b87f0dc94459"  # Recipient Address

# Function to send 0 ETH transaction
def send_0_eth_transaction(private_key, to_address, repetitions):
    # Get the sender address from the private key
    sender_address = web3.eth.account.from_key(private_key).address

    # Loop for the specified number of repetitions
    for i in range(repetitions):
        # Get the current transaction count (nonce)
        nonce = web3.eth.getTransactionCount(sender_address)

        # Create the transaction dictionary
        tx = {
            'nonce': nonce,
            'to': to_address,
            'value': 0,  # 0 ETH
            'gas': 21000,  # Basic gas limit for ETH transfers
            'gasPrice': web3.eth.gas_price,  # Use current network gas price
            'chainId': CHAIN_ID
        }

        # Sign the transaction with the private key
        signed_tx = web3.eth.account.sign_transaction(tx, private_key)

        # Send the transaction
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

        # Print the transaction hash
        print(f"Transaction {i+1}/{repetitions} sent! Tx Hash: {web3.toHex(tx_hash)}")

        # Wait a few seconds between transactions to avoid nonce issues
        time.sleep(5)

# Main script
if __name__ == "__main__":
    # Get the private key from the user (ensure you keep this secure!)
    private_key = input("Enter your private key: ")

    # Ask how many times to perform the transaction
    repetitions = int(input("How many times do you want to perform the transaction? "))

    # Call the function to send transactions
    send_0_eth_transaction(private_key, TO_ADDRESS, repetitions)
