from query import query_collection

# Update this if major changes are made
pricing_model_version = "0.07"


# Define the necessary functions
def get_size_multiplier(width, height):
    size_multipliers = {
        (8, 8): 1.05,
        (16, 16): 1.10,
        (32, 32): 1.20,
        (64, 64): 1.30,
        (128, 128): 1.40
    }
    return size_multipliers.get((width, height), 1)  # Default to 1 if size not predefined

def get_animation_bonus(is_animation):
    return 1.25 if is_animation else 1

def get_pride_multiplier(pride_factor):
    pride_multipliers = {
        1: 1,
        2: 1.02,
        3: 1.05
    }
    return pride_multipliers.get(pride_factor, 1)  # Default to 1 if pride factor is not valid

def calculate_base_price(best_offer, floor_price):
    return (best_offer + floor_price) / 2

def calculate_final_price(best_offer, floor_price, width, height, is_animation, pride_factor):
    base_price = calculate_base_price(best_offer, floor_price)
    size_multiplier = get_size_multiplier(width, height)
    animation_bonus = get_animation_bonus(is_animation)
    pride_multiplier = get_pride_multiplier(pride_factor)
    
    final_multiplier = 1 + (size_multiplier-1) + (animation_bonus-1) + (pride_multiplier-1)
    final_price = base_price * final_multiplier
    
    return final_price, base_price, final_multiplier

def get_pricing_method(is_animation):
    return "Auction" if is_animation else "Sale"

# Main execution block
try:
    floor_price, best_offer = query_collection()
except Exception as e:
    print(f"Error fetching data from query: {e}")
    exit()

size_input = input("Size in pixels (i.e '16x16'): ")
is_animation_input = input("Is there animation? (yes/no): ")
pride_factor_input = input("Pride factor (1-3): ")

# Parse inputs
size_parts = size_input.split('x')
width = int(size_parts[0])
height = int(size_parts[1])
is_animation = is_animation_input.strip().lower() == 'yes'
pride_factor = int(pride_factor_input)

# Calculate prices and multipliers
final_price, base_price, final_multiplier = calculate_final_price(best_offer, floor_price, width, height, is_animation, pride_factor)

pricing_method = get_pricing_method(is_animation)

# Print detailed output with rounding
print("\n=== Pricing Calculation Details ===")
print(f"Version: {pricing_model_version}")
print(f"Floor Price: {floor_price:.2f} STARS")
print(f"Best Offer: {best_offer:.2f} STARS")
print(f"Base Price: ({best_offer:.2f} + {floor_price:.2f}) / 2 = {base_price:.2f} STARS")
print(f"Size Multiplier: {get_size_multiplier(width, height):.2f}")
print(f"Animation Bonus: {get_animation_bonus(is_animation):.2f}")
print(f"Pride Multiplier: {get_pride_multiplier(pride_factor):.2f}")
print(f"Final Multiplier: {final_multiplier:.2f}")
print(f"Calculated Price: {final_price:.2f} STARS")
print(f"Pricing Method: {pricing_method}")