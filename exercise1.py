class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Instantiate the Cat object with 3 cats
cat1 = Cat('Tom', 12)
cat2 = Cat('Oggy', 19)
cat3 = Cat('Kitty', 8)

# Find the oldest cat
def findOldest(*args):
    return max(args)

# Output
print(f'The oldest cat is {findOldest(cat1.age, cat2.age, cat3.age)} years old.')