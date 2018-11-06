# Yerim Dia
# November 2, 2018
# Introduction to Computer Science
#  This program is based on the rotation cipher. It re-sequences the alphabet depending on the desired shift.
# This program allows the user to either decode or encode a word or phrase or to quit the program


def user_choice():
    """
    This function gets the choice from the user either to encode, decode or to quit the program
    :return: It returns the user choice either by 'e', 'd', or 'q'
    """
    while True:
        user_choice = input("Press 'e' to encode, 'd' to decode, or 'q' to quit:")
        if user_choice == 'e' or user_choice == 'd' or user_choice == 'q':
            return user_choice


def user_phrase():
    """
    This function gets the phrase that the user wants
    :return: It returns the user's desired phrase as a string
    """
    user_phrase = input("What phrase do you want to use:")
    return user_phrase


def main():
    choice = user_choice()

    if choice == 'e':
        phrase = user_phrase()
        key = int(input("By what key between (0-24) do you want to shift:"))
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        first = alphabet[key:]
        last = alphabet[0:key]
        final = first + last
        encoded = ""
        for x in phrase:
            if x == " ":
                encoded = encoded + " "
            else:
                bet = alphabet.index(x)
                end = final[bet]
                encoded = encoded + end
        print(encoded)
    elif choice == 'd':

            key = int(input("By what key between (0-24) do you want to shift:"))
            alphabet = 'abcdefghijklmnopqrstuvwxyz'
            first = alphabet[key:]
            last = alphabet[0:key]
            final = first + last
            phrase = user_phrase()
            decoded = ""
            for x in phrase:
                if x == " ":
                    decoded = decoded + " "
                else:
                    bet = final.index(x)
                    end = alphabet[bet]
                    decoded = decoded + end
            print(decoded)
    elif choice == 'q':
        print("See you later")


main()
