import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	#2 * 4 = 8
	current_elements = len(a) * len(a[0])
	#4 * 2 = 8
	target_elements = new_shape[0] * new_shape[1]

	if current_elements != target_elements:
		return []
	
	#use numpy to reshaping
	np_matrix = np.array(a)
	reshaped = np.reshape(np_matrix, new_shape)

	return reshaped.tolist()