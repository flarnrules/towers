import subprocess
import json
import os
import datetime

# Constants for split percentages and memo
STAKE_PERCENTAGE = 0.25
LIQUID_PERCENTAGE = 0.24
SMOKERS_CLUB_PERCENTAGE = 0.01
COLLABORATORS_PERCENTAGE = 0.50
MEMO = ""
TRANSACTIONS_DIR = "/home/flarnrules/repos/towers/collections/2-proto_towers/code/data/transactions"
COLLABS_FILE_PATH = "/home/flarnrules/repos/towers/collections/2-proto_towers/code/data/collabs.json"
ROYALTIES_WALLET_ADDRESS = "stars1hyhmssn4j6fxlvq58ctlpxwg5az7shg7zc77rp" # royalties wallet
VALIDATOR_WALLET_ADDRESS = "starsvaloper10jm8fvdyqlj78w0j5nawc76wsn4pqmdx9vsdyy" # nos node
SMOKERS_CLUB_ADDRESS = "stars1mlxynkqd9js8tkdnkk0e27lgz7x9lt866n5r44" # ashtray?

# Collaborators' contributions
contributions = {
    'Jinxto': 7,
    'Fluffhead': 2,
    'Ajk': 3,
    'Randomkid': 3,
    'Berny': 2,
    'Votor': 1,
    'Quasimosos': 2,
    'Pajon': 6,
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
    command = ["starsd", "query", "bank", "balances", ROYALTIES_WALLET_ADDRESS]
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

    generate_json = input("Do you want to output royalties data as JSON? (y/n) ").strip().lower()
    if generate_json == 'y':
        output_royalties_json(royalties, date_input)
    
    generate_tx = input("Do you want to generate a transaction from the results? (y/n) ").strip().lower()
    if generate_tx == 'y':
        if not os.path.exists(COLLABS_FILE_PATH):
            print(f"Error: The file {COLLABS_FILE_PATH} does not exist.")
            return

        with open(COLLABS_FILE_PATH, 'r') as f:
            collab_addresses = json.load(f)

        # Timestamp for the transaction file
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        file_path = os.path.join(TRANSACTIONS_DIR, f'transaction_{timestamp}.json')

        transactions = []
        for name, amount in royalties.items():
            address = collab_addresses.get(name)
            if address:
                transaction = {
                    "@type": "/cosmos.bank.v1beta1.MsgSend",
                    "from_address": ROYALTIES_WALLET_ADDRESS,
                    "to_address": address,
                    "amount": [{
                        "denom": "ustars",
                        "amount": str(int(amount * 1_000_000))  # Convert to micro-units
                    }]
                }
                             
                transactions.append(transaction)
        
        smokers = {
                "@type": "/cosmos.bank.v1beta1.MsgSend",
                "from_address": ROYALTIES_WALLET_ADDRESS,
                "to_address": SMOKERS_CLUB_ADDRESS,
                "amount": [{
                    "denom": "ustars",
                    "amount": str(int(smokers_club_amount * 1_000_000))
                }]
            }
        
        
        stake = {
                "@type": "/cosmos.staking.v1beta1.MsgDelegate",
                "delegator_address": ROYALTIES_WALLET_ADDRESS,
                "validator_address": VALIDATOR_WALLET_ADDRESS,
                "amount": {
                    "denom": "ustars",
                    "amount": str(int(stake_amount * 1_000_000))
                }
            }
        transactions.append(stake)


        transactions.append(smokers)

        # Generate the transaction file
        transaction_data = {
            "body": {
                "messages": transactions,
                "memo": "automation success?",
                "timeout_height": "0",
                "extension_options": [],
                "non_critical_extension_options": []
            },
            "auth_info": {
                "signer_infos": [],
                "fee": {
                    "amount": [{"denom": "ustars", "amount": "600000"}],
                    "gas_limit": "600000",
                    "payer": "",
                    "granter": ""
                }
            },
            "signatures": []
        }

        with open(file_path, 'w') as f:
            json.dump(transaction_data, f, indent=4)

        print(f"Transaction file generated and saved to {file_path}")
        print(file_path)

def output_royalties_json(royalties, date_input):
    # Ensure the directory for output exists
    os.makedirs(TRANSACTIONS_DIR, exist_ok=True)

    # Define file path
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    output_path = os.path.join(TRANSACTIONS_DIR, f'royalties_{timestamp}.json')

    # Structure the data
    royalties_data = []
    for collaborator, amount in royalties.items():
        royalties_data.append({
            "collaborator": collaborator,
            "amount": amount,
            "memo": MEMO,
            "date": date_input
        })

    # Write the JSON output to a file
    with open(output_path, 'w') as f:
        json.dump(royalties_data, f, indent=4)

    print(f"Royalties data saved to {output_path}")


calculate_royalties()

