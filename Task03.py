
import re

def check_password_strength(password):
    # Minimum length
    if len(password) < 8:
        return "Password is too short, it must be at least 8 characters long."

    # Check for uppercase, lowercase, numbers, and special characters
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = re.search("[!@#$%^&*()_+{}\[\]:;\"'\\<,>.?/|`~]", password)

    # Assess strength
    if not has_upper:
        return "Password should contain at least one uppercase letter."
    elif not has_lower:
        return "Password should contain at least one lowercase letter."
    elif not has_digit:
        return "Password should contain at least one number."
    elif not has_special:
        return "Password should contain at least one special character."
    else:
        return "Password strength: Strong!"

# Test the function
password = input("Enter your password: ")
print(check_password_strength(password))
