import itertools
import string

# Characters to include in the combinations
characters = string.ascii_letters + string.digits

# Password length
length = 8

# Generate all possible combinations and write to file
with open('passwords.txt', 'w') as file:
    combinations = itertools.product(characters, repeat=length)
    for combination in combinations:
        password = ''.join(combination)
        file.write(password + '\n')

print(f"Generated all passwords and saved to passwords.txt.")