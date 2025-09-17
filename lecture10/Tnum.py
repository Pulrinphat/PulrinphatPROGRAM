import numpy as np

random_matrix = np.random.randint(1,11, size=(3, 3))
print("Random 3x3 matrix:\n", random_matrix)

matrix_sum = np.sum(random_matrix)
print(f"\nSum of all element: {matrix_sum}")

matrix_mean = np.mean(random_matrix)
print(f"\nSum of all matrix: {matrix_mean:2.2f}")

transposed_matrix = np.transpose(random_matrix)
print("\nTraansposed Matrix:\n", transposed_matrix)