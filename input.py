print('How old are you?', end=' ')
age=input()

print('What is your height?', end= ' ')
height=input()

print('How much do you weigh?', end= ' ')
weight=input()

# WARNING! We put a end=' ' at the end of each print line. This tells print to not end
# the line with a newline character and go to the next line.

print(f"so your age is {age}, you are {height} tall and weigh {weight}...")


# ### Another way...

age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weigh? ")

print(f"So, you're {age} old, {height} tall and {weight} heavy.")
