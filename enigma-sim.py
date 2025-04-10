import random
import string

class ROTOR:
	def __init__(self, current_value=1, wiring=False):
		self.current_value = current_value
		if not wiring:
			self.wiring = self.generate_wiring()
		else:
			self.wiring = wiring
	
	@staticmethod
	def generate_wiring():
   	 letters = list(string.ascii_uppercase)
 	   shuffled_letters = letters.copy()

   	 while True:
      	  random.shuffle(shuffled_letters)
    	    if all(a != b for a, b in zip(letters, shuffled_letters)):
       	     break

   	 return dict(zip(letters, shuffled_letters))

class RING:
	def __init__(self, notch=[26]):
		self.notch = notch

class ENIGMA_MACHINE:
	def __init__(self, configurations):
		self.configurations = configurations
		self.configurations_copy = configurations
		self.rotor1, self.rotor2, self.rotor3 = [self.configurations["rotor_order"][i] for i in range(3)]
		self.ring1, self.ring2 = [self.configurations["ring_setting"][i] for i in range(2)]
		self.reflector = {
    'A': 'Y', 'B': 'R', 'C': 'U', 'D': 'H', 'E': 'Q', 'F': 'S', 'G': 'L',
    'H': 'D', 'I': 'P', 'J': 'X', 'K': 'N', 'L': 'G', 'M': 'O', 'N': 'K',
    'O': 'M', 'P': 'I', 'Q': 'E', 'R': 'B', 'S': 'F', 'T': 'Z', 'U': 'C',
    'V': 'W', 'W': 'V', 'X': 'J', 'Y': 'A', 'Z': 'T'
}
		self.plugboard = self.configurations["plugboard_connections"]

	def updateMachine(self):
		if self.rotor2.current_value in self.ring2.notch:
			self.rotor3.turn()
			if self.rotor1.current_value in self.ring1.notch:
				self.rotor2.turn()
		self.rotor1.turn()
		return None

	def encrypt(self, text):
		cipher = ""
		temp = ""

		for letter in list(text.upper()):
			print(letter, end=" -> ")
			if letter in self.plugboard:
				temp = self.plugboard[letter]
			elif letter in (reversed_pluboard:={value: key for key, value in self.plugboard.items()}):
				temp = reversed_pluboard[letter]
			else:
				temp = letter
			print(temp, end=" -> ")
			temp = self.rotor1.wiring[chr((((ord(temp) - 65) + (self.rotor1.current_value - 1)) % 26) + 65) if self.rotor1.current_value != 1 else temp]
			print(temp, end=" -> ")
			temp = self.rotor2.wiring[chr((((ord(temp) - 65) + (self.rotor2.current_value - 1)) % 26) + 65) if self.rotor2.current_value != 1 else temp]
			print(temp, end=" -> ")
			temp = self.rotor3.wiring[chr((((ord(temp) - 65) + (self.rotor3.current_value - 1)) % 26) + 65) if self.rotor3.current_value != 1 else temp]
			print(temp, end=" -> ")
			
			reversed_rotor1 = ROTOR(current_value=rotor1.current_value, wiring={value: key for key, value in rotor1.wiring.items()})
			reversed_rotor2 = ROTOR(current_value=rotor2.current_value, wiring={value: key for key, value in rotor2.wiring.items()})
			reversed_rotor3 = ROTOR(current_value=rotor3.current_value, wiring={value: key for key, value in rotor3.wiring.items()})
			
			temp = self.reflector[temp]
			print(temp, end=" -> ")
			temp = reversed_rotor3.wiring[chr((((ord(temp) - 65) + (reversed_rotor3.current_value - 1)) % 26) + 65) if reversed_rotor3.current_value != 1 else temp]
			print(temp, end=" -> ")
			temp = reversed_rotor2.wiring[chr((((ord(temp) - 65) + (reversed_rotor2.current_value - 1)) % 26) + 65) if reversed_rotor2.current_value != 1 else temp]
			print(temp, end=" -> ")
			temp = reversed_rotor1.wiring[chr((((ord(temp) - 65) + (reversed_rotor1.current_value - 1)) % 26) + 65) if reversed_rotor1.current_value != 1 else temp]
			print(temp, end=" -> ")
			if temp in self.plugboard:
				temp = self.plugboard[temp]
			elif temp in (reversed_pluboard:={value: key for key, value in self.plugboard.items()}):
				temp = reversed_pluboard[temp]
			print(temp)
			self.updateMachine()
			cipher += temp
		
		return cipher

	def reset(self):
		self.rotor1.current_value, self.rotor2.current_value, self.rotor3.current_value = self.configurations_copy["rotor_starting_positions"]
		return None

if __name__ == "__main__":
	rotor1, rotor2, rotor3, rotor4, rotor5 = [ROTOR() for _ in range(5)]
	ring1, ring2 = [RING() for _ in range(2)]
	plugboard = { "A" : "D", "C" : "Z", "G" : "R" }

	# Temporary hardcoded rotors
	rotor1.wiring = {'A': 'W', 'B': 'Q', 'C': 'U', 'D': 'L', 'E': 'F', 'F': 'P', 'G': 'A', 'H': 'J', 'I': 'C', 'J': 'I', 'K': 'M', 'L': 'X', 'M': 'V', 'N': 'O', 'O': 'D', 'P': 'S', 'Q': 'R', 'R': 'N', 'S': 'K', 'T': 'E', 'U': 'H', 'V': 'Z', 'W': 'T', 'X': 'G', 'Y': 'B', 'Z': 'Y'}
	rotor2.wiring = {'A': 'K', 'B': 'A', 'C': 'R', 'D': 'W', 'E': 'J', 'F': 'I', 'G': 'U', 'H': 'Y', 'I': 'D', 'J': 'Z', 'K': 'L', 'L': 'F', 'M': 'P', 'N': 'M', 'O': 'Q', 'P': 'G', 'Q': 'X', 'R': 'S', 'S': 'O', 'T': 'V', 'U': 'T', 'V': 'B', 'W': 'E', 'X': 'C', 'Y': 'H', 'Z': 'N'}
	rotor3.wiring = {'A': 'G', 'B': 'A', 'C': 'I', 'D': 'X', 'E': 'Q', 'F': 'R', 'G': 'W', 'H': 'K', 'I': 'J', 'J': 'P', 'K': 'M', 'L': 'S', 'M': 'F', 'N': 'B', 'O': 'D', 'P': 'V', 'Q': 'Y', 'R': 'T', 'S': 'Z', 'T': 'H', 'U': 'L', 'V': 'U', 'W': 'E', 'X': 'C', 'Y': 'O', 'Z': 'N'}

	configurations = {
		"rotor_order" : [rotor1, rotor2, rotor3],
		"ring_setting" : [ring1, ring2],
		"rotor_starting_positions": [1, 1, 1],
		"plugboard_connections": plugboard
	}

	christopher = ENIGMA_MACHINE(configurations)
	print((en:=christopher.encrypt("hello")))
	christopher.reset()
	print(christopher.encrypt(en))
