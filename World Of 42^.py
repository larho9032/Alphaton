import os
import time

count = 0
prestige1 = 1
prestige2 = 1
limit = 42**prestige2

game = True
while game:
	
	click = input(f"<World Of 42^ 1.0>\n\nCount: {count}\nPrestige Level: {prestige1}\nSuper Prestige Level: {prestige2}\nCount & Prestige Level Limit: {limit}\n\nENTER: Game Tick | p1: Prestige | p2: Super Prestige\n\n>")
	
	if count < limit:
		for i in range(prestige1):
			if count < limit:
				count += 1
		
	if click == "p1":
		if count == limit:
			if prestige1 < limit:	
				count = 0
				prestige1 += 1
		
	if click == "p2":
		if count == limit:
			if prestige1 == limit:
				count = 0
				prestige1 = 1
				prestige2 += 1
				
	limit = 42**prestige2
	
	os.system("cls" if os.name == "nt" else "clear")
