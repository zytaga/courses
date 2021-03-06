"""
Exercise 1 (and Solution)
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
Extras:

    Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
    Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
"""

def get_user_input():
    user_input = input("How old are you?")
    user_input_2 = input("How many times do you want the message to be printed out?")
    return user_input, user_input_2

def main():

    user_input, user_input_2 = get_user_input()
    user_input = int(user_input)
    user_input_2 = int(user_input_2)
    year = 2020
    year_diff = 100 - user_input
    result = year + year_diff
    for x in range(0, user_input_2):
        print("You will be 100 years on in {}". format(result))

if __name__ == '__main__':
    main()