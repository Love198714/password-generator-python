import argparse
import secrets
import random
import string
from argparse import ArgumentParser
# --- Lines 1 to 5 are your imports ---

def check_strength(pw):
    length = len(pw)
    # Checks if any character matches these types
    has_upper = any(char.isupper() for char in pw)
    has_lower = any(char.islower() for char in pw)
    has_digit = any(char.isdigit() for char in pw)
    has_spec = any(char in string.punctuation for char in pw)
    
    # Summing the Booleans (True=1, False=0)
    score = sum([has_upper, has_lower, has_digit, has_spec])
    
    if length >= 12 and score >= 3:
        return "\033[92m⭐⭐⭐⭐ (Elite)\033[0m"
    elif length >= 8 and score >= 2:
        return "\033[93m⭐⭐⭐ (Strong)\033[0m"
    else:
        return "\033[91m⭐ (Weak/Basic)\033[0m"

# --- Your 'parser = ArgumentParser' code follows below ---
# Setting up the Argument Parser
parser = ArgumentParser(
    prog='Password Generator.',
    description='Generate any number of passwords with this tool.'
)

# Adding character count arguments
parser.add_argument("-n", "--numbers", default=0, help="Number of digits", type=int)
parser.add_argument("-l", "--lowercase", default=0, help="Number of lowercase chars", type=int)
parser.add_argument("-u", "--uppercase", default=0, help="Number of uppercase chars", type=int)
parser.add_argument("-s", "--special-chars", default=0, help="Number of special chars", type=int)

# Adding logic for total length or multiple passwords
parser.add_argument("-t", "--total-length", type=int, 
                    help="The total password length. If passed, it ignores specific counts.")
parser.add_argument("-a", "--amount", default=1, type=int, help="Number of passwords to generate")
parser.add_argument("-o", "--output-file", help="File to save the passwords")

# This final line actually processes the input
args = parser.parse_args()

# The list that will hold all generated passwords
passwords = []

for _ in range(args.amount):
    if args.total_length:
        # Scenario A: Generate a completely random password of fixed length
        alphabet = string.digits + string.ascii_letters + string.punctuation
        password = "".join(secrets.choice(alphabet) for _ in range(args.total_length))
        passwords.append(password)
    else:
        # Scenario B: Build a password based on specific counts (-n, -u, etc.)
        password_list = []
        
        for _ in range(args.numbers):
            password_list.append(secrets.choice(string.digits))
        for _ in range(args.uppercase):
            password_list.append(secrets.choice(string.ascii_uppercase))
        for _ in range(args.lowercase):
            password_list.append(secrets.choice(string.ascii_lowercase))
        for _ in range(args.special_chars):
            password_list.append(secrets.choice(string.punctuation))
            
        # Shuffle the list so the characters aren't in a predictable order
        random.shuffle(password_list)
        passwords.append("".join(password_list))

        # Save to file if the -o flag was used
if args.output_file:
    with open(args.output_file, 'w') as f:
        f.write('\n'.join(passwords))
    print(f"\n[+] Success! Passwords saved to: {args.output_file}")

# Always print results to the console for the user to see
print("\n--- Generated Passwords ---")
for p in passwords:
    # This runs every password through your grading function
    rating = check_strength(p)
    print(f"{p} | Strength: {rating}")