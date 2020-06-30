#!/usr/bin/env python
# coding: utf-8

'''
Capstone project - UDemy python bootcamp
This program is meant to generate fibonacci numbers up to 500.
There are depth recursion problems with larger numbers.
'''

def fibonacci(n):

	if n == 1:
		return [1,0]
	else:
		num = fibonacci(n - 1)
		num = [num[0] + num[1], num[0]]
		return num

def validation():
	'''
	Requests user input for a positive integer under 500.
	'''

	while True:
		f = input("Which Fibonacci number to you want? (Up to 500.)")
		try:
			n = int(f)
			if n >= 500:
				print("Please enter a number under 500.")
			elif n > 0:
				return n
			else:
				print("Please enter a positive number.")
		except ValueError:
			print("Please enter a number between 0-500.")


def main():
	n = validation()
	print (fibonacci(n)[1])

if __name__ == "__main__":
	main()

