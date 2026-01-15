# Gatekeeper password with loops
secret_code = "python123"

while True:
    response = input("Please enter your password: ")
    if response == secret_code:
        print("Access granted!")
        break
    elif response == "exit":
        print("Shutting down...")
        break
    else:
        print("Access denied")