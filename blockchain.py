import hashlib  # Used for generating secure hash values
import time  # Used for timestamps
import json  # Used for converting data structures to JSON format

class Block:
    """ Represents a block in the blockchain """
    
    def __init__(self, index, transactions, timestamp, previous_hash, nonce=0):
        """
        Initializes a new block.
        
        :param index: Position of the block in the chain
        :param transactions: List of transactions in the block
        :param timestamp: Time when the block was created
        :param previous_hash: Hash of the previous block in the chain
        :param nonce: Number used in mining (Proof-of-Work)
        """
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.calculate_hash()  # Compute initial hash for the block

    def calculate_hash(self):
        """
        Computes the SHA-256 hash of the block.
        :return: The hash of the block
        """
        block_string = json.dumps({
            "index": self.index,
            "transactions": self.transactions,
            "timestamp": self.timestamp,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True)  # Sorting keys ensures consistent hash values
        return hashlib.sha256(block_string.encode()).hexdigest()  # Generate SHA-256 hash


class Blockchain:
    """ Represents a blockchain """

    def __init__(self):
        """
        Initializes the blockchain with a genesis block.
        """
        self.chain = []  # List to store blocks
        self.difficulty = 4  # Defines mining difficulty (number of leading zeros)
        self.pending_transactions = []  # Transactions waiting to be added to a block
        self.create_genesis_block()  # Generate the first block in the chain

    def create_genesis_block(self):
        """
        Creates the first block of the blockchain (Genesis Block).
        """
        genesis_block = Block(0, [{"sender": "Genesis", "receiver": "Network", "amount": 0}], 
                              time.strftime('%Y-%m-%d %H:%M:%S'), "0")
        genesis_block.hash = self.proof_of_work(genesis_block)  # Perform proof of work
        self.chain.append(genesis_block)  # Add genesis block to chain

    def get_latest_block(self):
        """
        Retrieves the most recently added block in the blockchain.
        :return: The latest block
        """
        return self.chain[-1]

    def add_transaction(self, sender, receiver, amount):
        """
        Adds a transaction to the list of pending transactions.
        
        :param sender: Sender's name
        :param receiver: Receiver's name
        :param amount: Amount being transferred
        """
        if sender and receiver and amount > 0:  # Validate transaction
            self.pending_transactions.append({"sender": sender, "receiver": receiver, "amount": amount})
        else:
            print("Invalid transaction")  # Display error if transaction is invalid

    def mine_block(self):
        """
        Mines a new block containing pending transactions and adds it to the blockchain.
        :return: True if the block was mined, False otherwise
        """
        if not self.pending_transactions:
            print("No transactions to mine.")  # Skip mining if no transactions
            return False
        
        # Create a new block using pending transactions
        block = Block(len(self.chain), list(self.pending_transactions), 
                      time.strftime('%Y-%m-%d %H:%M:%S'), self.get_latest_block().hash)
        
        block.hash = self.proof_of_work(block)  # Perform proof of work
        self.chain.append(block)  # Add block to chain
        self.pending_transactions = []  # Clear pending transactions
        print(f"Block {block.index} successfully mined!")  # Confirm successful mining
        return True

    def proof_of_work(self, block):
        """
        Implements Proof-of-Work by finding a hash with the required number of leading zeros.
        
        :param block: The block to be mined
        :return: The valid hash of the mined block
        """
        block.nonce = 0  # Start nonce at 0
        computed_hash = block.calculate_hash()  # Calculate initial hash
        
        # Adjust nonce until a valid hash is found
        while not computed_hash.startswith('0' * self.difficulty):
            block.nonce += 1
            computed_hash = block.calculate_hash()
        
        return computed_hash  # Return valid hash

    def is_chain_valid(self):
        """
        Checks whether the blockchain is valid.
        
        :return: True if the blockchain is valid, False if it's been tampered with
        """
        for i in range(1, len(self.chain)):  # Start from second block (index 1)
            current = self.chain[i]
            previous = self.chain[i - 1]
            
            if current.hash != current.calculate_hash():  # Validate block integrity
                print(f"Block {i} has been tampered!")
                return False
            
            if current.previous_hash != previous.hash:  # Validate chain linkage
                print(f"Block {i} has an invalid previous hash!")
                return False
        
        return True  # If all blocks are valid, return True

    def print_chain(self):
        """
        Prints all blocks in the blockchain.
        """
        for block in self.chain:
            print("\nBlock Details:")
            print(f"Index: {block.index}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Transactions: {json.dumps(block.transactions, indent=4)}")  # Pretty-print transactions
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Current Hash: {block.hash}")
            print(f"Nonce: {block.nonce}")


# Demonstration
def main():
    """
    Demonstrates the working of the blockchain.
    """
    blockchain = Blockchain()  # Create a new blockchain

    print("\nAdding transactions and mining blocks...")
    blockchain.add_transaction("Alice", "Bob", 1.5)
    blockchain.add_transaction("Bob", "Charlie", 0.8)
    blockchain.mine_block()  # Mine the block

    blockchain.add_transaction("Charlie", "Dave", 2.2)
    blockchain.mine_block()  # Mine another block

    print("\nOriginal Blockchain:")
    blockchain.print_chain()  # Print blockchain data

    print("\nValidating original chain...")
    print("Is chain valid?", blockchain.is_chain_valid())  # Validate blockchain

    print("\nTampering with block 1...")
    blockchain.chain[1].transactions[0]["amount"] = 100  # Modify block to simulate tampering

    print("\nValidating tampered chain...")
    print("Is chain valid?", blockchain.is_chain_valid())  # Check if blockchain is still valid


# Run the script
if __name__ == "__main__":
    main()
