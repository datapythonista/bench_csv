# Python benchmarks to process a csv file

To run the benchmarks install [Pixi](https://prefix.dev/), clone this repository
and from inside the repository directory run:

```sh
gzip -d data.csv.gz
pixi install
pixi run bench
```

The results in my machine:

| Description                                           | File / Function      | Time (seconds)        |
|-------------------------------------------------------|----------------------|-----------------------|
| Pure Python looping with csv module using int types   | pure_python_int      | 3.4547557830810547    |
| Pure Python looping with csv module using float types | pure_python_float    | 3.8738009929656982    |
| pandas with C engine                                  | pandas_c             | 1.50089430809021      |
| pandas with Python engine                             | pandas_python        | 8.328583478927612     |
| pandas with PyArrow engine and NumPy dtypes           | pandas_pyarrow       | 0.31276631355285645   |
| pandas with PyArrow engine and PyArrow dtypes         | pandas_pyarrow_arrow | 0.29172492027282715   |
| Polars in lazy mode                                   | polars_lazy          | 0.1676042079925537    |
| Polars in streaming mode                              | polars_streaming     | 0.11536002159118652   |
| DuckDB with SQL API                                   | duckdb_sql           | 0.10763740539550781   |
| DataFusion with SQL API                               | datafusion_sql       | 0.0019359588623046875 |
| NumPy with loadtxt function                           | numpy_loadtxt        | 1.8354885578155518    |


The exact version of each library can be seen in the `pixi.toml` file. Note that DuckDB seems to package
for conda-forge later, so the benchmarks use DuckDB 0.9 while 0.10 seems to be available in other package
managers.
