import datafusion
import pyarrow

QUERY = """
    SELECT COUNT(*)
    FROM data
    WHERE SQRT(
        POWER(column_2, 2)
        + POWER(column_3, 2)
        + POWER(column_4, 2)
        + POWER(column_5, 2)
        + POWER(column_6, 2)
        + POWER(column_7, 2)
        + POWER(column_8, 2)
        + POWER(column_9, 2)
    ) < 1e16
"""

def datafusion_sql(fname):
    schema = pyarrow.schema([
        ("column_1", pyarrow.uint32()),
        *((f"column_{i}", pyarrow.float32()) for i in range(2, 10))
    ])
    context = datafusion.SessionContext()
    context.register_csv("data",
                         fname,
                         has_header=False,
                         schema=schema)

    return context.sql(QUERY).collect()


if __name__ == "__main__":
    print(datafusion_sql("data.csv"))
