import duckdb

QUERY = """
    SELECT COUNT(*)
    FROM '{}'
    WHERE SQRT(
        column1 ** 2
        + column2 ** 2
        + column3 ** 2
        + column4 ** 2
        + column5 ** 2
        + column6 ** 2
        + column7 ** 2
        + column8 ** 2
    ) < 1e16
"""

def duckdb_sql(fname):
    return duckdb.sql(QUERY.format(fname))


if __name__ == "__main__":
    print(duckdb_sql("data.csv"))
