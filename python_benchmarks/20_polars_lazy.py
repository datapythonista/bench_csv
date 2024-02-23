import polars


def polars_lazy(fname):
    dtypes = {
        f"column{i}": (polars.UInt32 if i == 0 else polars.Float32()) for i in range(9)
    }
    return (
        polars.scan_csv(fname, dtypes=dtypes)
        .filter(
            polars.sum_horizontal(polars.all().exclude("column0").pow(2)).sqrt() < 1e16
        )
        .select(polars.len())
        .collect()
    )


if __name__ == "__main__":
    print(polars_lazy("data.csv"))
