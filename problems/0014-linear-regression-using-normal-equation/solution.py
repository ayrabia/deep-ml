import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# Your code here, make sure to round
	#theta = (X^T * X)^-1 X^T * y
	#thetta: output vector of coefficients
	#X: input matrix of features
	#X^T: Transpose of matrix X
	# y input target vector
	X = np.array(X)
	y = np.array(y)

	XT = np.transpose(X)
	dot = np.dot(XT, X)
	inv_dot = np.linalg.inv(dot)
	XTT = np.dot(inv_dot, XT)
	final = np.dot(XTT, y)

	theta = np.round(final, 4).tolist()

	return theta