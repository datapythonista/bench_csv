import pandas


def pandas_pyarrow_arrow(fname):
    values = (
        pandas.read_csv(
            fname,
            engine="pyarrow",
            dtype_backend="pyarrow",
            header=None,
            index_col=0,
            dtype=float,
        )
        .pow(2)
        .sum(axis="columns")
        .pow(0.5)
    )
    return values[values < 1e16].count()


if __name__ == "__main__":
    print(pandas_pyarrow_arrow("data.csv"))
