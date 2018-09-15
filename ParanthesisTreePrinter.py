#Check working of stacks
string_input = input("Please enter input string inside and along with []")
try:
	stacks = list(string_input)
	stacks.append(4)
	print(stacks.pop())
except:
	print("Invalid!")