import csv
import random
import sys


def main():
    writer = csv.writer(sys.stdout)

    for i in range(1_000_000):
        values = [int(((random.random() - 0.5) * 2) * 2e16) for _ in range(8)]
        writer.writerow([i] + values)


if __name__ == "__main__":
    main()
