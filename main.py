from web3 import Web3
from eth_account import Account

# Enable key generation
Account.enable_unaudited_hdwallet_features()

# Ask the user for how many wallets to generate
try:
    NUM_WALLETS = int(input("🔢 How many Ethereum wallets do you want to generate? "))
    if NUM_WALLETS <= 0:
        raise ValueError("Number must be greater than zero.")
except ValueError as e:
    print(f"❌ Invalid input: {e}")
    exit(1)

private_keys = []
addresses = []

for _ in range(NUM_WALLETS):
    acct = Account.create()
    private_keys.append(acct.key.hex())
    addresses.append(acct.address)

# Save private keys
with open("eth_private_keys.txt", "w") as pk_file:
    for key in private_keys:
        pk_file.write(key + "\n")

# Save addresses
with open("eth_addresses.txt", "w") as addr_file:
    for addr in addresses:
        addr_file.write(addr + "\n")

print(f"\n✅ Generated {NUM_WALLETS} Ethereum wallets.")
print("🔐 Private keys saved to: eth_private_keys.txt")
print("📬 Addresses saved to: eth_addresses.txt")

