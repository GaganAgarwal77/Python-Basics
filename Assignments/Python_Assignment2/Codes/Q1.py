from Q1input import *

# Your code - begin
output = str()
last_character = ''
i = 0
j = 1
while (i < len(inp)):
    if (inp[i] != last_character):
        if (last_character != ''):
            output += str(j) + last_character
        j = 1
        last_character = inp[i]
    else:
        j += 1
    i += 1
else:
    output += str(j) + last_character
# Your code - end
print output
