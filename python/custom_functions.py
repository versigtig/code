# --- Custom Functions ---
# === Johnathan Fisher ===
# This file contains custom functions and a
# loop to test them.

# --- FUNCTIONS ---

def substring_exists(string, substring):
	'''When passed a string and substring, 
	returns True if substring exists in string'''
	i = 0 
	j = 0
	
	while i != len(string):
		if string[i] == substring[j]:
			i += 1
			j += 1
		else:
			i += 1
			j = 0
	
		if j == len(substring):
			return True
	
	return False
	
def substring_location(string, substring):
	'''When passed a string and substring, returns 
	starting index location of substring if it exists 
	within string'''
	i = 0
	j = 0
	
	while i != len(string):
		if string[i] == substring[j]:
			i += 1
			j += 1
		else:
			i += 1
			j = 0
		if j == len(substring):
			return i - j
	
	return -1
	

# --- MAIN TEST LOOP ---

done = False

while not done:
	
	print("")
	print("Which function would you like to test? ")
	print("0. QUIT PROGRAM")
	print("1. substring_exists")
	print("2. substring_location")
	user_input = input("Enter the number of the function to try, or 0 to quit: ")
	print("")
	
	if user_input == "0":
		done = True
	elif user_input == "1":
		user_string = input("Enter a string: ")
		user_substring = input("Enter a substring to find: ")
		
		if substring_exists(user_string,user_substring):
			print("\"", user_substring,"\" is contained within \"", user_string,"\".")
		else:
			print("\"", user_substring,"\" is NOT contained within \"", user_string,"\".")
		
	elif user_input == "2":
		user_string = input("Enter a string: ")
		user_substring = input("Enter a substring to find: ")
		
		substring_index = substring_location(user_string,user_substring)
		
		if substring_index != -1:
			print("\"", user_substring,"\" is at index ", substring_index, " of\"", user_string,"\".")
		else:
			print("\"", user_substring,"\" is NOT contained within \"", user_string,"\".")
	else:
		print("Please enter a function number, or 0 to quit.")
