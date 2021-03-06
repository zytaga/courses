"""
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
Extras:

    If the number is a multiple of 4, print out a different message.
    Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""

def check_if_multiple_of_4(func):
    def checking(user_input, user_input_2):
        if user_input % 4 == 0:
            print("multiple of 4!")
        else:
            return func(user_input, user_input_2)
    return checking

@check_if_multiple_of_4
def check_if_even(user_input, user_input_2):
    if user_input % user_input_2 == 0:
        print("can be divided")
    else:
        print("cant be divided")

def main():
    user_input = input("input first number: ")
    user_input_2 = input("input modulo number: ")
    user_input = int(user_input)
    user_input_2 = int(user_input_2)
    check_if_even(user_input, user_input_2)

if __name__ == '__main__':
    main()