import polars


def polars_lazy(fname):
    return (polars.scan_csv(fname)
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
