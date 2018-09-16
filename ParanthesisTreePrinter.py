'''
	A valid input is an input having equal number of opening and closing square brackets where closing brackets always follow the opening ones.
	This python file prints valid inputs as per the following input design :

  	- Individual elements are delimited with a comma followed by space (e.g. ", ")
  	- Individual groupings are designated with an open bracket [ and a close bracket ]
  	- Empty elements are valid (e.g. [], "").

	(Input): [1, 2, [A, B, C, [5^&, )()6, , 7], D, E], 3, 4]
	(Output):
	1
	2
		A
		B
		C
			5^&
			)()6

			7
		D
		E
	3
	4

	If the string input is invalid, print "Invalid!" and exit.
	(Input): [1, 2, [A, B, C, [5, 6]]
	(Output): Invalid!
'''

def paranthesesChecker(tree):
	'''
		Check if given tree has equal number of closing and opening square brackets using the paranthesesStack
		input : tree as string
		output : boolean value indicating paranthesesCheck
	'''
	paranthesesStack = []

	#try-except required to ensure you dont pop from an empty list, which means we get a closing bracket before an opening one
	try:	
		for elem in tree:
			if(elem == "["):
				paranthesesStack.append(elem)
			elif(elem == "]"):
				paranthesesStack.pop()
		if(len(paranthesesStack) == 0):
			return True
		else:
			return False
	except:
		return False

def tabs(count):
	'''
		Return String with n number of tabs
		input : number of tabs needed
		output : string with tabs = count
	'''
	emptySpaces = ''
	if(count <= 0):
		return emptySpaces
	while(count > 0):
		emptySpaces = emptySpaces + '    '
		count = count - 1
	return emptySpaces


#Enter input string
string_input = input("Please enter input string inside and along with []\n")

#Check if first and last characters of input are opening and closing brackets
if(string_input[0] is not '[' or string_input[len(string_input)-1] is not ']'):
	print("Invalid")
	exit()

#remove outermost square brackets
#string_input = string_input[1:len(string_input)-1]

#Validate for equal number of square parantheses	
if(paranthesesChecker(string_input) is False):
	print("Invalid")
	exit()

#commas not allowed in elements stripped by commas
for elem in string_input.split(", "):
	if(',' in elem):
		print("Invalid")
		exit()
try:
	bracketCount = 0 														#count of currently open square brackets
	for elem in string_input.split(", "): 									#split strings at commas
		elem = elem.strip()
		if('[' in elem and ']' in elem): 									#if empty list exists in elem
			if(elem.count('[') ==elem.count(']')): 							#equal square brackets in elem indicates complete empty sublist
				print(tabs(bracketCount))
			elif(elem.count('[') > elem.count(']')): 						#if more open brackets, increase bracket count
				bracketCount = bracketCount + 1
				print(tabs(bracketCount))
			else: 															#if more closed brackets, decrease bracket count
				print(tabs(bracketCount))
				bracketCount = bracketCount - 1
		elif('[' in elem): 													#if brackets open, add spaces
			bracketCount = bracketCount + 1
			print(tabs(bracketCount - 1) + elem[1:])
		elif(']' in elem): 													#if brackets close, remove spaces
			print(tabs(bracketCount - 1) + elem[:len(elem)-1])
			bracketCount = bracketCount - 1
		else:
			print(tabs(bracketCount - 1) + elem)
except:
	print("Invalid!")

