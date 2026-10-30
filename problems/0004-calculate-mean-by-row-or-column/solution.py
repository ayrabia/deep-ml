def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	
	
	if mode == 'row':
		row_mean = []
		for row in matrix:
			
			mean = sum(row) / len(row)
			row_mean.append(mean)
		return row_mean

	elif mode == 'column':
		col_mean = []
		for i in range(len(matrix[0])):
			column_sum = 0
			for j in range(len(matrix)):
				column_sum += matrix[j][i]
			
			mean = column_sum/len(matrix)
			col_mean.append(mean)
		return col_mean
