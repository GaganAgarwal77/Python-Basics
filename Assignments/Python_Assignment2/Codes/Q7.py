from Q7input import *

# Your code - begin
l1.extend(l2)
l3=[]
j=0
min = l1[0]
while (j < len(l1)) :
    for i in l1 :
        if (i < min) :
            min = i
    l3.append(min)
    l1.remove(min)
    if (len(l1) != 0):
        min = l1[0]
l1 = l3
print(l3)
for num in l1:
    if (l1.count(num) > 1):
        l1.remove(num)
output = l1
# Your code - end
print output
