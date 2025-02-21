import tkinter as tk
import re

def analyze_password_strength(password):
    score = 0
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    digit_criteria = bool(re.search(r'\d', password))
    symbol_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    common_patterns = ["123456", "password", "qwerty", "111111", "abc123"]

    if length_criteria:
        score += 1
    if uppercase_criteria:
        score += 1
    if lowercase_criteria:
        score += 1
    if digit_criteria:
        score += 1
    if symbol_criteria:
        score += 1
    if any(pattern in password for pattern in common_patterns):
        score -= 2

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

def analyze_password(event=None):
    password = entry.get()
    score, feedback = analyze_password_strength(password)
    
    result_message = f"Password Score: {score}\nPassword Strength: {feedback}\n"
    
    if score < 4:
        result_message += "Consider the following to improve your password:\n"
        if not re.search(r'[A-Z]', password):
            result_message += "- Add at least one uppercase letter.\n"
        if not re.search(r'[a-z]', password):
            result_message += "- Add at least one lowercase letter.\n"
        if not re.search(r'\d', password):
            result_message += "- Add at least one digit.\n"
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            result_message += "- Add at least one special character.\n"
        if len(password) < 8:
            result_message += "- Make your password at least 8 characters long.\n"
        if any(pattern in password for pattern in ["123456", "password", "qwerty", "111111", "abc123"]):
            result_message += "- Avoid common patterns like '123456', 'password', 'qwerty', etc.\n"

    # Update the result label with the analysis result
    result_label.config(text=result_message)

def toggle_password_visibility():
    if entry.cget('show') == '*':
        entry.config(show='')
        toggle_button.config(text='Hide Password')
    else:
        entry.config(show='*')
        toggle_button.config(text='Show Password')

# Create the main window
root = tk.Tk()
root.title("Password Analyzer")
root.geometry("600x400")
root.configure(bg='light sky blue')

# Create a label
label = tk.Label(root, text="Enter your password:", bg='light sky blue', font=("Arial", 12))
label.pack(pady=10)

# Create an entry widget for password input
entry = tk.Entry(root, show='*', width=30)
entry.pack(pady=10)

# Create a button to toggle password visibility
toggle_button = tk.Button(root, text='Show Password', command=toggle_password_visibility, bg='blue', fg='white')
toggle_button.pack(pady=5)

# Create a button to analyze the password
analyze_button = tk.Button(root, text="Analyze Password", command=analyze_password, bg='blue', fg='white')
analyze_button.pack(pady=20)

# Create a label to display the results
result_label = tk.Label(root, text="", bg='light sky blue', font=("Arial", 12))
result_label.pack(pady=10)

# Bind the ENTER key to analyze the password
root.bind('<Return>', analyze_password)

# Start the GUI event loop
root.mainloop()
