import re
import random
import string


def analyze_password(password):
    length_criteria = len(password) >= 8
    upper_criteria = any(char.isupper() for char in password)
    lower_criteria = any(char.islower() for char in password)
    digit_criteria = any(char.isdigit() for char in password)
    special_criteria = any(char in string.punctuation for char in password)

    strength = "Weak"
    if length_criteria and upper_criteria and lower_criteria and digit_criteria and special_criteria:
        strength = "Strong"
    elif length_criteria and upper_criteria and lower_criteria and digit_criteria:
        strength = "Moderate"

    return strength


def suggest_password(password):
    suggestions = []
    if len(password) < 8:
        suggestions.append("Add more characters (at least 8 characters).")
    if not any(char.isupper() for char in password):
        suggestions.append("Include at least one uppercase letter.")
    if not any(char.islower() for char in password):
        suggestions.append("Include at least one lowercase letter.")
    if not any(char.isdigit() for char in password):
        suggestions.append("Include at least one digit.")
    if not any(char in string.punctuation for char in password):
        suggestions.append("Include at least one special character.")

    return suggestions


def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))


def complexity_meter(password):
    complexity = 0
    if len(password) >= 8:
        complexity += 1
    if any(char.isupper() for char in password) and any(char.islower() for char in password):
        complexity += 1
    if any(char.isdigit() for char in password):
        complexity += 1
    if any(char in string.punctuation for char in password):
        complexity += 1
    return complexity


def main():
    while True:
        print("\nPassword Strength Analyzer")
        user_password = input("Enter a password: ")

        strength = analyze_password(user_password)
        suggestions = suggest_password(user_password)
        meter = complexity_meter(user_password)

        print("Password strength:", strength)
        if suggestions:
            print("Suggestions:")
            for suggestion in suggestions:
                print("-", suggestion)
        print("Password complexity meter:", meter, "/ 4")

        generate_option = input("\nDo you want to generate a strong password? (yes/no): ")
        if generate_option.lower() == "yes":
            new_password = generate_password()
            print("Generated password:", new_password)

        repeat = input("\nDo you want to check another password? (yes/no): ")
        if repeat.lower() != "yes":
            break


if __name__ == "__main__":
    main()
