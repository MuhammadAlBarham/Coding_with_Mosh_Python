from tracemalloc import start


command = ""
started = False

while True:
    command = input("> ").lower()

    if command == "start":
        if started == True:
            print("The car is already started!")
        else:
            print("The car is started!")
            started = True

    elif command == "stop":
        if not started:
            print("The car is already stopped!")
        else:
            started = False
            print("The car is stopped!")

    elif command == "quit":
        break
    elif command == "help":
        print("""
start - to start the car 
stop - to stop the car
quit - to quit
        """)
