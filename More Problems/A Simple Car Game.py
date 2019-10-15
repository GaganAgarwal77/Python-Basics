print("Welcome to the Car Game.")
print("Type 'help' to know more")
command = ""
started = False
while command != "quit":
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started.")
        else:
            started = True
            print("Car started.....Ready to Go!")
    elif command == "stop":
        if not started:
            print("Car is already stopped.")
        else:
            started = False
            print("Car stopped!")
    elif command == "help":
        print(""" Enter:
start - To start the car
stop - To stop the car
quit - To exit the game
             """)
    elif command == "quit":
        break
    else:
        print("Sorry,I don't understand that.")
