import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# Your code here
	#row - data
	#column - feature
	#1. standardization shifts and sclaes data so that the #new values have a mean of 0 and standard deviation of 1
	means = np.mean(data, axis = 0)
	stds = np.std(data, axis = 0)
	standardized_data = (data - means)/ stds
	#2. min-max - squahes all data to fit perfectly into a strict range between 0 and 1. 
	mins = np.min(data, axis = 0)
	maxes = np.max(data, axis = 0)
	min_max_data = (data - mins) / (maxes - mins)

	return np.round(standardized_data, 4), np.round(min_max_data, 4)