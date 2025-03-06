from typing import List, Any
from Levenshtein import distance

# NOTE: compute the edit distance (Levenshtein distance) between two sequences
def edit_distance(X: List[Any], Y: List[Any]) -> int:
    return distance(X, Y)