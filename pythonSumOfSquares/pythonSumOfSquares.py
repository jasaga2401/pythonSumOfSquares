
import time

# Inefficient method: Using a loop
def sum_of_squares_loop(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** 2
    return total

# Efficient method: Using a mathematical formula
def sum_of_squares_formula(n):
    return n * (n + 1) * (2 * n + 1) // 6

# Timing the inefficient method
start_time = time.time()
result_loop = sum_of_squares_loop(10**6)
end_time = time.time()
print(f"Inefficient method result: {result_loop}")
print(f"Time taken (loop): {end_time - start_time:.5f} seconds")

# Timing the efficient method
start_time = time.time()
result_formula = sum_of_squares_formula(10**6)
end_time = time.time()
print(f"Efficient method result: {result_formula}")
print(f"Time taken (formula): {end_time - start_time:.5f} seconds")
