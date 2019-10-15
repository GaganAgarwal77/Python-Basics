from Q3input import *

# Your code - begin
no_of_rows_m1 = len(m1)
no_of_columns_m1 = len(m1[0])
m3 = []
m4 = []
for i in range(no_of_columns_m1):
  for j in range(no_of_rows_m1):
    m3.append(m1[j][i])
  m4.append(m3)
  m3 = []
output = m4

# Your code - end
print output
