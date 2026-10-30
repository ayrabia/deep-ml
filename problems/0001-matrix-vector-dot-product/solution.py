def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1
	if len(a[0]) != len(b):
		return -1

	# (1 * 1) + (2 *2) = 5
	# (2 * 1) + (4 * 2) = 10
	#[5,10]
	result = []
	#traverse each row in matrix a
	for row in a:
		row_sum = 0

		for row_val, b_val in zip(row, b):
			row_sum += row_val * b_val
		result.append(row_sum)
	return result