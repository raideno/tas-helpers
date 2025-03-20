from typing import List, Any
from Levenshtein import distance

# SOURCE: https://arxiv.org/pdf/2210.10352
# NOTE: compute the edit distance (Levenshtein distance) between two sequences
def edit_score(y_true: List[Any], y_pred: List[Any]) -> int:
    return (1 - (distance(y_true, y_pred) / max(len(y_true), len(y_pred))))