"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print(x, y, z)

# Use the 'format' string method to print the same thing
formatString = "x is {}, and y is {}".format(x, y)
formatString2 = "x is {0}, and y is {1}".format(x, y)
formatString3 = "x is {xName}, and y is {yName}".format(xName = 10, yName = 20)
print(formatString)
print(formatString2)
print(formatString3)

# Finally, print the same thing using an f-string
print(f'Hello, {x}, {y}, {z}')