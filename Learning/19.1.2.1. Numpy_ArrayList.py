from numpy import *

#! Numpy is a hatrogiour data type which allow you to insert any datatype 
arr = array([1,2,3,4,5,6,7.6,"Roaunak   "])
for x in arr:
    print(x)
    
#* Types of array in numpy

ar1 = linspace(0,20,11) # Here 0 and 20 is included in the range 
print(ar1)

ar2 = arange(0,20,2) # Here 0 is inclued but the 20 is exclued in the range
print(ar2)

ar3 = logspace(10,20,2) # Here logspace can use the 10^X 
print(ar3)

zeros = zeros(3)
print(zeros)
ones = ones(3)
print(ones)
full = full(10,2) # First is denote the how mush and second is denote the who
print(full)