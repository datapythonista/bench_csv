import numpy


def numpy_loadtxt(fname):
    return numpy.sum(
            numpy.sqrt(
                numpy.sum(numpy.loadtxt(fname, delimiter=",")[:, 1:] ** 2,
                          axis=1)
            ) < 1e16)


if __name__ == "__main__":
    print(numpy_loadtxt("data.csv"))
