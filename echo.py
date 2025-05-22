# Initialization

print("Welcome to my program")
print("Type 'exit' to exit\n")

# Main loop
while True:
    user_input = input("Enter anything: ")
    if user_input.lower() == "exit":
        break
    elif not user_input:
        print("You didn't enter anything\n")
    else:
        print(f"You entered: {user_input}\n")

# Clean up
print("Exiting program...")