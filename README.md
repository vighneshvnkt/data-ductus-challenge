# Data Ductus Challenge

## Question

```
PROMPT:
  	Given a string as input, your task is to write a program which parses the string and prints it out as a horizontal tree. </br>
  	If the string input is invalid, your program should print, "Invalid!" and exit. </br>
  		* Individual elements are delimited with a comma followed by space (e.g., ", ") </br>
  		* Individual groupings are designated with an open bracket [ and a close bracket ] </br>
  		* Your program should accomplish this task in the most efficient way possible. </br>
  		* Empty elements are valid. </br>

  	EXAMPLE 1 (Input): </br>
  		[1, 2, [A, B, C, [5^&, )()6, , 7], D, E], 3, 4] </br>

  	EXAMPLE 1 (Output): </br>
  	1 </br>
  	2 </br>
    	A </br>
    	B </br>
    	C </br>
      		5^& </br>
      		)()6 </br>

      		7 </br>
    	D </br>
    	E </br>
  	3 </br>
  	4 </br>

  	EXAMPLE 2 (Input): </br>
  		[1, 2, [A, B, C, [5, 6]] </br>

  	EXAMPLE 2 (Output): </br>
  		Invalid! </br>
```

## Assumptions

```
	Strings are split at ", " and there are no commas inside each element in the string array after splitting </br>
	If there is a comma, return Invalid.
```

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