

from itertools import permutations

def decrypt(message, key):

    i = 0
    decrypted_message = ""
    for ch in message:

        decrypted_message += chr(ch ^ key[i])

        i = (i + 1) % 3

    return decrypted_message

def is_plain_text(message):
    if all(x.isalpha() or x.isspace() for x in message):
        return True
    return False

with open("message.txt") as message:

    code = list(map(int, message.readline().strip().split(',')))

    # all lower case characters 

    lower_case_chars = [i for i in range(97, 123)]

    possible_permutations = list(permutations(lower_case_chars, r=3))

    i = 0

    for p in possible_permutations:

        message = decrypt(code, p)

        if is_plain_text(message):
            print(message)
