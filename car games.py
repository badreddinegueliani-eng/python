command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("car is already started")
        else:
            started = True
            print("car started...")
    elif command == "stop":
        if not started:
            print("car is already stopped")
        else:
            started = True
        print("car stopped.")
    elif command == "hlep":
        print("""start, to start - stop, to stop - help""")
    elif command == "quit":
        break
    else:
        print("sorry, i don't undrestund")
         

              
    