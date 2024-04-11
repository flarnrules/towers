import subprocess
import json
import os
import datetime

# Constants for split percentages and memo
STAKE_PERCENTAGE = 0.25
LIQUID_PERCENTAGE = 0.24
SMOKERS_CLUB_PERCENTAGE = 0.01
COLLABORATORS_PERCENTAGE = 0.50
MEMO = "for collab 🏙️🌆"
TRANSACTIONS_DIR = "../data/transactions"
COLLABS_FILE_PATH = "../data/collabs.json"

# Collaborators' contributions
contributions = {
    'Jinxto': 7,
    'Fluffhead': 2,
    'Ajk': 3,
    'Randomkid': 3,
    'Berny': 2,
    'Votor': 1,
    'Quasimosos': 2,
    'Ijon': 6,
    'Pixlgeist': 1,
    'Sia': 1,
    'Graphein': 1,
    'Reggie': 1,
    'Frogstar': 5,
    'Ubr': 1,
    'Sage': 1,
    'Brasco': 1,
    'Blue': 1,
    'Sebi': 3,
    'Brady': 1,
    'Peps': 1
    # Add more collaborators here
}

def get_wallet_balance():
    command = ["starsd", "query", "bank", "balances", "stars1hyhmssn4j6fxlvq58ctlpxwg5az7shg7zc77rp"]
    result = subprocess.run(command, capture_output=True, text=True)
    raw_output = result.stdout


    # Parse the raw output to extract the amount
    for line in raw_output.split('\n'):
        if 'amount:' in line:
            # Extract the amount value from the line
            amount = int(line.split('"')[1])
            liquid_contents = amount / 1_000_000  # Convert ustars to Stars
            return liquid_contents
    
    print("No balance found in the output.")
    return 0


# Count of collaborators
collaborator_count = len(contributions)

def calculate_next_tuesday(current_date):
    current_date = datetime.datetime.strptime(current_date, "%Y-%m-%d")
    next_tuesday = current_date + datetime.timedelta(days=(1 - current_date.weekday() + 7) % 7)
    return next_tuesday.strftime("%Y-%m-%d")

def get_royalty_amounts(liquid_contents):
    total_contributions = sum(contributions.values())
    collaborators_amount = liquid_contents * COLLABORATORS_PERCENTAGE

    royalties = {}
    for collaborator, num_nfts in contributions.items():
        collaborator_amount = collaborators_amount * (num_nfts / total_contributions)
        royalties[collaborator] = collaborator_amount

    return royalties

def calculate_royalties():
    # Getting the date in ISO format
    date_input = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # Getting the wallet liquid contents
    # queries liquid contents 'starsd query bank balances stars1hyhmssn4j6fxlvq58ctlpxwg5az7shg7zc77rp'
    liquid_contents = get_wallet_balance()
    
    royalties = get_royalty_amounts(liquid_contents)

    total_contributions = sum(contributions.values())

    # Calculations for splits
    stake_amount = int(liquid_contents * STAKE_PERCENTAGE)
    liquid_amount = int(liquid_contents * LIQUID_PERCENTAGE)
    smokers_club_amount = int(liquid_contents * SMOKERS_CLUB_PERCENTAGE)
    collaborators_amount = int(liquid_contents * COLLABORATORS_PERCENTAGE)

    # Separator for formatting
    separator = "=" * 40
    print(f"\n{separator}\n{date_input} - wallet liquid contents = {liquid_contents:,.0f} STARS")
    print("Split - 25% stake, 24% liquid, 1% to smokers club, 50% to collaborators")
    print(f"25% x {liquid_contents:,.0f} = {stake_amount:,} Staked")
    print(f"24% x {liquid_contents:,.0f} = {liquid_amount:,} Liquid")
    print(f"1% x {liquid_contents:,.0f} = {smokers_club_amount:,} To Smoker's Club")
    print(f"50% x {liquid_contents:,.0f} = {collaborators_amount:,} Collaborators")

    print(f"\nTotal collaborators: {collaborator_count}")
    print(f"Total collaborations: {total_contributions}")
    print(f"\nBreakdown\n{separator}")

    counter = 1
    for collaborator, num_nfts in contributions.items():
        collaborator_percentage = (num_nfts / total_contributions) * 100
        collaborator_amount = int(collaborators_amount * (num_nfts / total_contributions))
        counter_str = f"{counter}.".ljust(4)
        print(f"{counter_str} {collaborator.ljust(10)} - {num_nfts} of {total_contributions} ({collaborator_percentage:6.2f}%) = {collaborator_amount:,} STARS")
        counter += 1

    print(separator)
    print(f"Next split on {calculate_next_tuesday(date_input)}")
    print(f"memo: {MEMO}")
    print(f"{separator}")

    generate_tx = input("Do you want to generate a transaction from the results? (y/n) ").strip().lower()
    if generate_tx == 'y':
        # Load the collaborators' addresses
        if not os.path.exists(COLLABS_FILE_PATH):
            print(f"Error: The file {COLLABS_FILE_PATH} does not exist.")
            return  # Exit the function if the file doesn't exist

        with open(COLLABS_FILE_PATH, 'r') as f:
            collab_addresses = json.load(f)

        # Ensure the transactions directory exists
        os.makedirs(TRANSACTIONS_DIR, exist_ok=True)
        
        # Timestamp for the transaction file
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        file_path = os.path.join(TRANSACTIONS_DIR, f'transaction_{timestamp}.json')

        # Generate the custom transactions
        transactions = []
        for name, amount in royalties.items():
            if name in collab_addresses:
                address = collab_addresses[name]
                # Construct the transaction object
                transaction = {
                    "msg": {
                        "type": "cosmos-sdk/MsgSend",
                        "value": {
                            "from_address": "royalties_wallet_address",  # Make sure to replace with actual wallet address
                            "to_address": address,
                            "amount": [{"denom": "ustar", "amount": str(int(amount * 1000000))}]  # assuming the amount needs to be in micro units
                        }
                    },
                    "fee": {"amount": [{"denom": "ustar", "amount": "5000"}], "gas": "200000"},
                    "memo": f"Royalty payout for {name} on {date_input}",
                }
                transactions.append(transaction)
        
        # Write the transaction to a file
        with open(file_path, 'w') as f:
            json.dump(transactions, f, indent=4)

        print(f"Transaction generated and saved to {file_path}")

calculate_royalties()
