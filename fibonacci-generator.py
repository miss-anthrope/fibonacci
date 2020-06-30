#!/usr/bin/env python
# coding: utf-8
# THE MATH IN THIS PROGRAM RUNS MORE ACCURATELY.
'''
Capstone project - UDemy python bootcamp
This is a basic program designed to generate the Fibonacci sequence up to n.
'''

def fibnums(n):
	'''
	This should generate a Fibonacci sequence to the size of n.
	'''

	assert n > 0

	series = [1]

	while len(series) < n:
		if len(series) == 1:
			series.append(1)
		else:
			series.append(series[-1] + series[-2])

	for i in range(len(series)): #this converts the numbers into strings
		series[i] = str(series[i])

	return(', '.join(series)) #returns the full sequence separated by commas

def main(): #wrapper function
	print(fibnums(int(input("How many Fibonacci numbers do you want to see?"))))

if __name__ == '__main__':
	main()

