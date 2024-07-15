import re

def analyze_password_strength(password):
    # Initialize the score
    score = 0
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    digit_criteria = bool(re.search(r'\d', password))
    symbol_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    common_patterns = ["123456", "password", "qwerty", "111111", "abc123"]

    # Check length
    if length_criteria:
        score += 1

    # Check for uppercase letters
    if uppercase_criteria:
        score += 1

    # Check for lowercase letters
    if lowercase_criteria:
        score += 1

    # Check for digits
    if digit_criteria:
        score += 1

    # Check for symbols
    if symbol_criteria:
        score += 1

    # Check for common patterns
    if any(pattern in password for pattern in common_patterns):
        score -= 2  # Deduct points for common patterns

    # Provide feedback based on the score
    feedback = ""
    if score <= 1:
        feedback = "Very Weak"
    elif score == 2:
        feedback = "Weak"
    elif score == 3:
        feedback = "Moderate"
    elif score == 4:
        feedback = "Strong"
    elif score == 5:
        feedback = "Very Strong"

    return score, feedback

if __name__ == "__main__":
    password = input("Enter your password to analyze: ")
    score, feedback = analyze_password_strength(password)
    print(f"Password Score: {score}")
    print(f"Password Strength: {feedback}")

    if score < 4:
        print("Consider the following to improve your password:")
        if not re.search(r'[A-Z]', password):
            print("- Add at least one uppercase letter.")
        if not re.search(r'[a-z]', password):
            print("- Add at least one lowercase letter.")
        if not re.search(r'\d', password):
            print("- Add at least one digit.")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            print("- Add at least one special character.")
        if len(password) < 8:
            print("- Make your password at least 8 characters long.")
        if any(pattern in password for pattern in ["123456", "password", "qwerty", "111111", "abc123"]):
            print("- Avoid common patterns like '123456', 'password', 'qwerty', etc.")
