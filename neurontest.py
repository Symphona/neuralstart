	
#This piece of code is designed to create the simple perceptron learning model for a basic MCP neuron
#initialise all variables used
w1 = 0
w2 = 0
b = 0
n = 1
error = 0
tooLow = False

#The two inputs need to be varied between 1 and 0 to give all possible patterns
i1 = [0,1]
i2 = [0,1]
trainingSet = [0,0,0,1]
binaryInputs = [[0,0],[0,1],[1,0],[1,1]]
output = [0,0,0,0]
     

#The findOutput function just solves the truth table for the given inputs
#This is called later to update the outputs after every weight balance
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
           
   # def refreshOutput():
   #	while (len(output) < 0):
   #		output.pop()
     

#findErrors compares the output discovered above to the ideal training set and returns the first error #it encounters. If no errors, sets error to -1 to end the learning cycle.
#If error is located, it will set the global error variable to the current value of i (to locate the #error again)
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
                           
                           
#This function adjusts the weights depending on which input pattern is displayed. The bias is only #adjusted when the input is [0,0]
#The weights are checked to see if they are too low, and increased; otherwise they are decreased.
def weightChange(error, tooLow):
	global b, w1, w2
	if (binaryInputs[error][0] == 0 and binaryInputs[error][1] == 1):
		if tooLow: w2+=n
		else: w2-=n
	elif (binaryInputs[error][0] == 1 and binaryInputs[error][1] == 0):
		if tooLow: w1+=n
		else: w1-=n
	elif (binaryInputs[error][0] == 0 and binaryInputs[error][1] == 0):
		if tooLow: b+=n
		else: b-=n
	elif (binaryInputs[error][0] == 1 and binaryInputs[error][1] == 1):
		if tooLow: b+=n
		else: b=n
           
#The mainloop generally holds all the output and looping of the functions above
def mainLoop():
	while(error != -1):
		print "*"
		findOutput(i1,i2,w1,w2,b)
		print output
		findErrors(output)
		if (error != -1): weightChange(error, tooLow)
		print "\nw1: ", w1, " w2: ", w2, " b: ", b, " error: ", error
		#refreshOutput()
	print "done\n", output;
           
mainLoop()


