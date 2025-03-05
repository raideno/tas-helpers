from typing import List, Tuple

def compute_iou(pred_start: int, pred_end: int, gt_start: int, gt_end: int) -> float:
    """Calculate the Intersection over Union (IoU) for two segments."""
    intersection_start = max(pred_start, gt_start)
    intersection_end = min(pred_end, gt_end)
    intersection = max(0, intersection_end - intersection_start)
    
    union_start = min(pred_start, gt_start)
    union_end = max(pred_end, gt_end)
    union = max(0, union_end - union_start)
    
    if union == 0:
        return 0.0
    return intersection / union

def f1_score(pred_segments: List[Tuple[int, int]], gt_segments: List[Tuple[int, int]], tau: float = 25) -> float:
    """
    Compute the F1 score based on IoU with respect to the threshold tau.
    
    Args:
        pred_segments: A list of predicted segments [(start1, end1), (start2, end2), ...]
        gt_segments: A list of ground truth segments [(start1, end1), (start2, end2), ...]
        tau: The IoU threshold for considering a prediction as true positive.
    
    Returns:
        The F1 score as a float.
    """
    true_positives = 0
    false_positives = 0
    false_negatives = 0
    
    # NOTE: for each predicted segment, check its IoU with ground truth segments
    for pred_start, pred_end in pred_segments:
        matched = False
        for gt_start, gt_end in gt_segments:
            iou = compute_iou(pred_start, pred_end, gt_start, gt_end)
            if iou >= tau / 100:  # Threshold comparison
                true_positives += 1
                matched = True
                break
        if not matched:
            false_positives += 1
    
    # NOTE: for ground truth, count false negatives
    for gt_start, gt_end in gt_segments:
        matched = False
        for pred_start, pred_end in pred_segments:
            iou = compute_iou(pred_start, pred_end, gt_start, gt_end)
            if iou >= tau / 100:
                matched = True
                break
        if not matched:
            false_negatives += 1
    
    # NOTE: calculate precision, recall and F1 score
    precision = true_positives / (true_positives + false_positives) if (true_positives + false_positives) > 0 else 0
    recall = true_positives / (true_positives + false_negatives) if (true_positives + false_negatives) > 0 else 0
    
    if precision + recall == 0:
        return 0.0
    return 2 * (precision * recall) / (precision + recall)