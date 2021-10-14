#!/usr/bin/env python3

# Created by: Haokai Li
# Created on: Oct 2021
# This Program is about power


def main():
    # This function is about power
    loop_number = 0
    answer_number = 1

    # input
    first_string = input("Please enter a positive integer for the number: ")
    power_string = input("Please enter a positive integer for the power: ")
    print("")

    # process
    try:
        first_number = int(first_string)
        power_number = int(power_string)

        while loop_number < power_number:
            loop_number = loop_number + 1
            answer_number = answer_number * first_number

        # output
        print("Answer: {}".format(answer_number))

    except Exception:
        # output
        print("You didn't enter an integer.")

    print("\nDone.")


if __name__ == "__main__":
    main()
