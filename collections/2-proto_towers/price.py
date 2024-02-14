# proto towers pricing model
# version 0.01

best_offer_input = input("Best offer: ")
floor_price_input = input("Floor price: ")
size_input = input("Size in pixels (i.e '16x16'): ")
is_animation_input = input("Is there animation? (yes/no): ")
id_number_input = input("Proto Tower ID #: ")

# type cast so everything works
try:
    BEST_OFFER = float(best_offer_input)
    FLOOR_PRICE = float(floor_price_input)
    SIZE = size_input.split('x')
    WIDTH, HEIGHT = int(SIZE[0]), int(SIZE[1])
    IS_ANIMATION = True if is_animation_input.lower() == 'yes' else False
    ID_NUMBER = int(id_number_input)
except ValueError:
    print("Please enter valid numbers for bids and sizes.")
    exit()

# determine formula based on inputs
def calculate_price(best_offer, floor_price, width, height, is_animation):
    if width == 8 and height == 8:
        return best_offer * 1
    elif width == 16 and height == 16:
        return best_offer * 1.1
    elif width == 32 and height == 32:
        return best_offer * 1.25
    elif width == 64 and height == 64:
        return floor_price
    elif width == 128 and height == 128 or is_animation:
        id_number = ID_NUMBER
        return id_number + 10
    else:
        print("Invalid size. No pricing rule matched.")
        return None

# calculate and display list price
price = calculate_price(BEST_OFFER, FLOOR_PRICE, WIDTH, HEIGHT, IS_ANIMATION)
if price is not None:
    print(f"The price for your configuration is: {price}")
else:
    print("Could not calculate the price due to an error.")
