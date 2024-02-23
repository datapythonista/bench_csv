import pandas


def pandas_c(fname):
    values = (
        pandas.read_csv(fname, engine="c", header=None, index_col=0, dtype=float)
        .pow(2)
        .sum(axis="columns")
        .pow(0.5)
    )
    return values[values < 1e16].count()


if __name__ == "__main__":
    print(pandas_c("data.csv"))
