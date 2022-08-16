# strings and text! pg52

types_of_people=10
x = f"there are {types_of_people} types of people."
# first half of the joke with defined formatting

binary="binary"
do_not="don't"
y=f"Those who know {binary} and those who {do_not}"
# second half of the joke with simple string embedded variables.

print(x) #ex 6.2 = uniting the two parts of joke.
print(y)

print(f"I said: {x}") # note that round braces are used for print formatting and its different for variables.
print(f"I also said: {y}")

hilarious=False

joke_evaluation="Isn't that joke funny?! {}" ##inserting an empty formattable variable in string value of variable.

print(joke_evaluation.format(hilarious)) ##we printed the formatted value of a variable. MUST NOTE.

w="This is the left side of..."
e="a string with right side."

print(w+e) # adding two variables.
