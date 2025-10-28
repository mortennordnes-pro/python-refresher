# Save as: functions_practice.py

def greet(name):
    return f"Hello, {name}!"

def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count

def is_even(number):
    return number % 2 == 0

# Test your functions

print(greet("Alice"))

grades = [85, 90, 78, 92, 88]
print(f"Average grade: {calculate_average(grades)}")

test_number = 9
if is_even(test_number):
    print(f"{test_number} is even")
else:
    print(f"{test_number} is odd")