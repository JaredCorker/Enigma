# Initial Test Version of Enigma

alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

class Rotor():
    def __init__(self, wiring, position):
        self.wiring = wiring
        self.position = position
        self.reversed = wiring[::-1]

    def rotate(self):
        self.wiring = [self.wiring[-1]] + self.wiring[:-1]
        self.position += 1
        if self.position == 27:
            self.position = 1

    def return_letter(self, letter):
        return self.wiring[alphabet.index(letter)]
    
    def return_letter_reverse(self, letter):
        index = self.wiring.index(letter)
        return alphabet[index] 

    def reset_position(self):
        while(self.position != 1):
            self.rotate()


class Enigma():
    def __init__(self, rotor_one, rotor_two, rotor_three, reflector):
        self.rotor_one = rotor_one
        self.rotor_two = rotor_two
        self.rotor_three = rotor_three
        self.reflector = reflector

    def encrypt(self, message):
        output = ""
        message = message.upper()
        for char in message:
            char = rotor_one.return_letter(char)
            char = rotor_two.return_letter(char)
            char = rotor_three.return_letter(char)
            char = reflector.return_letter(char)
            char = rotor_three.return_letter_reverse(char)
            char = rotor_two.return_letter_reverse(char)
            char = rotor_one.return_letter_reverse(char)
            output += char

        return output

rotor_one = Rotor(list('EKMFLGDQVZNTOWYHXUSPAIBRCJ'), 1)
rotor_two = Rotor(list('AJDKSIRUXBLHWTMCQGZNPYFVOE'), 1)
rotor_three = Rotor(list('BDFHJLCPRTXVZNYEIWGAKMUSQO'), 1)
reflector = Rotor(list('EJMZALYXVBWFCRQUONTSPIKHGD'), 1)
enig = Enigma(rotor_one, rotor_two, rotor_three, reflector)
message = enig.encrypt("Hello")
print(enig.encrypt("Hello"))
print(enig.encrypt(message))
