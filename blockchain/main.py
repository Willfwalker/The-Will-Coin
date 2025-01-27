from blockchain import Blockchain
import time

def main():
    # Create blockchain with difficulty of 4 (adjust as needed)
    blockchain = Blockchain(difficulty=4)
    
    print("Mining block 1...")
    blockchain.add_block("Transaction: Alice sends 10 BTC to Bob")
    
    print("Mining block 2...")
    blockchain.add_block("Transaction: Bob sends 5 BTC to Charlie")
    
    print("Mining block 3...")
    blockchain.add_block("Transaction: Charlie sends 3 BTC to David")

    # Print blockchain details
    print("\nBlockchain details:")
    for block in blockchain.chain:
        print(f"\nBlock #{block.index}")
        print(f"Timestamp: {time.ctime(block.timestamp)}")
        print(f"Data: {block.data}")
        print(f"Previous Hash: {block.previous_hash}")
        print(f"Hash: {block.hash}")
        print(f"Nonce: {block.nonce}")

    # Validate the blockchain
    print(f"\nIs blockchain valid? {blockchain.is_chain_valid()}")

if __name__ == "__main__":
    main()