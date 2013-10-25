"""
Author: Joel Potts
Language: Python2.7
Last Edit: 10/25/13
Summary:
This program is meant to emulate the learning process of an MCP neuron
based off of the Simple Perceptron Learning.
"""

"""
Initialize variables
w1,w2 - the weights used on the inputs
b - the bias
n - the neeta value (learning curve)
error - indicates where an error is found(location in array)
tooLow - indicates whether the error is due to too low or not
i1,i2 - input values
trainingSet - the desired output
binaryInputs - list of possible input patterns
output - output for current weights and bias
"""

w1 = 0
w2 = 0
b = 0
n = 1
error = 0
tooLow = False
i1 = [0,1]
i2 = [0,1]
trainingSet = [0,1,0,1]
binaryInputs = [[0,0],[0,1],[1,0],[1,1]]
output = [0,0,0,0]

#this function finds the output using current w1 w2 and b
def findOutput(i1, i2, w1, w2, b):
	global output
	i = 0
	for input1 in i1:
		for input2 in i2:
			if (((input1*w1)+(input2*w2)+b) >= 0):
				output[i] = 1	#if sum is greater than 0 (threshold) output is 1
				i+=1
			else:
				output[i] = 0
				i+=1 		#else it doesnt reach threshold and is 0
	return output
	
#refreshes output... pointless function will edit out...
def refreshOutput():
	while (len(output) < 0):
		output.pop()

#find the location of any error in the output and provides its index in the array and also determines if it is too low or not
def findErrors(output):
	global error, tooLow
	for i in range(4):
		if (int(output[i]) != int(trainingSet[i])):	#there is an error
			print "", int(output[i]), " vs ", int(trainingSet[i]), " is ", (int(output[i]) != int(trainingSet[i]))
			error = i 				#error is at index i
			print i
			if (output[i] < trainingSet[i]): tooLow = True	#output is lower than desired output
			else: tooLow = False				#output is higher than desired
			print "", output[i], " is less than ", trainingSet[i], ": ", tooLow
			return 0	#stops function so error is not set to -1
	error = -1 	#if no errors are found error is set to -1 as sentinel value
			
#changes weights or bias according to error
#note to self: can change if to if(i = 0,1,2,3) to determine pattern... more efficiant
def weightChange(error, tooLow):
	global b, w1, w2
	if (binaryInputs[error][0] == 0 and binaryInputs[error][1] == 0):		#pattern 00 has error
		if tooLow: b+=1
		else: b-=n
	elif (binaryInputs[error][0] == 0 and binaryInputs[error][1] == 1):		#pattern 01 has error
		if tooLow: w2+=n
		else: w2-=n
	elif (binaryInputs[error][0] == 1 and binaryInputs[error][1] == 0):		#pattern 10 has error
		if tooLow: w1+=n
		else: w1-=n
	elif (binaryInputs[error][0] == 1 and binaryInputs[error][0] == 1):		#pattern 11 has error
		if tooLow:
			if (w1 > 0): w1+=n
			elif (w2 > 0): w2+=n
			elif (b > 0): 
				b+=n
				w1-=n
				w2-=n
			else:
				b-=n
				w1+=n
				w2+=n
		else:
			if (w1 < 0): w1-=n
			elif (w2 < 0): w2-=n
			elif(b < 0):
				b-=n
				w1+=n
				w2+=n
			else:
				b+=n
				w1-=n
				w2-=n

#mainloop manages which functions to call
def mainLoop():
	while(error != -1):
		print "*"
		findOutput(i1,i2,w1,w2,b)
		print output
		findErrors(output)
		if (error != -1): weightChange(error, tooLow)
		print "\nw1: ", w1, " w2: ", w2, " b: ", b, " error: ", error
		refreshOutput()
	print "done\n"
	print "Output: ", output, ", w1: ", w1, ", w2: ", w2, ", b: ", b
	print "Training Set: ", trainingSet
	
mainLoop() #calls mainLoop and main program
