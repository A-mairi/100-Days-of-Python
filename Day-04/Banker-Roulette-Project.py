# Banker's Roulette
import random

# example names
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# Option 1
print(random.choice(friends))

# Option 2
Banker_Roulette = random.randint(0, 4)
print(friends[Banker_Roulette])
