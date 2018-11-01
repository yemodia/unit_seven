def user_choice():
    while True:
        user_choice = input("Press 'e' to encode, 'd' to decode, or 'q' to quit:")
        if user_choice == 'e' or user_choice == 'd':
            break
        elif user_choice == 'q':
            print("See you later then")
            break
    return user_choice

def user_phrase():
    user_phrase = input("What phrase do you want to use:")
    return user_phrase

def index():



def main():
    user_choice()
    key = int(input("By what key between (0-24) do you want to shift:"))
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    first = alphabet[key:]
    last = alphabet[0:key]
    final = first + last
    print(final)
    phrase = user_phrase()
    for x in phrase:
        index = alphabet.index(x)
        new_letter = final[index]
        encoded_phrase = encoded_phrase + new_letter




main()
