def diagonalDifference(arr):
    primary_diagonal = 0 
    second_diagonal = 0
    for i in range (len(arr)):
        primary_diagonal += arr[i][i]
        second_diagonal += arr[i][len(arr)-1-i]
    return abs(primary_diagonal - second_diagonal)
