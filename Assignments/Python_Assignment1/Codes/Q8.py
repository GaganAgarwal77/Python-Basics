print("""Welcome to the Calculator.You can enter the following commands:
    add - to add two numbers a and b
    multiply - to multiply two numbers a and b
    average - to get the average of the two numbers a and b
    """)
command = input("Enter your command: ").lower()
if command == "add":
    a = int(input("Enter a : "))
    b = int(input("Enter b : "))
    print(f"The sum is {a+b}")
elif command == "multiply":
    a = int(input("Enter a : "))
    b = int(input("Enter b : "))
    print(f"The product is {a*b}")
elif command == "average":
    a = int(input("Enter a : "))
    b = int(input("Enter b : "))
    print(f"The average is {(a + b)/2}")
else:
    print("Invalid input")
