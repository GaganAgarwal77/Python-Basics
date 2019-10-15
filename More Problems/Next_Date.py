def is_a_LeapYear(y): 
    if (y % 4) == 0 and (y % 100) != 0: 
        return True
    elif (y % 400) == 0: 
        return True
    else:
        return False
def next_date(d):
     day = d[0]
     month = d[1]
     year = d[2]
     if month in [1,3,5,7,8,10,12]:
       if day > 31:
            return False
       elif day == 31:
         day = 1
         if month == 12:
             month =1
             year += 1
         else:
             month += 1
       else:
            day  += 1
     elif month == 2 :
        if (is_a_LeapYear(year)):
             if day > 29:
                 return False
             elif day == 29:
                 day = 1
             else:
                 day+=1
        else:
             if day > 28:
                 return False
             elif day == 28:
                 day = 1
                 month += 1
             else:
                 day +=1

     elif month in [4,6,9,11]:
         if day > 30:
             return False
         elif day == 30:
             day = 1
             month += 1
         else:
             day  += 1
     else:
         return False   
     d1 =(day,month,year)
     return d1


