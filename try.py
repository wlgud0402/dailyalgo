import itertools

chars = ['(', ')', ')']

p = list(itertools.permutations(chars, len(chars)))
print(len(set(p)))

# (() , )() ,   ))(
