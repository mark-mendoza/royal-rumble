# Royal Rumble
import random

# Identifying how many and who is going in on the Royal Rumble
# Prompting user how many people are placing bets
def participants ():
	temp_participants = input("How many participants are entering: ")
	while (not(temp_participants.isnumeric()) or int(temp_participants) == 0):
		temp_participants = input("Invalid input. How many participants are entering: ")
	return temp_participants

# Prompting for the names of the participants
def names_of_entrants (num_of_participants):
	entrants = []
	for j in range(1, int(num_of_participants) + 1):
		name = input(f"Name of participant {j}: ")
		entrants.append(name)
	return entrants

# Entering how many picks per person
def picks_per_person(num_of_rum_entrants, num_of_participants, entrants):
	temp = []
	temp_total = 0
	while temp_total < int(num_of_rum_entrants):
		for i in range(1, int(num_of_participants) + 1):
			temp_entrant = entrants[i - 1]
			num_of_picks = input(f"How many picks does participant {temp_entrant} have: ")
			while (not(num_of_picks.isnumeric()) or int(num_of_picks) == 0):
				# Validating the input is valid input. Has to be a number within the bounds
				num_of_picks = input(f"Invalid input. How many picks does participant {temp_entrant} have: ")
			temp.append(num_of_picks)
			temp_total += int(num_of_picks)
		# Will start process over if total number of picks is less than the total amount entered in by the user
		if temp_total > int(num_of_rum_entrants):
			print("Invalid total number of picks. Please re-enter number of picks per each participant.\n")
			temp = []
			temp_total = 0
		else:
			temp_total += int(num_of_rum_entrants)
	return temp

# Putting picks in random order
def royal_rumble_selection (num_of_rum_entrants, num, entrants, picks): 
	royal_rumble_entrants = ["None"] * int(num_of_rum_entrants)
	temp_picks = picks
	temp_total  = 0
	for i in range(1, int(num) + 1):
		temp_total += int(picks[i - 1])
	while temp_total > 0:
		random_int = random.randint(1, int(num))
		while int(temp_picks[random_int - 1]) <= 0:
			random_int = random.randint(1, int(num))
		temp_picks[random_int - 1] = int(temp_picks[random_int - 1]) - 1
		random_entrant = random.randint(1, int(num_of_rum_entrants))
		while True:
			if royal_rumble_entrants[random_entrant - 1] != "None":
				random_entrant = random.randint(1, int(num_of_rum_entrants))
			else:
				break
		royal_rumble_entrants[random_entrant - 1] = entrants[random_int - 1]
		temp_total -= 1
	return royal_rumble_entrants


# Main Program
rumble_entrants = input("How many people are in this year's Royal Rumble: ")
num_of_participants = participants()
print()
names_of_participants = names_of_entrants(num_of_participants)
print()
picks_per_participants = picks_per_person(rumble_entrants, num_of_participants, names_of_participants)
print()
rumble_placement = royal_rumble_selection(rumble_entrants, num_of_participants, names_of_participants, picks_per_participants)

for k in range(1, len(rumble_placement) + 1):
	print(f"Entry number {k}: {rumble_placement[k - 1]}")