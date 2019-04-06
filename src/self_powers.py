from multiprocessing import Pool


def self_powers(x):
	return x ** x


def main():
	series = (x for x in range(1, 1001))

	pool = Pool(5)
	series_sum = sum(pool.map_async(self_powers, series).get())

	pool.close()	
	pool.join()

	print(str(series_sum)[-10:])


if __name__ == "__main__":
	main()
