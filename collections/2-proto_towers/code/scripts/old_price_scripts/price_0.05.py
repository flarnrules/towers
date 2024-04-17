# proto towers pricing model
from query import query_collection

pricing_model_version = "0.05"

try:
    floor_price, best_offer = query_collection()
except Exception as e:
    print(f"Error fetching data from query: {e}")
    exit()

best_offer_input = best_offer
floor_price_input = floor_price
size_input = input("Size in pixels (i.e '16x16'): ")
is_animation_input = input("Is there animation? (yes/no): ")

# type cast so everything works
try:
    BEST_OFFER = float(best_offer_input)
    FLOOR_PRICE = float(floor_price_input)
    SIZE = size_input.split('x')
    WIDTH, HEIGHT = int(SIZE[0]), int(SIZE[1])
    IS_ANIMATION = True if is_animation_input.lower() == 'yes' else False
except ValueError:
    print("Please enter valid numbers for bids and sizes.")
    exit()


# determine formula based on inputs
def calculate_price(best_offer, floor_price, width, height, is_animation, pride_factor):
    # Calculate the base price as a starting point - using floor price or best offer as base depending on context
    base_price = (best_offer + floor_price) / 2  # Starting with best offer as the base for further calculations

    # Adjust size multipliers to ensure larger canvases are priced higher
    size_multiplier = 1  # Start with 1 for no change
    if width == 8 and height == 8:
        size_multiplier = 1.05
    elif width == 16 and height == 16:
        size_multiplier = 1.10
    elif width == 32 and height == 32:
        size_multiplier = 1.20
    elif width == 64 and height == 64:
        size_multiplier = 1.30
    elif width == 128 and height == 128:
        size_multiplier = 1.40
    
    # Animation bonus applies as an additional percentage
    animation_bonus = 1.25 if is_animation else 1  # 25% increase for animations
    
    # Pride factor adjustment
    pride_multiplier = 1  # Default to 1 for no change
    if pride_factor == 2:
        pride_multiplier = 1.02  # 2% boost
    elif pride_factor == 3:
        pride_multiplier = 1.05  # 5% boost

    # Combine the multipliers for the final price calculation
    final_multiplier = 1 + (size_multiplier-1) + (animation_bonus-1) + (pride_multiplier-1)
    final_price = base_price * final_multiplier
    print(f"The final multiplier for this piece is: {final_multiplier}")

    return final_price, size_multiplier, animation_bonus, pride_multiplier, base_price

# Add an input for the pride factor
pride_factor_input = input("Pride factor (1-3): ")
try:
    PRIDE_FACTOR = int(pride_factor_input)
except ValueError:
    print("Please enter a valid number for the pride factor.")
    exit()

# Ensure pride factor is within the expected range
if PRIDE_FACTOR not in [1, 2, 3]:
    print("Pride factor must be between 1 and 3.")
    exit()

# calculate and display list price
price = calculate_price(BEST_OFFER, FLOOR_PRICE, WIDTH, HEIGHT, IS_ANIMATION, PRIDE_FACTOR)
if price is not None:
    print(f"The price for your configuration is: {price}")
else:
    print("Could not calculate the price due to an error.")

# Calculate intermediate values for display
base_price = (best_offer + floor_price) / 2
final_multiplier = size_multiplier * animation_bonus * pride_multiplier
final_price = base_price * final_multiplier

# Print the detailed formula and its components
print("\n=== Detailed Pricing Formula ===")
print(f"Base Price (Average of Best Offer and Floor Price): ({best_offer} STARS + {floor_price} STARS) / 2 = {base_price:.2f} STARS")
print(f"Multipliers - Size: {size_multiplier}, Animation: {animation_bonus}, Pride: {pride_multiplier}")
print(f"Final Multiplier: {final_multiplier:.2f}")
print(f"Calculated Price: {base_price:.2f} STARS * {final_multiplier:.2f} = {final_price:.2f} STARS")
print(f"The price for your configuration is: {final_price:.2f} STARS")