from typing import List, Any

from tas_helpers.utils import frame_level_annotations_to_segment_level_annotations

# SOURCE: https://arxiv.org/pdf/2210.10352
def repetition_score(frame_level_video_annotations: List[Any]) -> float:
    """
    The repetition score quantifies how much action repetition occurs within the video.
    - 0 signifies no repetitions.
    - Higher scores reflect a higher degree of repetition withing a sequence.
    
    It tell us how often actions repeat in a sequence / activity.
    
    Returns:
        float: Repetition score. Range: [0, 1]
    """
    if len(frame_level_video_annotations) == 0:
        return 0.0
    
    unique_actions_len = len(set(frame_level_video_annotations))
    
    total_number_of_actions = len(frame_level_annotations_to_segment_level_annotations(frame_level_video_annotations, 1))

    return 1 - unique_actions_len / total_number_of_actions