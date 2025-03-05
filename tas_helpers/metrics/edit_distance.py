import numpy as np

from typing import List, Any

# NOTE: compute the edit distance (Levenshtein distance) between two sequences
def edit_distance(X: List[Any], Y: List[Any]) -> int:
    m, n = len(X), len(Y)
    dp = np.zeros((m + 1, n + 1), dtype=int)

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    
    return dp[m][n]