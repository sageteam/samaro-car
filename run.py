from itertools import permutations
from string import ascii_lowercase

a = list(permutations(ascii_lowercase))

from random import choice


print(choice(a))


