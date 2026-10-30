import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	
	#compare current count to proposed count
	current_elements = len(a) * len(a[0])
	target_elements = new_shape[0] * new_shape[1]

	if current_elements != target_elements:
		return []
	
	np_matrix = np.array(a)
	reshaped = np.reshape(np_matrix, new_shape)

	return reshaped