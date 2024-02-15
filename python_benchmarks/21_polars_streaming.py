import polars as pl


def polars_streaming(fname):
    dtypes = {f"column{i}": (pl.UInt32 if i == 0 else pl.Float32())
              for i in range(9)}
    return (pl.scan_csv(fname, dtypes=dtypes)
            .filter(pl.sum_horizontal(pl.all()
                                      .exclude("column0")
                                      .pow(2)
                                      ).sqrt() < 1e16)
            .select(pl.len())
            .collect(streaming=True)
            )


if __name__ == "__main__":
    print(polars_streaming("data.csv"))
