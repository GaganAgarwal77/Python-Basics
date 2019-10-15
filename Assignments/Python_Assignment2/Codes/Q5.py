from Q5input import *

# Your code - begin
output = []
for num in l[n:len(l)]:
    output.append(num)
    l.remove(num)
output.extend(l)
# Your code - end
print output
