import hashlib
import time

class Block:
    def __init__(self, index, transactions, previous_hash, nonce=0):
        self.index = index
        self.timestamp = time.time()  # Current time in seconds
        self.transactions = transactions  # List of transactions
        self.previous_hash = previous_hash  # Hash of the previous block
        self.nonce = nonce  # For Proof-of-Work
        self.hash = self.calculate_hash()  # Current block's hash

    def calculate_hash(self):
        # Combine all block data into a single string and hash it
        block_string = f"{self.index}{self.timestamp}{self.transactions}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def __str__(self):
        return (f"Block #{self.index}\n"
                f"Timestamp: {self.timestamp}\n"
                f"Transactions: {self.transactions}\n"
                f"Previous Hash: {self.previous_hash}\n"
                f"Hash: {self.hash}\n")

class Blockchain:
    def __init__(self):
        # Genesis block (first block in the chain)
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4  # For Proof-of-Work (number of leading zeros)

    def create_genesis_block(self):
        # First block with dummy data
        return Block(0, ["Genesis Block"], "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, transactions):
        # Create a new block linked to the previous one
        previous_block = self.get_latest_block()
        new_block = Block(previous_block.index + 1, transactions, previous_block.hash)
        
        # Mine the block with Proof-of-Work
        new_block.hash = self.mine_block(new_block)
        self.chain.append(new_block)
        print(f"Block #{new_block.index} added to the chain!")

    def mine_block(self, block):
        # Proof-of-Work: Find a hash with 'difficulty' leading zeros
        target = "0" * self.difficulty
        while block.hash[:self.difficulty] != target:
            block.nonce += 1
            block.hash = block.calculate_hash()
        print(f"Block mined! Nonce: {block.nonce}")
        return block.hash

    def is_chain_valid(self):
        # Validate the entire chain
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            # Check if current block's hash is valid
            if current.hash != current.calculate_hash():
                print(f"Invalid hash at Block #{current.index}")
                return False

            # Check if previous hash links correctly
            if current.previous_hash != previous.hash:
                print(f"Invalid previous hash link at Block #{current.index}")
                return False

        return True

    def print_chain(self):
        # Print all blocks in the chain
        print("\nCurrent Blockchain State:")
        for block in self.chain:
            print(block)
            print("-" * 50)

def main():
    # Create a blockchain instance
    my_blockchain = Blockchain()
    print("Genesis block created!\n")

    # Dynamically add blocks with user-input transactions
    for i in range(1, 3):  # Add 2 blocks as an example
        print(f"\nPreparing Block #{i}")
        transactions = input("Enter transactions (comma-separated, e.g., 'Alice sends 10 BTC to Bob'): ").split(",")
        my_blockchain.add_block([t.strip() for t in transactions])  # Strip whitespace from inputs

    # Print the blockchain
    my_blockchain.print_chain()

    # Validate the chain
    print("\nIs chain valid?", my_blockchain.is_chain_valid())

    # Tamper with the chain (modify Block 1)
    print("\nTampering with Block 1...")
    my_blockchain.chain[1].transactions = ["Alice sends 1000 BTC to Hacker"]  # Tamper with data
    my_blockchain.chain[1].hash = my_blockchain.chain[1].calculate_hash()  # Recalculate hash

    # Print tampered chain
    my_blockchain.print_chain()

    # Validate again
    print("\nIs chain valid after tampering?", my_blockchain.is_chain_valid())

if __name__ == "__main__":
    main()
