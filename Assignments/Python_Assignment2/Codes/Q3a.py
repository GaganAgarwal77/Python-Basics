from Q3input import *

# Your code - begin
no_of_rows_m1 = len(m1)
no_of_rows_m2  = len(m2)
no_of_columns_m1 = len(m1[0])
no_of_columns_m2 = len(m2[0])
m3 = []
m4 = []
sum = 0

if (no_of_columns_m1 == no_of_rows_m2) :
  for i in range(no_of_rows_m1) :
    for j in range(no_of_columns_m2) :
      for k in range(no_of_columns_m1) :
        sum += (m1[i][k] * m2[k][j])
      m3.append(sum)
      sum = 0
    m4.append(m3)
    m3 = []
else:
  print("Matrices are not multiplicable")
output = m4

# Your code - end
print output
