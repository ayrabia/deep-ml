import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# Your code here
	
	#standardization
	means = np.mean(data, axis = 0)
	stds = np.std(data, axis = 0)
	standardized_data = (data - means) / stds

	#min-max normalization
	mins = np.min(data, axis = 0)
	maxes = np.max(data, axis = 0)
	min_max_data = (data - mins)/ (maxes - mins)

	return np.round(standardized_data, 4), np.round(min_max_data, 4)

