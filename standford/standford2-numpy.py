import numpy as np

# Create the following rank 2 array with shape (3, 4)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
a = np.array( [ [1,2,3,4], [5,6,7,8], [9,10,11,12] ] )

# Use slicing to pull out the subarray consisting of the first 2 rows
# and columns 1 and 2; b is the following array of share (2, 2):
b = a[:2, 1:3]
print(a[0, 1])

# A slice of an array is a view into the same data, so modifying it
# will modify the original array.
b[0, 0] = 77
print(a[0, 1]) # print 77

row_r1 = a[1, :] #Rank 1 view of the second row of a
row_r2 = a[1:2, :] #Rank 2 view of the second row of a
#print(row_r1, row_r1.shape)