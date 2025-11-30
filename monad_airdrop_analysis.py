import pandas as pd

# Sample structure for wallet + allocation analysis
# Replace this later with real data from Dune or CSV

# Load your CSV file
df = pd.read_csv("monad_airdrop_data.csv")

# Total unique wallets eligible
total_wallets = df['wallet'].nunique()

# Total allocated amount
total_allocation = df['allocation'].sum()

print("Total eligible wallets:", total_wallets)
print("Total allocation:", total_allocation)
