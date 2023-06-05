import numpy as np

n_dim = 3  # Number of dimensions for each array
n_arrays = 3  # Number of arrays to append

# Create an empty array to store the results
result_array = np.empty((0, n_dim))

# Generate and append each n-dimensional array
for i in range(n_arrays):
    new_array = np.random.rand(3)  # Replace this with your own n-dimensional array
    result_array = np.append(result_array, [new_array], axis=0)

print(result_array)
