# Data Ductus Challenge

## Requirements

[Python 3](https://www.python.org/downloads/)

## Building

Acquire the source code.

```
$ git clone https://github.com/vighneshvnkt/data-ductus-challenge.git
$ cd data-ductus-challenge
```

## Running

```
$ python ParanthesisTreePrinter.py
```

You will get a prompt to submit input string. Once you submit it, you will see the printed output and the program exits.

## Question

PROMPT:
  	Given a string as input, your task is to write a program which parses the string and prints it out as a horizontal tree. </br>
  	If the string input is invalid, your program should print, "Invalid!" and exit. </br>
  			- Individual elements are delimited with a comma followed by space (e.g., ", ") </br>
  			- Individual groupings are designated with an open bracket [ and a close bracket ] </br>
  			- Your program should accomplish this task in the most efficient way possible. </br>
  			- Empty elements are valid. </br>

  	EXAMPLE 1 (Input): 
  		[1, 2, [A, B, C, [5^&, )()6, , 7], D, E], 3, 4] 

  	EXAMPLE 1 (Output): 
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

  	EXAMPLE 2 (Input): 
  		[1, 2, [A, B, C, [5, 6]] 

  	EXAMPLE 2 (Output): 
  		Invalid! 


## Assumptions


	Strings are split at ", " and there are no commas inside each element in the string array after splitting </br>
	If there is a comma, return Invalid.


## Runtime complexity

	O(3N) ~ O(N) where N is the size of the input string
	First for loop is to check for equal parantheses
	Second for loop is to ensure there are no commas in each element of string array after splitting
	Third for loop is for printing the required output

## Space complexity

	O(S + I) ~ O(I) where S is the size of paranthesesStack and I is the size of array after splitting input string
	Additional space is required for selecting substrings from elements in string array
	eg: string = "Apple" and string[:3] returns a new string containing chars from index 0 to 2