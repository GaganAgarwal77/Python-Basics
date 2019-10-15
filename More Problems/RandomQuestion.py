#Q.A class is divided inton teams with m members each.Each member is assigned a unique code which maps him/her back to his/her team.Use a function
to return a list  which maps team number to list of codes of its members.

import random
def gen_codes(n,m):
  l = []
  for i in range(n):
    l += [[random.randint(1,1000000) fo j in range(m)]]
  print l
    
  
