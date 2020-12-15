#!/usr/bin/env python3

# Created by: Wenda Zhao
# Created on: Dec 2020
# This program for continue statement


def main():
    # this function for continue statement

    loop_number = 0

    # input
    add_number = input("Enter how many number do you wangt to add: ")
    print("")

    # process & output
    try:
        add_number_int = int(add_number)
        if add_number_int > 0:
            for positive_integer in range(add_number_int):
                positive_integer = positive_integer - 1
                want_add_number = input("Enter number that you want to add: ")
                try:
                    want_add_number_int = int(want_add_number)
                    if want_add_number_int >= 0:
                        loop_number = loop_number + want_add_number_int
                        continue
                    else:
                        print("Please enter a non-negative integer")
                except Exception:
                    print("It not a integer")
            print("The answer is {0}".format(loop_number))
        else:
            print("It is not a positive number")
    except Exception:
        print("It not a integer")


if __name__ == "__main__":
    main()
