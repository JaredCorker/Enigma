# Initial Test Version of Enigma

class Rotor():
    def __init__(self, wiring, position):
        self.alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        self.wiring = wiring
        self.position = position
        self.reversed = wiring[::-1]

    def rotate(self):
        self.alphabet = [self.alphabet[-1]] + self.alphabet[:-1]
        self.wiring = [self.wiring[-1]] + self.wiring[:-1]
        self.position += 1
        if self.position == 27:
            self.position = 1

    def return_char(self, char):
        return self.wiring[self.alphabet.index(char)]
    
    def return_char_reverse(self, char):
        index = self.wiring.index(char)
        return self.alphabet[index] 

    def reset_position(self):
        while(self.position != 1):
            self.rotate()


class Enigma():
    def __init__(self, rotor_one, rotor_two, rotor_three, reflector):
        self.rotor_one = rotor_one
        self.rotor_two = rotor_two
        self.rotor_three = rotor_three
        self.reflector = reflector

    def process_char(self, char):
            char = rotor_one.return_char(char)
            char = rotor_two.return_char(char)
            char = rotor_three.return_char(char)
            char = reflector.return_char(char)
            char = rotor_three.return_char_reverse(char)
            char = rotor_two.return_char_reverse(char)
            char = rotor_one.return_char_reverse(char)

            self.rotor_one.rotate()
            if self.rotor_one.position == 1:
                self.rotor_two.rotate()
                if self.rotor_two.position == 1:
                    self.rotor_three.rotate()

            return char

    def encrypt(self, message):
        output = ""
        message = message.upper()
        for char in message:
            output += self.process_char(char)
        return output

rotor_one = Rotor(list('EKMFLGDQVZNTOWYHXUSPAIBRCJ'), 1)
rotor_two = Rotor(list('AJDKSIRUXBLHWTMCQGZNPYFVOE'), 1)
rotor_three = Rotor(list('BDFHJLCPRTXVZNYEIWGAKMUSQO'), 1)
reflector = Rotor(list('EJMZALYXVBWFCRQUONTSPIKHGD'), 1)
enig = Enigma(rotor_one, rotor_two, rotor_three, reflector)
message = enig.encrypt("AAA")
print(enig.encrypt("AAA"))
print(enig.encrypt(message))
