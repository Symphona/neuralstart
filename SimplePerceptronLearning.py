"""
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
trainingSet = [0,1,1,1]
binaryInputs = [[0,0],[0,1],[1,0],[1,1]]
output = [0,0,0,0]

def findOutput(i1, i2, w1, w2, b):
	global output
	i = 0
	for input1 in i1:
		for input2 in i2:
			if (((input1*w1)+(input2*w2)+b) >= 0):
				output[i] = 1
				i+=1
			else:
				output[i] = 0
				i+=1
	return output

def refreshOutput():
	while (len(output) < 0):
		output.pop()

def findErrors(output):
	global error, tooLow
	for i in range(4):
		if (int(output[i]) != int(trainingSet[i])):
			print "", int(output[i]), " vs ", int(trainingSet[i]), " is ", (int(output[i]) != int(trainingSet[i]))
			error = i
			print i
			if (output[i] < trainingSet[i]): tooLow = True
			else: tooLow = False
			return 0
	error = -1


def weightChange(error, tooLow):
	global b, w1, w2
	if (int(binaryInputs[error][0]) == 0 and int(binaryInputs[error][1]) == 0):
		if tooLow: b+=n
		else: b-=n
	elif (binaryInputs[error][0] == 0 and binaryInputs[error][1] == 1):
		if tooLow: w2+=1
		else: w2-=1
	elif (binaryInputs[error][0] == 1 and binaryInputs[error][1] == 0):
		if tooLow: w1+=1
		else: w1-=1
	elif (binaryInputs[error][0] == 1 and binaryInputs[error][0] == 1):
		#do something

def mainLoop():
	while(error != -1):
		print "*"
		findOutput(i1,i2,w1,w2,b)
		print output
		findErrors(output)
		if (error != -1): weightChange(error, tooLow)
		print "\nw1: ", w1, " w2: ", w2, " b: ", b, " error: ", error
		refreshOutput()
	print "done";

mainLoop()
