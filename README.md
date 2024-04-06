# **Password Strength Analyzer**

The Password Strength Analyzer is a Python program designed to evaluate the strength of passwords entered by users and provide suggestions for enhancing their security. It also offers the option to generate strong passwords automatically.

## **Features:**
1. **Password Strength Analysis:** The program analyzes the strength of a password based on various criteria, including length, presence of uppercase and lowercase letters, digits, and special characters.
2. **Password Suggestions:** If a password is deemed weak, the program offers suggestions to improve its strength, such as adding more characters or including different character types.
3. **Password Complexity Meter:** It provides a complexity meter rating, indicating how many of the password criteria are met out of a total of four.
4. **Password Generation:** Users have the option to generate strong passwords of a specified length automatically.

## **Components:**
- `analyze_password(password)`: Function to analyze the strength of a password.
- `suggest_password(password)`: Function to suggest improvements for weak passwords.
- `generate_password(length)`: Function to generate strong passwords of a specified length.
- `complexity_meter(password)`: Function to measure the complexity of a password.
- `main()`: The main function orchestrating the user interaction and calling other functions accordingly.

## **How to Use:**
1. Run the program.
2. Enter a password to be analyzed.
3. Receive feedback on the strength of the password, suggestions for improvement (if applicable), and its complexity meter.
4. Optionally, generate a strong password automatically.
5. Choose whether to check another password or exit the program.

## **Example:**
```
Password Strength Analyzer

Enter a password: mySecurePassword123@
Password strength: Strong
Password complexity meter: 4 / 4

Do you want to generate a strong password? (yes/no): no

Do you want to check another password? (yes/no): no
```

## **Requirements:**
- Python 3.x
- `re` module
- `random` module
- `string` module

## **Usage:**
```python
python main.py
```

## **Note:** Ensure that you have Python installed on your system and meet the requirements mentioned above before running the program.

## **Contributors:**
- https://github.com/Janani-m17

