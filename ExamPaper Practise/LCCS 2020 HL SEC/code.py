# Question 16(a)
# Examination Number:

# Prompt the user to enter a password and store the ...
# value entered in the variable password
password = input("Enter a password: ")

# A variable to store all the lowercase letters in the alphabet
LOWER_CASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPER_CASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "123456789"

# The variables lowercase and uppercase indicate the presence or ...
# absence of lowercase and uppercase characters in the password
lowercase = False # True if password contains a lowercase letter
uppercase = False # True if password contains an uppercase letter
digits = False

# Loop through each character in the password and ...
# check the password for specific characters
for character in password:
    if character in LOWER_CASE_LETTERS:
        lowercase = True
    if character in UPPER_CASE_LETTERS:
        uppercase = True
    if character in DIGITS:
        digits = True

# Calculate the score based on the rules

score = 0   # initialise score

# Rule 1
if len(password) < 4:
    score = score - 2
elif len(password) <= 7:
    score = score + 2
elif len(password) > 7:
    score = score + 5

# Rule 2
if lowercase:
    score = score + 1

# Rule 3
if lowercase and uppercase:
    score = score + 5

# Rule 4
if uppercase >= 1 :
    score = score + 2
    
# Rule 5
if digits:
    score = score + 5

# Rule 6
if password[0] in DIGITS:
    score = score + 1
if password[-1] in DIGITS:
    score = score + 1
if (password[0] in DIGITS) and (password[-1] in DIGITS):
    score = score + 2
    
# Rule 7
if (not uppercase) and (not lowercase):
    score = score - 10

# Display the score
print("Score:", score)