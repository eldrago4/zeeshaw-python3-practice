# parameters, unpacking and variables.
# we are at exercise 13!

# just another way to pass variables into strings...

from sys import argv # argv = arguement variable

script, first, second, third = argv

print("This is the script:", script)
print("This is the first variable:", first)
print("This is the second variable:", second)
print("This is the...THIRD variable", third)
