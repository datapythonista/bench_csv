import importlib
import pathlib
import time


def main():
    this_dir = pathlib.Path(__file__).parent
    data_fname = (this_dir.parent / "data.csv").resolve()

    for benchmark in sorted(this_dir.glob("[0-9][0-9]_*.py")):
        module_name = benchmark.with_suffix("").name
        module = importlib.import_module(f"python_benchmarks.{module_name}")
        function_name = module_name[3:]
        benchmark_function = getattr(module, function_name)

        start = time.time()
        str(benchmark_function(data_fname))
        elapsed = int((time.time() - start) * 1000)
        print(f"{function_name},{elapsed}")


if __name__ == "__main__":
    main()
