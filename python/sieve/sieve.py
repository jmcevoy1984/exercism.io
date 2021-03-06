def sieve(n):
	num_range = range(2, n+1)
	numbers = dict(zip(num_range, num_range))

	for i in range(2, len(numbers)+1):
		if numbers[i]:
			for j in range(2, n+1):
				if (numbers[i] * j) <= n+1:
					numbers[i * j] = False
				else:
					break

	return [numbers[i] for i in range(2, len(numbers)+1) if numbers[i]]
