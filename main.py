from morse_code import morse_code


def get_keys_from_value(d, val):
    return [k for k, v in d.items() if v == val][0]


choice = int(input("What would you like to do:\n1. translate morse code into text\n2. translate text into morse code\n"))

if choice == 1:
    code_to_translate = input("Enter the morse code letters separated by spaces and words by \\ : ").replace(" / ", " /")
    letter_to_translate = ''
    completed_text = []
    letter = ''
    for ch in code_to_translate + ' ':
        if ch == '.' or ch == '-':
            letter_to_translate += ch
        elif ch == ' ':
            letter = get_keys_from_value(morse_code, letter_to_translate)
            letter_to_translate = ''
            completed_text.append(letter)
            letter = ''
        elif ch == '/':
            completed_text.append(" ")
        else:
            pass

    separator = ''
    print(separator.join(completed_text))

elif choice == 2:
    sentence_to_translate = input("Enter the text you want to translate into the morse code: ").lower()
    completed_morse_code = [morse_code[letter] for letter in sentence_to_translate]
    separator = ' '
    print(separator.join(completed_morse_code))








