# Python String Slicing
# In addition to indexing, slicing is also supported. 
# While indexing is used to obtain individual characters, 
# slicing allows you to obtain substring: 

word = 'Python'

word[0:2]  # characters from position 0 (included) to 2 (excluded)
word[2:5]  # characters from position 2 (included) to 5 (excluded)

# Note how the start is always included, and the end always excluded. 
# This makes sure that s[:i] + s[i:] is always equal to s:

word[:2] + word[2:]
word[:4] + word[4:]

# If you need a different string, you should create a new one:

'J' + word[1:]
word[:2] + 'py'
