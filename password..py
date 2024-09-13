import re

def assess_password_strength(password):
    # Initialize the strength score and feedback
    score = 0
    feedback = []

    # Check length
    length = len(password)
    if length < 8:
        feedback.append("Password is too short; use at least 8 characters.")
    elif length <= 10:
        feedback.append("Password length is acceptable but could be longer.")
        score += 1
    else:
        feedback.append("Good password length.")
        score += 2

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        feedback.append("Contains uppercase letters.")
        score += 1
    else:
        feedback.append("Add some uppercase letters.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        feedback.append("Contains lowercase letters.")
        score += 1
    else:
        feedback.append("Add some lowercase letters.")

    # Check for numbers
    if re.search(r'[0-9]', password):
        feedback.append("Contains numbers.")
        score += 1
    else:
        feedback.append("Add some numbers.")

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        feedback.append("Contains special characters.")
        score += 1
    else:
        feedback.append("Add some special characters.")

    # Determine strength based on score
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    # Return the feedback and strength
    return {
        "strength": strength,
        "score": score,
        "feedback": feedback
    }

def main():
    # Get the password input from the user
    password = input("Enter a password to check its strength: ")
    # Assess the password strength
    result = assess_password_strength(password)
    # Display the results
    print(f"\nPassword Strength: {result['strength']}")
    print("Feedback:")
    for line in result['feedback']:
        print(f"- {line}")

# Run the main function
if __name__ == "__main__":
    main()
