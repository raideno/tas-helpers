import numpy as np

from typing import List, Any
from Levenshtein import distance

# SOURCE: https://arxiv.org/pdf/2210.10352
def order_variation_score(frame_level_videos_annotations: List[List[Any]]) -> float:
    """
    The Order Variation Score measures how consistent the order of actions is across different videos / sequences / activities.
    - 1 Indicates no deviations in ordering between action paris.
    - A lower score indicates a higher amount of ordering variations.
    """
    num_videos = len(frame_level_videos_annotations)
    total_edit_distance = 0
    max_length = 0
    
    # NOTE: compute the total edit distance and find the maximum sequence length
    for i in range(num_videos):
        for j in range(i + 1, num_videos):
            edit_dist = distance(frame_level_videos_annotations[i], frame_level_videos_annotations[j])
            total_edit_distance += edit_dist
            max_length = max(max_length, len(frame_level_videos_annotations[i]), len(frame_level_videos_annotations[j]))

    # NOTE: normalize by the maximum sequence length
    if num_videos > 1:
        average_edit_distance = total_edit_distance / (num_videos * (num_videos - 1) / 2)  # average over all pairs
        order_variation = 1 - (average_edit_distance / max_length)
    else:
        # NOTE: no variation if we have one video only
        order_variation = 1.0
    
    return order_variation