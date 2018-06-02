x = 'Johnny Cage'  # Single quotes
print(x)
x = "Johnny Cage"  # Double quotes
print(x)
x = "Johnny Cage's red tinted glasses."  # If a sentence uses single quotes surround in double quotes
print(x)
x = 'And then he said, "Put the alphabet in Math."'  # If a sentence uses double quotes place it inside single quotes
print(x)

# Uncomment below, erase the hash symbol, to see the error.
# x = "And then he said, "Put the alphabet in Math.""  # SyntaxError: invalid syntax
# print(x)

x = "And then he said, \"Put the alphabet in Math.\""  # Using a backslash before the double quotes to make them strings
print(x)
myFilePath = "home\Desktop\niceImages"  # \n in the word niceImages is read as a new line
print(x)
myFilePath = r"home\Desktop\niceImages"  # Type the letter r before the string to ignore all special symbols
print(myFilePath)

# Can add strings together and multiply with numbers.
x = "Johny"
y = "Cage"
print(x+y)
print(x*5)
