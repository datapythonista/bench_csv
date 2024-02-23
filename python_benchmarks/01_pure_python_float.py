import csv
import math


def pure_python_float(fname):
    with open(fname) as f:
        counter = 0

        reader = csv.reader(f)
        for row in reader:
            result = math.sqrt(sum([float(value) ** 2 for value in row[1:]]))
            if result < 1e16:
                counter += 1

        return counter


if __name__ == "__main__":
    print(pure_python_float("data.csv"))
