"""
Data Formation

To help with date formatting you should create a new helper class. This class must represent a Date (no time) that knows
how to print a formatted date. It should work like this:

from dates import Date
d = Date(11, 21, 2007)
d.formatted()

Prints:
21-11-2007

Create and implement this class inside a date.py file. Get to work!
"""
from date import Date


def main():
    date = Date(11, 21, 2007)
    date.formatted()


if __name__ == '__main__':
    main()
