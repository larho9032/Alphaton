import os
import time

print("Welcome to Alphaton, the programming language that only uses letters. It is case-sensitive. Type '?' for a list of commands.\n\nLatest Version: 0.1 on 18 Sep 2022")

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

ints = [i1, i2, i3, i4, i5, i6, i7, i8, i9, i10]
id = 0

use = True
while use:
	
	print(f"\nData Integers: {ints}\nCurrent D.I (Left -> Right): {id+1}")
	
	command = input("\n>")
	
	for char in command:
		
		if char == "?":
			print("\nA: Adds 1 to current integer.\nS: Subtracts 1 from current integer\nL: Move to the next integer to the left.\nR: Move to the next integer to the right.\nP: Prints corrosponding letter of alphabet. Type 'l' for the list.\np: Prints current integer value.\nI: Asks for a number. Number will replace current integer value.\nE: Resets current integer to 0.")
			
		if char == "l":
			print("Alphabet list with corrosponding integer.\n\nA = 1\nB = 2\nC = 3\nD = 4\nE = 5\nF = 6\nG = 7\nH = 8\nI = 9\nJ = 10\nK = 11\nL = 12\nM = 13\nN = 14\nO = 15\nP = 16\nQ = 17\nR = 18\nS = 19\nT = 20\nU = 21\nV = 22\nW = 23\nX = 24\nY = 25\nZ = 26\nSPACE = 27\n. = 28\n! = 29\n? = 30")
			
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
			if ints[id] == 1:
				print("a", end="")
			
			if ints[id] == 2:
				print("b", end="")
			
			if ints[id] == 3:
				print("c", end="")
			
			if ints[id] == 4:
				print("d", end="")
			
			if ints[id] == 5:
				print("e", end="")
			
			if ints[id] == 6:
				print("f", end="")
			
			if ints[id] == 7:
				print("g", end="")
			
			if ints[id] == 8:
				print("h", end="")
			
			if ints[id] == 9:
				print("i", end="")
			
			if ints[id] == 10:
				print("j", end="")
			
			if ints[id] == 11:
				print("k", end="")
			
			if ints[id] == 12:
				print("l", end="")
			
			if ints[id] == 13:
				print("m", end="")
			
			if ints[id] == 14:
				print("n", end="")
			
			if ints[id] == 15:
				print("o", end="")
			
			if ints[id] == 16:
				print("p", end="")
			
			if ints[id] == 17:
				print("q", end="")
			
			if ints[id] == 18:
				print("r", end="")
			
			if ints[id] == 19:
				print("s", end="")
			
			if ints[id] == 20:
				print("t", end="")
			
			if ints[id] == 21:
				print("u", end="")
			
			if ints[id] == 22:
				print("v", end="")
			
			if ints[id] == 23:
				print("w", end="")
			
			if ints[id] == 24:
				print("x", end="")
			
			if ints[id] == 25:
				print("y", end="")
			
			if ints[id] == 26:
				print("z", end="")
			
			if ints[id] == 27:
				print(" ", end="")
			
			if ints[id] == 28:
				print(".", end="")
			
			if ints[id] == 29:
				print("!", end="")
			
			if ints[id] == 30:
				print("?", end="")
				
		if char == "p":
			print(ints[id])
			
		if char == "I":
			ask = int(input("Enter an integer: "))
			ints[id] = ask
			
		if char == "E":
			ints[id] = 0