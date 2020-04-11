command = ""
started = False
while True:
    command = input("Please input your command: ").lower()
    if command == "start":
        if started:
            print("The car has already started.")
        else:
            started = True
            print("Start the car")
    elif command == "stop":
        if not started:
            print("The car has already stopped.")
        else:
            started = False
            print("Stop the car")
    elif command == "help":
        print("""
        start- to start the car
        stop-to stop the car
        quit-to quit
        """)
    elif command == "quit":
        break
    else:
        print("sorry, I cannot understand")
