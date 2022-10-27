import numpy as np


# Indexing:

# 1D arrays: 
a = np.array([1, 2, 3])
print('\n*******************************************************\n')
print('\n1-1D array:\n', a)
b=a[0] # 1 element by index
print('\nOne element by index: a[0]: ', b)
# using vector indexing: [value start index: number of values to print]
b = a[0:2] 
# Printing 2 values starting from first value  
print('\na[0:2]:', b)
b = a[1:] 
# Printing all values starting from second value 
print('\na[1:]:', b)

#2D arrays: 
print('*******************************************************\n')
arr = np.array([[1, 2, 3], [4,5,6]])
print('\n2-2D array:\n', arr)
b = arr[1][2]
# Printing value in second row and third column 
print('\narr[1][2]: ', b)
b = arr[1][-1]
# first row last element:
print('\narr[0][-1]: ', b)

# using vector indexing: [start_row:end_row, start_col:end_col]
b = arr[1:, 1:2]
# Printing values from first row and second column: 
print('\narr[1:, 1:2]:\n', b)

# A 1D array with 4 columns that has A in all columns but 0 in third:
B = np.full((1,4), 'A')
print('*******************************************************\n')
print('\nArray with \'A\' values: \n', B)
np.put(B, [2,2], ['0'])
print('\nChanging 3rd column to 0: \n',B)

# Sum using vector indexing:
C = np.array([[2, 2, 2], [1, 1, 1], [1, 1, 1]])
s = sum(C[:]) 
print('*******************************************************\n')
print('\n3-Vector:\n', C)
print('\nArray elemnts\' sum:\n', s)
# same as: 
# a = sum(C) 
# print(a)


# Transpose function: 
print('*******************************************************\n')
print('\nVector transpose: \n', np.transpose(C))

# reversing elements of a vector  
rev = np.array([1, 2, 3, 4, 5])
print('\nOriginal array: \n', rev)
print('\nReverse of the array: \n', rev[::-1])