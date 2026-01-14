def main():
    # Ask the user for their name;  clean up whitespace and capitalize
    name = input("What is your first name?: ").strip().title()

    # Ask the user for their current job title;  clean up whitespace and capitalize
    job_title = input("What is your current job title?: ").strip().title()

    # Call the custom function, print_switch_message
    print_switch_message(name, job_title)

def print_switch_message(name, job):
    # Use an f-string to print a clean message with name and title
    print(f"Hello, {name}!  From {job} to AI Engineer - the switch has turned ON!")

# Start the actual program here
main()