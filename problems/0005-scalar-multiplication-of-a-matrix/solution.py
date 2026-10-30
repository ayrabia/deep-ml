def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	res = []

	for row in matrix:
		new_row = []

		for val in row:
			new_val = val * scalar
			new_row.append(new_val)
		
		res.append(new_row)
	
	return res
		