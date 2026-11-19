import numpy as np
def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    if not a or not a[0]:
        return []
    #asaarry turns python list into numpy array
    #tolist() turns the numpyarray back to a standard python list
    return np.asarray(a).transpose().tolist()