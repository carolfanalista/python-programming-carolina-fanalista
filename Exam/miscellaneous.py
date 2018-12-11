# miscellaneous.py
# For the following exercises, pseudo-code is not required

# Exercise 1
# Create a list L of numbers from 21 to 39
# print the numbers of the list that are even
# print the numbers of the list that are multiples of 3
L=list(range(21,40))
for i in L:
...     if i%2==0:
...         print (i)

>>> for i in L:
...     if i%3==0:
...         print (i)




# Exercise 2
# Print the last two elements of L 
>>> len(L)
19
>>> print (L[18],L[17])


# Exercise 3
# What's wrong with the following piece of code? Fix it and 
# modify the code in order to have it work AND to have "<i> is in the list" 
# printed at least once

for i in range(10):
...     if i in L:
...         print("%d in the list"%i)
...     else:
...         print("%d not found"%i)
... 

 


# Exercise 4
# Read the first line from the sprot_prot.fasta file
# Split the line using 'OS=' as delimiter and print the second element
# of the resulting list 
open_file=open("sprot_prot.fasta")
>>> first_line=open_file.readline()
>>> first_line
>>> split_line=first_line.split('OS=')
>>> split_line[1]



# Exercise 5
# Split the second element of the list of Exercise 4 using blanks
# as separators, concatenate the first and the second elements and print
# the resulting string
a=split_line[1]
b=a.split("blanks")
print(str(split_line[0])+str(b))




# Exercise 6
# reverse the string 'asor rosa'
c="asor rosa"
>>> c[::-1]
'asor rosa'



# Exercise 7
# Sort the following list: L = [1, 7, 3, 9]
L.sort()

# Exercise 8
# Create a new sorted list from L = [1, 7, 3, 9] without modifying L
a=L.sort

# Exercise 9
# Write to a file the following 2 x 2 table:
# 2 4
# 3 6
 s=("2\t4\n3\t6")
>>> print(s)

