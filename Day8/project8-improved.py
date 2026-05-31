import string

# Using Python's built-in lowercase alphabet string is cleaner than typing it manually
ALPHABET = string.ascii_lowercase


def encode_or_decode(message, shift, encrypt=True):
    # If we are decrypting, we just shift backwards!
    if not encrypt:
        shift = -shift

    output = []

    for letter in message.lower():
        # Check if the character is a letter
        if letter.isalpha():
            current_index = ALPHABET.index(letter)

            # Add the shift and use modulo 26 to automatically wrap around 'z' to 'a'
            new_index = (current_index + shift) % 26
            output.append(ALPHABET[new_index])
        else:
            # Keep spaces, numbers, and punctuation exactly as they are
            output.append(letter)

    return "".join(output)


def prompt_user(prompt, validation=None):
    # (Your prompt_user function remains exactly the same, it is great!)
    while True:
        user_input = input(prompt).lower()

        if validation is None:
            return user_input
        elif isinstance(validation, int):
            try:
                return int(user_input)
            except ValueError:
                print("Please enter a number")
        elif isinstance(validation, list):
            try:
                assert user_input in validation
                return user_input
            except AssertionError:
                print("Please enter a valid input like:", *validation, sep=", ")


while True:
    is_encrypt = prompt_user("Type 'encode' to encrypt, type 'decode' to decrypt:\n", ["encode", "decode"])
    message = prompt_user("Type your message:\n")
    shift_number = prompt_user("Type the shift number:\n", 0)

    # Simplified the boolean logic here
    is_encoding = (is_encrypt == "encode")

    output_message = encode_or_decode(message, shift_number, encrypt=is_encoding)

    prefix = "encoded" if is_encoding else "decoded"
    print(f"Here's the {prefix} result: {output_message}")

    go_again = prompt_user("Type 'yes' if you want to go again. Otherwise type 'no'.\n", ["yes", "no"])
    if go_again == "no":
        break