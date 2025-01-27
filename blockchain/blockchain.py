from .block import Block
import csv
import os

class Blockchain:
    def __init__(self, difficulty=4):
        self.chain = []
        self.difficulty = difficulty
        self.csv_file = os.path.join(os.path.dirname(__file__), 'blockchain_data.csv')
        self.load_chain()

    def load_chain(self):
        """Load blockchain from CSV file if it exists, otherwise create genesis block."""
        if os.path.exists(self.csv_file):
            with open(self.csv_file, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    block = Block(
                        int(row['index']),
                        row['data'],
                        row['previous_hash']
                    )
                    block.timestamp = float(row['timestamp'])
                    block.nonce = int(row['nonce'])
                    block.hash = row['hash']
                    self.chain.append(block)
        else:
            self.create_genesis_block()

    def save_chain(self):
        """Save blockchain to CSV file."""
        with open(self.csv_file, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['index', 'timestamp', 'data', 'previous_hash', 'hash', 'nonce'])
            writer.writeheader()
            for block in self.chain:
                writer.writerow({
                    'index': block.index,
                    'timestamp': block.timestamp,
                    'data': block.data,
                    'previous_hash': block.previous_hash,
                    'hash': block.hash,
                    'nonce': block.nonce
                })

    def create_genesis_block(self):
        """Create the first block in the chain."""
        genesis_block = Block(0, "Genesis Block", "0")
        genesis_block.mine_block(self.difficulty)
        self.chain.append(genesis_block)

    def get_latest_block(self):
        """Return the most recent block in the chain."""
        return self.chain[-1]

    def add_block(self, data):
        """Add a new block to the chain and save to CSV."""
        previous_block = self.get_latest_block()
        new_block = Block(
            previous_block.index + 1,
            data,
            previous_block.hash
        )
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
        self.save_chain()

    def is_chain_valid(self):
        """Verify the current state of the blockchain."""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            # Verify current block's hash
            if current_block.hash != current_block.calculate_hash():
                return False

            # Verify chain link
            if current_block.previous_hash != previous_block.hash:
                return False

        return True