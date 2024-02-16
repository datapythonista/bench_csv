import polars

QUERY = """
    SELECT COUNT(*)
    FROM data
    WHERE SQRT(
        POWER(column1, 2)
        + POWER(column2, 2)
        + POWER(column3, 2)
        + POWER(column4, 2)
        + POWER(column5, 2)
        + POWER(column6, 2)
        + POWER(column7, 2)
        + POWER(column8, 2)
    ) < 10000000000000000
"""

def polars_sql(fname):
    dtypes = {f"column{i}": (polars.UInt32 if i == 0 else polars.Float32())
              for i in range(9)}
    context = polars.SQLContext(data=polars.scan_csv(fname, dtypes=dtypes))
    return context.execute(QUERY, eager=True)


if __name__ == "__main__":
    print(polars_sql("data.csv"))
