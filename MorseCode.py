morse_mapping = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
}
msg_entry = ""
while msg_entry != "q":
    morse_code = ""
    msg_entry = input("Enter Message or q to quit : ")
    if msg_entry == "q":
        break
    else:
        if msg_entry.isalnum():
            msg_entry = msg_entry.upper()
            for letter in msg_entry:
                if letter != " ":
                    morse_code += morse_mapping[letter] + " "
                else:
                    morse_code += "   "
        else:
            print(
                "Invalid Character in String - Only letters and numbers are supported - please try again"
            )
            continue
        print(morse_code)

