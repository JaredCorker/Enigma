# Initial Test Version of Enigma

letter_to_num = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4,
                'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
                'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14,
                'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19,
                'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24,
                'Z': 25 }
rotor_one = list('EKMFLGDQVZNTOWYHXUSPAIBRCJ')
rotor_two = list('AJDKSIRUXBLHWTMCQGZNPYFVOE')
rotor_three = list('BDFHJLCPRTXVZNYEIWGAKMUSQO')
reflector = list('EJMZALYXVBWFCRQUONTSPIKHGD')


class Rotor():
    def __init__(self, wiring, position):
        self.wiring = wiring
        self.position = position

    def rotate(self):
        self.wiring = [self.wiring[-1]] + self.wiring[:-1]
        self.position += 1
        if self.position == 27:
            self.position = 1

    def return_letter(self, letter):
        return self.wiring[letter_to_num[letter]]

    def reset_position(self):
        while(self.position != 1):
            self.rotate()


test = Rotor(rotor_one, 1)
test2 = Rotor(rotor_two, 1)
test3 = Rotor(rotor_three, 1)
test4 = Rotor(reflector, 1)
letter = test.return_letter('B')
letter = test2.return_letter(letter)
letter = test3.return_letter(letter)
letter = test4.return_letter(letter)
letter = test3.return_letter(letter)
letter = test2.return_letter(letter)
letter = test.return_letter(letter)
print(letter)
letter = test.return_letter('D')
letter = test2.return_letter(letter)
letter = test3.return_letter(letter)
letter = test4.return_letter(letter)
letter = test3.return_letter(letter)
letter = test2.return_letter(letter)
letter = test.return_letter(letter)
print(letter)
