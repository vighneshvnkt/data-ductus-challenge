def printTree(tree,count):
	for elem in tree:
		print(elem)
	#	if(elem  is '[' or elem is ']'):
	#		pass
		if(elem is list):
			printTree(elem.split(", "),"    ")
		else:
			print(count,elem)

def paranthesesChecker(tree):
	paranthesesStack = []
	for elem in tree:
		#print(elem)
		if(elem == "["):
			paranthesesStack.append(elem)
		elif(elem == "]"):
			paranthesesStack.pop()
	if(len(paranthesesStack) == 0):
		return True
	else:
		return False


string_input = input("Please enter input string inside and along with []\n")
if(string_input[0] is not '[' or string_input[len(string_input)-1] is not ']'):
	print("Invalid")
	exit()
string_input = string_input[1:len(string_input)-1]
#print(string_input)
if(paranthesesChecker(string_input) is False):
	print("Invalid")
	exit()
try:
	stringDict = {}
	#for elem in string_input.split(", "):

	#stacks = string_input.split(", ")
	#print(stacks)
	#printTree(stacks,"")
except:
	print("Invalid!")

