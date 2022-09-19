from string import ascii_lowercase
from string import ascii_uppercase

print("Welcome to Alphaton, the programming language that only uses letters. It is case-sensitive. Type '?' for a list of commands.\n\nLatest Version: 0.3 on 19 Sep 2022")

chars = ascii_lowercase + ascii_uppercase + " .!?+-×÷\n\t"

i1 = 0
i2 = 0
i3 = 0
i4 = 0
i5 = 0
i6 = 0
i7 = 0
i8 = 0
i9 = 0
i10 = 0
i11 = 0
i12 = 0

saved = 0
carry = 0

ints = [i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11, i12]
id = 0

use = True
while use:
	
	print(f"\n\nData Integer Tape:\n{ints}\n\nCurrent D.I (Left -> Right): {id+1}\nSaved Value: {saved}")
	
	command = input("\nMain Command Line >")
	
	for char in command:
		
		if char == "?":
			print("\nA: Adds 1 to current integer.\nS: Subtracts 1 from current integer\nL: Move to the next integer to the left.\nR: Move to the next integer to the right.\nP: Prints corrosponding letter of alphabet. Type '*' for the list.\np: Prints current integer value.\nI: Asks for a number. Number will replace current integer value.\ni: Asks for a number. Number will be the selected value on tape.\nE: Resets current integer to 0.\ns: Saves current number to memory\nl: Loads saved number to current position, replacing the previous.\nZ: Transfers current value to the left.\nX: Transfers current value to the right.\nO: Opens loop if value of integer IS NOT 0.\nC: Closes loop if value of integer IS 0. (Loops are NOT stackable)")
			
		if char == "*":
			print("Alphabet list with corrosponding integer.\n\nA = 1\nB = 2\nC = 3\nD = 4\nE = 5\nF = 6\nG = 7\nH = 8\nI = 9\nJ = 10\nK = 11\nL = 12\nM = 13\nN = 14\nO = 15\nP = 16\nQ = 17\nR = 18\nS = 19\nT = 20\nU = 21\nV = 22\nW = 23\nX = 24\nY = 25\nZ = 26\nCapital letters are 27 -> 52\nSPACE = 53\n. = 54\n! = 55\n? = 56\n+ = 57\n- = 58\n× = 59\n÷ = 60\nNEW LINE = 61\nTAB = 62")
			
		if char == "A":
			ints[id] += 1
			
		if char == "S":
			ints[id] -= 1
			
		if char == "L":
			if id > 0:
				id -= 1
				
		if char == "R":
			if id < 11:
				id += 1
				
		if char == "P":
			if 1 <= ints[id] <= len(chars):
				print(chars[ints[id]-1], end="")
				
		if char == "p":
			print(ints[id], end="")
			
		if char == "I":
			ask = int(input("\nEnter an integer: "))
			ints[id] = ask
		
		if char == "i":
			ask = int(input("\nEnter a tape position: "))
			id = ask-1
			
		if char == "E":
			ints[id] = 0
			
		if char == "s":
			saved = ints[id]
			
		if char == "l":
			ints[id] = saved
			
		if char == "Z":
			carry = ints[id]
			ints[id] = 0
			if id > 0:
				id -= 1
			ints[id] = carry
			
		if char == "X":
			carry = ints[id]
			ints[id] = 0
			if id < 11:
				id += 1
			ints[id] = carry
	
		if char == "O":
			if ints[id] != 0:
				loop = input("\nLoop Command Line >")
				
				done = False
				
				while not done:
					
					for char2 in loop:
						
						if char2 == "A":
							ints[id] += 1
			
						if char2 == "S":
							ints[id] -= 1
			
						if char2 == "L":
							if id > 0:
								id -= 1
				
						if char2 == "R":
							if id < 11:
								id += 1
				
						if char2 == "P":
							if 1 <= ints[id] <= len(chars):
								print(chars[ints[id]-1], end="")
				
						if char2 == "p":
							print(ints[id], end="")
			
						if char2 == "I":
							ask = int(input("\nEnter an integer: "))
							ints[id] = ask
		
						if char2 == "i":
							ask = int(input("\nEnter a tape position: "))
							id = ask-1
			
						if char2 == "E":
							ints[id] = 0
			
						if char2 == "s":
							saved = ints[id]
			
						if char2 == "l":
							ints[id] = saved
			
						if char2 == "Z":
							carry = ints[id]
							ints[id] = 0
							if id > 0:
								id -= 1
							ints[id] = carry
			
						if char2 == "X":
							carry = ints[id]
							ints[id] = 0
							if id < 11:
								id += 1
							ints[id] = carry
						
						if char2 == "C":
							if ints[id] == 0:
								done = True
							else:
								continue
							if id > 0 or id < 11:
								done = True
							else:
								continue
