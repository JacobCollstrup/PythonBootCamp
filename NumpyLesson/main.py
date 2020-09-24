import numpy as np

# Declaring numpy arrays:
x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(x)

y = np.array(x)

print(y)

# Methods for Numpy:

z = y * y

print(z)

w = np.dot(y, y)  # dot-/matrix multiplication of two matrices

print(w)

zero = np.zeros((3, 3))  # returns 3 x 3 matrix of zeroes

print(zero)

one = np.ones((3, 3))  # returns 3 x 3 matrix of ones

print(one)

ident = np.eye(3)  # returns 3 x 3 identity matrix

print(ident)

vector = np.arange(10)  # returns vector of 10 elements from 0 to 9

print(vector)

matrix = np.arange(50).reshape(5, 10)  # returns 5 x 10 matrix of numbers from 0 to 49 (50 elements)

print(matrix)

linspace = np.linspace(0, 10, 5)  # returns vector of 5 linear spaced values from 0 to 10

print(linspace)

print(y.max())  # returns max value in np-array

print(y.argmax())  # returns index of max value in np-array

new_matrix = matrix[1, 3] # returns the element at position 1,3 in the matrix. Row 1, column 3. Remember these are
                          # zero-indexed, so it's equivalent to 2nd row 4th column!
print(new_matrix)

newer_matrix = matrix[2:4, 4:6] # returns the submatrix from rows 2 to 3, column 4 to 5. Beware of zero-indexing and
print(newer_matrix)             # that slicing stops with element *before* the one indicated, upper limit is excluded.

new_vector = np.arange(1,20)
print(new_vector)
print(new_vector > 12)  # prints boolean vector with False where new_vector is smaller and equal to 12 and
                        # True where the vector is larger than 12.
print(new_vector[new_vector > 12])  # prints the values from new_vector that are larger than 12.

arr1 = np.array([1,1,2,3,4,5,6])
arr2 = np.array([0,2,1,3,4,8,9])

print(np.intersect1d(arr1,arr2))