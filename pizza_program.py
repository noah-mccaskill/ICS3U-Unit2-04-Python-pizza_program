#!/usr/bin/env python3

# Created by Noah McCaskill
# Created in March 2022
# Program calculating the cost of a pizza

import constants


def main():
    # This function calculates the cost of a pizza

    # Input
    diameter = int(input("What diameter pizza would you like? (inch): "))

    # Process
    sub_total = constants.RENT + constants.LABOUR
    +(diameter * constants.COST_PER_INCH)
    total = total = (1 + constants.HST) * sub_total

    # Output
    print("The total cost is: ${:,.2f}".format(total))


if __name__ == "__main__":
    main()
