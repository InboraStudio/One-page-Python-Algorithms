import random
import cmath

def logic_gate():
    a = random.randint(1, 10)
    b = random.randint(-10, 10)
    c = random.randint(-10, 10)
    return a, b, c

def solve_logic(a, b, c):

    discriminant = b**2 - 4*a*c

    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    return root1, root2

def main():
    print("Welcome to The logic Gate Optimization core! ")

    a, b, c = logic_gate()
    print(f"Generated quadratic equation: {a}x^2 + ({b})x + ({c}) = 0")

    root1, root2 = solve_logic(a, b, c)

    print(f"The Optimal Core are : {root1} and {root2}")

if __name__ == "__main__":
    main()
