def find_square_part_size(grid_size, parts):
    width, height = grid_size  # Assuming a square grid

    # Calculate the total number of squares that can fit into the grid
    total_squares = width * height // parts

    # The side of each square part will be the square root of the total_squares
    part_side = int(total_squares ** 0.5)

    return part_side, part_side

# Usage example
grid_size = (768, 768)  # width, height
parts = int(input("Enter the number of square parts to divide the grid into: "))
part_width, part_height = find_square_part_size(grid_size, parts)

print(f"Each square part size: {part_width}x{part_height} pixels")

x = 16
y = x
calculate_squares = x * y
print(calculate_squares)