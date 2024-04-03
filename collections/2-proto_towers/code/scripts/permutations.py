# calculate the total number of permutations given an x, y and color quantity.

width = 32
height = 32
num_colors = 4

def calculate_permutations(width, height, num_colors):
    return num_colors ** (width * height)

total_permutations = calculate_permutations(width, height, num_colors)
print(f"Total number of permutations for a {width}x{height} grid with {num_colors} colors: {total_permutations}")
