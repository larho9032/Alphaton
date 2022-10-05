from string import ascii_lowercase
from string import ascii_uppercase
from random import randint
import math

print("Welcome to Alphaton, the programming language that only uses letters for main commands. It is case-sensitive. Type '?' for a list of commands.\n\nLatest Version: 0.6 on 3 Oct 2022")

chars = ascii_lowercase + ascii_uppercase + " .!?+-×÷\n\t"

value = 0

cell_count = 15

saved = 0
carry = 0
temp = 0

saved_string = "None"

ints = [value] * cell_count # The memory tape
id = 0

def func(char):
	if char == "A":
		ints[id] += 1

	elif char == "S":
		ints[id] -= 1

	elif char == "M":
		ints[id] *= saved

	elif char == "D":
		ints[id] //= saved

	elif char == "m":
		print("\n1: Exponent of current value with saved value.\n2: Square root of current value as integer.\nELSE: Return to main interpreter.")
		_input = input("\nChoose a math function >")

		if _input == "1":
			ints[id] = ints[id] ** saved

		elif _input == "2":
			ints[id] = int(math.sqrt(ints[id]))
		
		del _input # Deletes the _input variable (it is not needed)

	elif char == "r":
		min = int(input("\nMinimum Int >"))
		max = int(input("\nMaximum Int >"))

		ints[id] = randint(min,max)

	elif char == "L":
		if id > 0:
			id -= 1

	elif char == "R":
		if id < cell_count - 1:
			id += 1

	elif char == "P":
		if 1 <= ints[id] <= len(chars):
			print(chars[ints[id]-1], end="")

	elif char == "p":
		print(ints[id], end="")

	elif char == "I":
		ints[id] = int(input("\nEnter an integer >"))

	elif char == "i":
		id = int(input("\nEnter a tape position >"))-1

	elif char == "E":
		ints[id] = 0

	elif char == "s":
		saved = ints[id]

	elif char == "l":
		ints[id] = saved

	elif char == "e":
		saved = 0

	elif char == "Z":
		carry = ints[id]
		ints[id] = 0
		if id > 0:
			id -= 1
		ints[id] = carry

	elif char == "X":
		carry = ints[id]
		ints[id] = 0
		if id < 11:
			id += 1
		ints[id] = carry

	elif char == "c":
		cell_count = int(input("\nEnter a new cell count >"))

		ints = [value] * cell_count
	
while True:
	
	print(f"\n\nData Integer Tape:\n{ints}\n\nCurrent Data Integer (Left -> Right): {id+1}\nCell Count: {cell_count}\nSaved Value: {saved}")
	
	command = input("\nMain Command Line >")
	
	for char in command:
		
		func(char)
			
		if char == "?":
			print("\nA: Adds 1 to current integer.\nS: Subtracts 1 from current integer\nM: Multiplies current integer by saved value.\nD: Floor divides the current integer by the saved value.\nm: Advanced math functions.\nr: 2 integers needed. Random number will be selected from range.\nL: Move to the next integer to the left.\nR: Move to the next integer to the right.\nP: Prints corrosponding letter of alphabet. Type '*' for the list.\np: Prints current integer value.\nI: Asks for a number. Number will replace current integer value.\ni: Asks for a number. Number will be the selected value on tape.\nE: Resets current integer to 0.\ns: Saves current number to memory\nl: Loads saved number to current position, replacing the previous.\ne: Clear saved value.\nZ: Transfers current value to the left.\nX: Transfers current value to the right.\nc: Asks for an integer. Integer will be no. of cells for memory.\nO: Opens loop if value of integer IS NOT 0.\nC: Closes loop if value of integer IS 0. (Loops are NOT stackable)")
	
		elif char == "O":
			if ints[id] != 0:
				loop = input("\nLoop Command Line >")
				
				while True:
					
					for char2 in loop:
						
						func(char2)
						
						if char2 == "C":
							if ints[id] == 0 or (id > 0 or id < cell_count - 1):
								break
							else:
								continue
