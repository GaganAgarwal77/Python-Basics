from Q6input import *

# Your code - begin
min = l[0]
l1 = []
j = 0
while (j < len(l)):
    for i in l :
        if (i < min) :
            min = i
    l1.append(min)
    l.remove(min)
    if (len(l) != 0):
        min = l[0]
l = l1
if ((len(l)+1) % 2 == 0):
    median = float(l[int((len(l)+1)/2)-1])
else:
    median = float((l[int((len(l)/2)) - 1] + l[int((len(l)+3)/2) - 1 ])/2)
output = median
# Your code - end
print output
