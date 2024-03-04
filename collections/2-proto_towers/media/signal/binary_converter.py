def text_to_binary_block(text):
    # Convert each character into binary and join them with newline character
    binary_result = '\n'.join(format(ord(char), '08b') for char in text)
    return binary_result

# Example usage
text = "total car monkey apple choadz"
binary_text = text_to_binary_block(text)
print(f"Original text: {text}")
print("Binary representation (each character on a new line):")
print(binary_text)
