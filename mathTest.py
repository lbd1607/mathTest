#Laura Davis
#24 March 2016
#CGP145 Programming Challenge - Math Test
#This program creates a math test which asks the student
#to input their name and generates ten equations using 
#the random function. It will allow the student to answer
#the questions and will display whether the answers were
#right or wrong, accumulate the correct values, calculate
#the average number of correct answers, and finally display
#the average in decimal format.

#Import libraries
import random

#this is the main function
def main():
	print "Welcome to the math test program."
	#declare variables
	counter = 0
	right = 0
	numberOne = 0
	numberTwo = 0
	answer = 0
	studentName = "NO NAME"
	averageRight = 0.0
	
	#call to input names
	studentName = inputNames()
	
	#While loop to run program again
	while counter < 10:
		#call to get numbers
		numberOne, numberTwo = getNumbers()
		#call to get answer
		answer = getAnswer(numberOne, numberTwo)
		#call to check answer
		right = checkAnswer(numberOne, numberTwo, answer, right)
		counter = counter + 1
	#call to get results
	averageRight = results(right)
	#call to display info
	displayInfo(right, averageRight, studentName)
	
#module to input student name
def inputNames():
	studentName = raw_input("Enter student name: ")
	print studentName
	return studentName
	
#function to generate numbers with random function
def getNumbers():
	numberOne = random.randint(1, 500)
	numberTwo = random.randint(1, 500)
	return numberOne, numberTwo
	
#function to get the answers
def getAnswer(numberOne, numberTwo):
	print "What is the answer to the following equation? "
	print numberOne, "+", numberTwo
	answer = input("What is the sum? ")
	return answer
	
#function to check the answer
def checkAnswer(numberOne, numberTwo, answer, right):
	if answer == numberOne + numberTwo:
		print "Right"
		right = right + 1
	else:
		print "Wrong"
	print
	return right
	
#module to calculate results
def results(right):
	averageRight = right / 10.0
	return averageRight
	
#module to display info
def displayInfo(right, averageRight, studentName):
	print "Student Name: ", studentName
	print "The number right is ", right
	print "The average right is ", averageRight
	
main()
