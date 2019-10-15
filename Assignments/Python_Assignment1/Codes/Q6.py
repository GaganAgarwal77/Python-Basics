
Abhiraj_paid = 990
Leon_paid = 140 + 150
Vigyan_paid =1100
Total = 990 + 290 + 1100
Split = Total/3
Abhiraj_due = round(Split - 990, 2)
Leon_due =round(Split - 290, 2)
Vigyan_due = round(Split - 1100, 2)
print(f"""
    Abhiraj's due amount is Rs{Abhiraj_due}
    Leon's due amount is Rs{Leon_due}
    Vigyan's due amount is Rs{Vigyan_due}    
    """)