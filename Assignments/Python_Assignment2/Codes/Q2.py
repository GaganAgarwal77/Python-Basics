from Q2input import *

# Your code - begin
opening_brackets = ['(', '[', '{']
closing_brackets = [')', ']', '}']
l = []
i = 0
a = len(inp)
if ( a%2 == 0) :
        while (i < a):
            if (inp[i] in opening_brackets) :
                l.append(inp[i])
            elif (inp[i] in closing_brackets) :
                n = len(l)
                x = closing_brackets.index(inp[i])
                if (l[n-1] == opening_brackets[x] and n > 0):
                    l.pop()
                else:
                    output = False
                    break
            i += 1
        if (len(l) == 0):
            output = True
else:
    output = False
# Your code - end
print output
