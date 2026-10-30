def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    transposed = []
    #iterate through the number of columns
    for i in range(len(a[0])):
        new_row = []
        #iterate through the rows
        for j in range(len(a)):
            new_row.append(a[j][i])
    
        transposed.append(new_row)
    return transposed
