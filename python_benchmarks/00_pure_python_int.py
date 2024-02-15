import csv
import math


def pure_python_int(fname):
    with open(fname) as f:
        counter = 0

        reader = csv.reader(f)
        for row in reader:
            result = math.sqrt(sum([int(value) ** 2 for value in row[1:]]))
            if result < 10_000_000_000_000_000:
                counter += 1

        return counter


if __name__ == "__main__":
    print(pure_python_int("data.csv"))
