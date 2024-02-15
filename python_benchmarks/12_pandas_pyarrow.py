import pandas


def pandas_pyarrow(fname):
    values = (pandas.read_csv(fname,
                              engine='pyarrow',
                              header=None,
                              index_col=0,
                              dtype=float)
                    .pow(2)
                    .sum(axis='columns')
                    .pow(.5)
    )
    return values[values < 1e16].count()


if __name__ == "__main__":
    print(pandas_pyarrow("data.csv"))
