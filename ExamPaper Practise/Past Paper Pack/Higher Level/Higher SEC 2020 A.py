
# Prompt the user to enter a password and store the ... 
# value entered in the variable password
password = input("Enter a password: ")
print("Password:",password)

# A variable to store all the lowercase letters in the alphabet
LOWER_CASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPER_CASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "1234567890"

# The variables lowercase and uppercase indicate the presence or ...
# absence of lowercase and uppercase characters in the password
lowercase = False # True if password contains a lowercase letter 
uppercase = False # True if password contains an uppercase letter
number = False # True if password contains an integer

# Loop through each character in the password and ...
# check the password for specific characters 
for character in password: 
    if character in LOWER_CASE_LETTERS: 
        lowercase = True 
    if character in UPPER_CASE_LETTERS:
        uppercase = True 
    if character in NUMBERS:
        number = True

# Calculate the score based on the rules

# initialise score
score = 0

# Rule 1
if len(password) > 7:
    score = score + 5
elif (len(password) >= 4) and (len(password) <= 7):
    score = score + 2
else:
    score -= 2

# Rule 2
if lowercase:
    score = score + 1

# Rule 3
if lowercase and uppercase:
    score = score + 5

# Rule 4
if uppercase:
    score += 2

# Rule 5
if number:
    score += 5

# Rule 6
password = list(password)
for character in password[0]:
    if character in NUMBERS:
        score += 1
for character in password[-1]:
    if character in NUMBERS:
        score += 1
for character in password[-1] and password[0]:
    if character in NUMBERS:
        score += 2

# Rule 7
if not uppercase + lowercase:
    score -= 10


# Display the score
print("Score:",score)