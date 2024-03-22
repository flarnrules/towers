import datetime

# Constants for split percentages and memo
STAKE_PERCENTAGE = 0.25
LIQUID_PERCENTAGE = 0.24
SMOKERS_CLUB_PERCENTAGE = 0.01
COLLABORATORS_PERCENTAGE = 0.50
MEMO = "for collab 🏙️🌆"

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
    

    # Add more collaborators here
}

def calculate_next_tuesday(current_date):
    current_date = datetime.datetime.strptime(current_date, "%d/%m/%Y")
    next_tuesday = current_date + datetime.timedelta(days=(1 - current_date.weekday() + 7) % 7)
    return next_tuesday.strftime("%d/%m/%Y")

def calculate_royalties():
    # Getting the date (day/month/year)
    date_input = input("Enter the date (e.g., 1/9/2024): ")
    
    # Getting the wallet liquid contents
    liquid_contents = float(input("Enter the wallet liquid contents in STARS: "))
    
    total_contributions = sum(contributions.values())
    

    # Calculations for splits
    stake_amount = liquid_contents * STAKE_PERCENTAGE
    liquid_amount = liquid_contents * LIQUID_PERCENTAGE
    smokers_club_amount = liquid_contents * SMOKERS_CLUB_PERCENTAGE
    collaborators_amount = liquid_contents * COLLABORATORS_PERCENTAGE

    # Separator for formatting
    separator = "=" * 40
    print(f"\n{separator}\n{date_input} - wallet liquid contents = {liquid_contents} STARS")
    print("Split - 25% stake, 24% liquid, 1% to smokers club, 50% to collaborators")
    print(f"25% x {liquid_contents} = {stake_amount} Staked")
    print(f"24% x {liquid_contents} = {liquid_amount} Liquid")
    print(f"1% x {liquid_contents} = {smokers_club_amount} To Smoker's Club")
    print(f"50% x {liquid_contents} = {collaborators_amount} Collaborators")

    print("\n\nTotal collaborations:",total_contributions)

    print("\nBreakdown")
    for collaborator, num_nfts in contributions.items():
        collaborator_percentage = (num_nfts / total_contributions) * 100
        collaborator_amount = collaborators_amount * (num_nfts / total_contributions)
        print(f"{collaborator} - {collaborator_percentage:.2f}% x {collaborators_amount} = {collaborator_amount}")

    next_split_date = calculate_next_tuesday(date_input)
    print(f"\nNext split on {next_split_date}")
    print(f"memo: {MEMO}")
    print(f"{separator}")

calculate_royalties()
