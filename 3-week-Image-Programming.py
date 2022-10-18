#Example about arrays:
import numpy as np, random

# 1-2D array initializing with dot product:
arr1 = np.array([[1,2,3],[4,5,6]]) # 2*3
arr2 = np.array([[1,2],[3,4],[5,6]]) #3*2
result = np.dot(arr1,arr2) 
print(result) 


# 2- np.zeros and np.ones example:
arrZeros = np.zeros ((2,3))
arrOnes = np.ones((2,3))
addition = arrZeros + arrOnes
# or np.add(arrZeros, arrOnes) 
print(addition)


# 3- Numpy.eye() example, array with ones on the diagonal and zeros elsewhere.:
npEye = np.eye(3, dtype=int)
print(npEye)


# 4- Numpy.random.randn() example, creates array with 3 random numbers (floats) between 0 and 1:
arrRand = np.random.randn(3)
print(arrRand)


# 5- Numpy.random.rand() example, 2d array with 2 rows containing 3 random floats:
randomArr = np.random.rand(2, 3)
print(randomArr)



# 6- Numpy.matrix example, can take strings or numbers:
string:
strArr = np.matrix('6 7; 8 9')
print("numpy matrix with string input : \n", strArr, "\n\n")
  
# numbers input
numArr = np.matrix([[1, 10], [20, 30]])
print("\n numpy matrix with numbers input : \n", numArr)



# 7- if condition and while: 
while True:
    userInput = int(input('Choose operation: 1-Enter a string to reverse (1), 2-Hello Mssage (2), 3-Exit (3): '))
    if userInput == 3:
        break
    elif userInput == 1:
        str = input('String: ')
        print(str[::-1])
    elif userInput == 2:
        print('Hey, Sunshine! How are you? Your rays have already brightened my day!')


# 8- For loops:
doctors = ('Ahmet', 'Selim', 'Cevat')
for doc in doctors:
    print('Dr.' + doc)


# 9-Functions, sum of all numbers as arguments:
def sumArgs(*args):
  sum = 0
  for a in args:
    sum += a
  return sum

sum = sumArgs(1,1,1,1)
print(f"1-Argument sum = {sum}")

sum = sumArgs(5,10,15,20,50,100)
print(f"2-Argument sum = {sum}")

# 10-Taken numbers of elements and adding it and finding the average:
num = int(input("How many numbers are going to be entered? "))
numbers = []
for i in range(0,num):
    element = int(input("Enter the number: "))
    numbers.append(element)
average = sum(numbers)/num
print("The average of the entered numbers: ", round(average,2))
