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


a = np.array( [ [1,2,3,4], [5,6,7,8], [9,10,11,12] ] )

row_r1 = a[1, :] #Rank 1 view of the second row of a
row_r2 = a[1:2, :] #Rank 2 view of the second row of a
print(row_r1, row_r1.shape) #shape (4,)
print(row_r2, row_r2.shape)


col_r1 = a[:, 1] # prints "[ 2 6 10] (3,)"
col_r2 = a[:, 1:2] # prints "[[ 2]
				   # 		  [ 6]
				   # 		  [10]] (3, 1)
print(col_r1, col_r1.shape)
print(col_r2, col_r2.shape)


# Integer array indexing
# When you index numpy arrays using slicing, the resulting array view will always be a subarray of the original array. 
# In contrast, integer array indexing allows you to construct arbitrary arrays using the data from another array.
