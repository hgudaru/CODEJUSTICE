import math

def quadratic_solver(a, b, c):
    # Calculate the discriminant
    delta = b**2 - 4*a*c

    # Check if the roots are real
    if delta >= 0:
        # Calculate the roots
        root1 = (-b + math.sqrt(delta)) / (2*a)
        root2 = (-b - math.sqrt(delta)) / (2*a)
        return root1, root2
    else:
        return "Complex roots - No real solution"

# Hard-coded variables
a_hardcoded, b_hardcoded, c_hardcoded = 2, -3, 1
roots_hardcoded = quadratic_solver(a_hardcoded, b_hardcoded, c_hardcoded)
print(f"Hard-coded roots: {roots_hardcoded}")

# Keyboard input
a_keyboard = float(input("Enter coefficient a: "))
b_keyboard = float(input("Enter coefficient b: "))
c_keyboard = float(input("Enter coefficient c: "))
roots_keyboard = quadratic_solver(a_keyboard, b_keyboard, c_keyboard)
print(f"Keyboard input roots: {roots_keyboard}")

# Read from a file (coefficients.txt)
with open('coefficients.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        a_file, b_file, c_file = map(float, line.strip().split())
        roots_file = quadratic_solver(a_file, b_file, c_file)
        print(f"File input roots: {roots_file}")

# Multiple sets of inputs
coefficient_sets = [(2, -3, 1), (1, 0, -1), (-1, 5, -2)]

for set in coefficient_sets:
    a_set, b_set, c_set = set
    roots_set = quadratic_solver(a_set, b_set, c_set)
    print(f"Set input roots: {roots_set}")
