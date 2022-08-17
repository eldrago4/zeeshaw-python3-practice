from sys import argv

ayana,user_name=argv
prompt='$'

print(f"Hi, {user_name} I'm {ayana}") # first arguement will always be file name
print("I'd like to ask you few questions.. uwu")

print(f"Do you like me {user_name}? [do/don't]")
likes = input(prompt) # creating a variable that stores input.

print("Where do you live??")
lives=input(prompt) # we write x as message to be printed while fetching
# user input in input(x)

print("What computer do you use?")
computer = input(prompt)

print(f'''Got  you!\nSo you {likes} like me, live at {lives} and texting me from {computer}
huehuehueh''')
