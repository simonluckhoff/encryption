import random
import string

# Set the seed
random.seed(42)

# Get a list of lowercase letters
alphabet = list(string.ascii_lowercase)

# Shuffle the list
random.shuffle(alphabet)

# Print the shuffled alphabet
print("Shuffled alphabet:", ''.join(alphabet))
