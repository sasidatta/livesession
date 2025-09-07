"""demo.py - A generic Python demo script for GitHub/CI-CD presentations."""

from typing import List

def greet_user(name: str) -> str:
    """Return a greeting message for the given user."""
    return f"Hello, {name}! 👋 Welcome to the Python demo."

def calculate_sum(numbers: List[int]) -> int:
    """Return the sum of a list of numbers."""
    return sum(numbers)

def main():
    """Run demo examples: greeting, sum calculation, and dictionary iteration."""
    # Demo 1: Greeting
    user_name = "Dattu"
    print(greet_user(user_name))

    # Demo 2: Sum Calculation
    numbers = [10, 20, 30, 40]
    print(f"Numbers: {numbers}")
    print(f"Sum: {calculate_sum(numbers)}")

    # Demo 3: Dictionary iteration
    capitals = {"India": "New Delhi", "USA": "Washington DC", "Japan": "Tokyo"}
    for country, capital in capitals.items():
        print(f"The capital of {country} is {capital}")

if __name__ == "__main__":
    main()
