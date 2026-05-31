alphabet = list("abcdefghijklmnopqrstuvwxyz")

def encode_or_decode(message, shift, encrypt= True):
    if shift > 26:
        shift = shift % 26

    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    output = []

    for letter in message.lower():
        if not letter.isalpha():
            output.append(letter)
        else:
            index = alphabet.index(letter) if encrypt else shifted_alphabet.index(letter)
            output.append(shifted_alphabet[index]) if encrypt else output.append(alphabet[index])
    return "".join(output)


def prompt_user(prompt, validation=None):
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

    output_message = encode_or_decode(message, shift_number, encrypt=True if is_encrypt=="encode" else False)
    print(f"Here's the encoded result: {output_message}" if is_encrypt=="encode" else f"Here's the decoded result: {output_message}")

    go_again = prompt_user("Type 'yes' if you want to go again. Otherwise type 'no'.\n", ["yes", "no"])

    if go_again == "no":
        break