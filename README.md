# 🦊 Ethereum Wallet Generator

A simple Python script to generate one or more Ethereum wallet addresses and their corresponding private keys.

---

## 📦 Features

- Generates any number of Ethereum wallets
- Saves:
  - Public addresses → `eth_addresses.txt`
  - Private keys → `eth_private_keys.txt`
- Interactive CLI: specify how many wallets to generate

---

## 🚀 Requirements

- Python 3.6+
- `web3` library

---

## 🛠 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Yours-Pranav/EVM-Wallet-Gen.git
cd EVM-Wallet-Gen
# 📦 Install Python dependencies
pip install web3

# 🧪 Run the script
python main.py



## 🖥️ Example Terminal Output

When you run the script:

```bash
$ python main.py
🔢 How many Ethereum wallets do you want to generate? 3
Generated 3 Ethereum wallets.
Saved to 'eth_addresses.txt' and 'eth_private_keys.txt'

