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

```bash
# 📁 Step 1: Clone the repository
git clone https://github.com/Yours-Pranav/EVM-Wallet-Gen.git
cd EVM-Wallet-Gen

# 📦 Step 2: Install dependencies
pip install web3
```

---

## 🧪 Usage

```bash
# 🧪 Run the script
python main.py
```

You will be prompted:

```text
🔢 How many Ethereum wallets do you want to generate?
```

Enter a number (e.g. `10`) and two files will be generated:

- `eth_addresses.txt`
- `eth_private_keys.txt`

Each line corresponds to one wallet.

---

## 🖥️ Example Terminal Output

```bash
$ python main.py
🔢 How many Ethereum wallets do you want to generate? 3
Generated 3 Ethereum wallets.
Saved to 'eth_addresses.txt' and 'eth_private_keys.txt'
```

---

## 📁 Example Output Files

### 🧾 eth_addresses.txt

```text
0x0D1dBeA88D19738c367A7C1B4F9217D47C26d5B2
0x8f3d3C3F5d633498BDA55B7EbA1116621Fe3Cb1F
0xA1F5677aE6d383e7Ef4d682B7F82b6Df95A6CcD4
```

### 🔐 eth_private_keys.txt

```text
0x6a1f1de3b6f6b7e0f28e5d9a7d3e60aa1d528dfdc48e3195e7f8f7e0173a7cf2
0x8f2a559490823a3cf812e50276ad5d3f3cd7f2b4206e65cfa9ae38d2a43cda57
0x4bc20a05918bbd79c61127525c3b6726c3f0590703a48b2ae2073f6d684cb4ed
```

---

## 🔐 Warning

⚠️ **Do not share your private keys.**  
These wallets are for testing purposes. For production or real funds, use audited and secure wallet tools.

---

## 🤝 Contributions

Pull requests welcome! For major changes, please open an issue first.

---


