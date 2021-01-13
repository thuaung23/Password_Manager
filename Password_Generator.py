import string
import random

'''
 This program generates a password that consists 6 letters, 10 numbers and 3 special characters.
 Import string and random for getting random alphabets and numbers + shuffling.
'''

SYMBOLS = ["!", "@", "#", "$", "%", "^", "&", "*"]


class PasswordGenerator:

    def __init__(self):
        # Create empty list to hold all alphabets, numbers and a special character as strings.
        self.pwd_list = []
        # Create empty string for later joining strings in list.
        self.pwd = ""

    # Add 6 random letters from alphabets to the list.
    def mixed_letter(self):
        letter = list(string.ascii_lowercase)
        random.shuffle(letter)
        for i in range(6):
            # For heightened security, make 3 letters upper cases.
            if i == 1 or i == 3 or i == 5:
                self.pwd_list.append(letter[i].capitalize())
            else:
                self.pwd_list.append(letter[i])

    # Add 10 random numbers as strings to the list.
    def mixed_num(self):
        for i in range(11):
            num = random.randint(0, 9)
            self.pwd_list.append(str(num))

    # Add 3 random symbols to the list.
    def mixed_char(self):
        for i in range(3):
            char = random.choice(SYMBOLS)
            self.pwd_list.append(char)

    def password_generator(self):
        self.mixed_letter()
        self.mixed_num()
        self.mixed_char()
        # Shuffle the list and join them together.
        random.shuffle(self.pwd_list)
        return ''.join(self.pwd_list)
