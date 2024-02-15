import polars


def polars_lazy(fname):
    dtypes = {f"column{i}": (polars.UInt32 if i == 0 else polars.Float32())
              for i in range(9)}
    return (polars.scan_csv(fname, dtypes=dtypes)
                  .select(
                      polars.sum_horizontal(polars.all()
                                                  .exclude("0")
                                                  .pow(2)
                      ).sqrt()
                       .alias("sum_sq"))
                  .filter(polars.col("sum_sq") < 1e16)
                  .count()
                  .collect()
    )


if __name__ == "__main__":
    print(polars_lazy("data.csv"))
