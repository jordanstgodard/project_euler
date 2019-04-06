from multiprocessing import Pool


# O(N) - will convert to O(1) in future commit
def multiple_of_any(x, factors=[3, 5]):
    for f in factors:
        if x % f == 0:
            return x

    return 0


def main():
    series = (x for x in range(0, 1000))

    pool = Pool(5)
    series_sum = sum(pool.map_async(multiple_of_any, series).get())

    print(series_sum)


if __name__ == "__main__":
	main()
