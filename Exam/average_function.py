# average_function.py
# For this exercise the pseudo-code is required (in this same file) 
# Write a function that calculates the average of the values of
# any vector of 10 numbers 
# Each single value of the vector should be read from the keyboard
# and added to a list.
# Print the input vector and its average 
# Define separate functions for the input and for calculating the average

'''
pseudo-code:
function vector: insert in input 10 values recursively
                 create list with values
                 save list output
function average:input a vector of 10 number
                 calculate sum of values
                 calculate length of vector
                 output sum/length 

>>> def vector_function():
...     L=[]
...     for i in list(range(10)):
...         a=input("insert number: ")
...         L.insert(i,a)
...     return L




>>> def average_function(L):
...     sum=0
...     for i in list(range(10)):
...         b=L[i]
...         sum=sum+b
...     average=sum/len(L)
...     print("the vector is ",L)
...     print("the average is ", average)

