import string

password = input("Enter a password: ")

length = len(password)

has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_number = any(c.isdigit() for c in password)
has_symbol = any(c in string.punctuation for c in password)

score = 0

if length >= 8:
    score += 1
if has_upper:
    score += 1
if has_lower:
    score += 1
if has_number:
    score += 1
if has_symbol:
    score += 1

if score <= 2:
    strength = "Weak"
elif score <= 4:
    strength = "Moderate"
else:
    strength = "Strong"

print("\nPassword Analysis")
print("-----------------------")
print("Length:", length)
print("Contains uppercase:", has_upper)
print("Contains lowercase:", has_lower)
print("Contains number:", has_number)
print("Contains symbol:", has_symbol)
print("Password strength:", strength)

print("\nSuggestions:")

if length < 8:
    print("- Make the password at least 8 characters long")
if not has_upper:
    print("- Add at least one uppercase letter")
if not has_lower:
    print("- Add at least one lowercase letter")
if not has_number:
    print("- Add at least one number")
if not has_symbol:
    print("- Add at least one symbol like ! @ # $")