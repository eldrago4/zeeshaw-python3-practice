# ex8

# ### print(...)
# ##### formatter.format(...)

formatter="{} {} {} {}"

print(formatter.format(1,2,3,4))
# printing integers

print(formatter.format("one","two","three","four"))
# printing embedded strings

print(formatter .format(True,False,False,True))
# printing booleans

# Why do I have to put quotes around ”one” but not around True or False?
# Python recognizes True and
# False as keywords representing the concept of true and false. If you put quotes around them
# then they are turned into strings and won’t work. You’ll learn more about how these work in
# Exercise 27.

print(formatter. format(formatter, formatter, formatter,formatter))
# printing embedded variables themselves.
# note that it will be four times the value of variable.

print(formatter
.format("quick brown","fox","jumped over"
,"the wall."))
# longer strings...
