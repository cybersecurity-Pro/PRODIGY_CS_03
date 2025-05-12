
import re

# Password strength checking function
def check_strength(password):
    feedback = []
    strength = 0

    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("❌ At least 8 characters")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("❌ Add lowercase letter")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("❌ Add uppercase letter")

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        feedback.append("❌ Add a digit")

    if re.search(r"[!@#$%^&*(),.?":{}|<>]", password):
        strength += 1
    else:
        feedback.append("❌ Add special character")

    if strength == 5:
        return "✅ Strong Password", "green", []
    elif strength >= 3:
        return "⚠️ Medium Password", "orange", feedback
    else:
        return "❌ Weak Password", "red", feedback

# Function to evaluate password
def evaluate():
    password = input("Enter your password to check its strength: ")
    result, color, issues = check_strength(password)
    print(f"\nResult: {result}")
    
    if issues:
        print("Feedback:")
        for issue in issues:
            print(issue)
    else:
        print("All criteria met! The password is strong.")

# Running the checker
if __name__ == "__main__":
    evaluate()
