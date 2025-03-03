import numpy as np

from typing import List, Tuple, Any

DEFAULT_FALLBACK_LABEL = "none"

def segment_level_annotations_to_frame_level_annotations(
    annotations: List[Tuple[str, float, float]],
    fps: int,
    fallback_label: Any = DEFAULT_FALLBACK_LABEL
) -> List[str]:
    pass

def frame_level_annotations_to_segment_level_annotations(
    annotations: List[Any],
    fps: int
) -> List[Tuple[str, float, float]]:
    labels = list(set(annotations))
    
    grouped_labels = []
    current_label = annotations[0]
    starting_frame = 0

    for i, label in enumerate(annotations):
        if label != current_label:
            # NOTE: convert frame indices to time in milliseconds
            starting_timestamp = (starting_frame / fps) * 1000
            ending_timestamp = ((i - 1) / fps) * 1000
            grouped_labels.append((current_label, starting_timestamp, ending_timestamp))
            current_label = label
            starting_frame = i
            
    # NOTE: handle the last segment
    starting_timestamp = (starting_frame / fps) * 1000
    ending_timestamp = ((len(annotations) - 1) / fps) * 1000
    grouped_labels.append((current_label, starting_timestamp, ending_timestamp))
    
    return grouped_labels

def generate_random_segmentation(
    length: int = 1000, 
    labels: list = None, 
    min_segment_length: int = 25, 
    max_segment_length: int = 250
) -> list:
    """
    Generate random segmentation data for testing/examples.
    
    Args:
        length: Total number of frames
        labels: List of labels to use
        min_segment_length: Minimum segment length
        max_segment_length: Maximum segment length
    
    Returns:
        List of labels for each frame
    """
    if labels is None:
        labels = ["grimpe", "chrono", "lecture", "nothing", "brossage"]
    
    result = []
    frames_left = length
    
    while frames_left > 0:
        # NOTE: select a random label and length
        label = np.random.choice(labels)
        segment_length = min(np.random.randint(min_segment_length, max_segment_length), frames_left)
        
        # NOTE: add to the result
        result.extend([label] * segment_length)
        frames_left -= segment_length
    
    return result