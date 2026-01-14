def main():
    score = int(input("On a scale of 1-10, how focused are you today? "))

    mood(score)

def mood(n):
    if n >= 8:
        print("You're doing great!  Push some code.")
    elif n >= 5:
        print("You're making steady progress.  Keep it up!")
    else:
        print("Take a short mental break and come back.  Don't give up!")

main()