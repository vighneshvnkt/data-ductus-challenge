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
	emptySpaces = ''
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
try:
	bracketCount = 0
	for elem in string_input.split(", "):
		if(elem.strip() == '[]' or elem.strip() == ''):
			print(tabs(bracketCount))
		elif('[' in elem):
			bracketCount = bracketCount + 1
			print(tabs(bracketCount - 1) + elem[1:])
		elif(']' in elem):
			print(tabs(bracketCount - 1) + elem[:len(elem)-1])
			bracketCount = bracketCount - 1
		else:
			print(tabs(bracketCount) + elem)
except:
	print("Invalid!")

