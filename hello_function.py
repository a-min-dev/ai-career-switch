def main():
    name = input("What's your name? ")
    hello(name)


# Created a hello() function with default parameter of the string, "world"
def hello(to="world"):
    print("hello,", to)

# Call main() function
main()

