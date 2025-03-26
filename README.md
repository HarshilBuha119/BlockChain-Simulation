# Simple Blockchain Simulation

## Overview
This project is a basic **Blockchain Simulation** implemented in Python. It demonstrates core blockchain concepts, including:

- Block structure (index, timestamp, transactions, hashes)
- Hash generation using **SHA-256**
- Chain validation to detect tampering
- Basic **Proof-of-Work** mechanism
- Adding and mining transactions

## Features
✅ **Block Structure**: Each block contains an index, timestamp, transactions, previous block hash, and its own hash.  
✅ **Hashing**: Uses SHA-256 to hash each block.  
✅ **Blockchain Management**: Manages adding blocks, transactions, and validating the chain.  
✅ **Proof-of-Work**: Implements a mining mechanism where block hashes must meet a difficulty condition.  
✅ **Tamper Detection**: Demonstrates how modifying a block invalidates the chain.  

---

## Installation & Setup
### **1️⃣ Prerequisites**
- Python 3.x installed
- (Optional) Docker for containerization

### **2️⃣ Clone the Repository**
```bash
git clone https://github.com/your-username/blockchain-simulation.git
cd blockchain-simulation
```

### **3️⃣ Run the Blockchain Simulation**
```bash
python blockchain.py
```

---

## Usage
### **Adding Transactions and Mining Blocks**
The script demonstrates transaction addition and mining:
1. Transactions are added using `add_transaction(sender, receiver, amount)`.
2. Mining adds a block to the blockchain.

Example:
```python
blockchain.add_transaction("Alice", "Bob", 5.0)
blockchain.mine_block()
```

### **Checking Blockchain Integrity**
```python
print("Is blockchain valid?", blockchain.is_chain_valid())
```
If any block is tampered with, the validation will fail.

### **Tampering Detection**
The script modifies a block's transaction to show how the chain detects tampering.

---

## Docker Setup (Optional)
### **1️⃣ Build Docker Image**
```bash
docker build -t blockchain-simulation .
```
### **2️⃣ Run Container**
```bash
docker run --rm blockchain-simulation
```

---

## Project Structure
```
blockchain-simulation/
├── blockchain.py   # Main blockchain logic
├── Dockerfile      # Docker setup (optional)
├── README.md       # Documentation
└── requirements.txt # Dependencies (if needed)
```

---

## Future Improvements 🚀
- [ ] Implement a Flask API for interaction
- [ ] Add a simple UI for transaction visualization
- [ ] Improve Proof-of-Work mechanism

## License
MIT License.


