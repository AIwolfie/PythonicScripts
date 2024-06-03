# Here is a comprehensive example that demonstrates several functions from the random module:

import random

# Generate a random float between 0.0 and 1.0
random_float = random.random()
print(f"Random float between 0.0 and 1.0: {random_float}")

# Generate a random integer between 1 and 10
random_int = random.randint(1, 10)
print(f"Random integer between 1 and 10: {random_int}")

# Select a random element from a list
my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
random_choice = random.choice(my_list)
print(f"Random choice from list: {random_choice}")

# Select 3 random elements from the list with replacement
random_choices = random.choices(my_list, k=3)
print(f"Random choices from list: {random_choices}")

# Select 3 unique random elements from the list
random_sample = random.sample(my_list, k=3)
print(f"Random sample from list: {random_sample}")

# Shuffle the list in place
random.shuffle(my_list)
print(f"Shuffled list: {my_list}")

# Generate a random float between 1.5 and 10.5
random_uniform = random.uniform(1.5, 10.5)
print(f"Random float between 1.5 and 10.5: {random_uniform}")

# Generate a random number based on Gaussian distribution
random_gauss = random.gauss(0, 1)
print(f"Random Gaussian number with mean 0 and standard deviation 1: {random_gauss}")


# Explanation:

# Random Float: Generates a random floating-point number between 0.0 and 1.0 using random.random().
# Random Integer: Generates a random integer between 1 and 10 using random.randint(1, 10).
# Random Choice: Selects a random element from my_list using random.choice(my_list).
# Random Choices: Selects 3 random elements from my_list (with replacement) using random.choices(my_list, k=3).
# Random Sample: Selects 3 unique random elements from my_list using random.sample(my_list, k=3).
# Shuffle List: Shuffles my_list in place using random.shuffle(my_list).
# Random Float Range: Generates a random float between 1.5 and 10.5 using random.uniform(1.5, 10.5).
# Random Gaussian: Generates a random number based on Gaussian distribution with mean 0 and standard deviation 1 using random.gauss(0, 1).