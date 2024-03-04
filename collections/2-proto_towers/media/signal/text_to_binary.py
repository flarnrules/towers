def binary_to_text_block(binary):
    # Split the binary string into an array of binary characters by space, then convert each to text
    text_result = ''.join(chr(int(b, 2)) for b in binary.split(' '))
    return text_result

# Replace the placeholder below with your space-delimited binary string
binary_input = "00100000"
text_output = binary_to_text_block(binary_input)

print("Original text from binary:")
print(text_output)
