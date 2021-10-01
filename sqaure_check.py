#!/usr/bin/env python3

# Created by: Liam Fletcher
# Created on: Sep 2021
# This program asks the user to enter positive integer
# The program will find the square for all the positive numbers


def main():
    # this tells the user the answer of
    # all the sqaures of the positive numbers up to the integer

    # input
    number_count = input("Please enter a positive integer: ")

    # process & output
    try:
        integer_as_number = int(number_count)

        if integer_as_number < 0:
            print("The is not a positive integer!")

        for square_loop in range(integer_as_number + 1):
            answer = square_loop * square_loop
            print("{0}² = {1}".format(square_loop, answer))

    except Exception:
        print("This is not a positive integer!")

    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
