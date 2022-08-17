from sys import argv

ayana,user_name=argv
prompt='$'

print(f"Hi, {user_name} I'm {ayana}")
print("I'd like to ask you few questions.. uwu")

print(f"Do you like me {user_name}? [do/don't]")
likes = input(prompt)

print("Where do you live??")
lives=input(prompt)

print("What computer do you use?")
computer = input(prompt)

print(f'''Got  you!\nSo you {likes} like me, live at {lives} and texting me from {computer}
huehuehueh''')
