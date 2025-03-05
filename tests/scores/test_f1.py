import pytest

from tas_helpers.metrics.f1 import f1_score

def test_empty_sequences():
    pred_segments = []
    gt_segments = []
    assert f1_score(pred_segments, gt_segments, 25) == 0.0

def test_identical_segments():
    pred_segments = [(0, 5), (6, 10), (12, 16)]
    gt_segments = [(0, 5), (6, 10), (12, 16)]
    assert f1_score(pred_segments, gt_segments, 25) == 1.0

def test_completely_different_segments():
    pred_segments = [(0, 5), (6, 10), (12, 16)]
    gt_segments = [(20, 25), (30, 35)]
    assert f1_score(pred_segments, gt_segments, 25) == 0.0

def test_partial_overlap_segments():
    pred_segments = [(0, 5), (6, 10), (12, 16)]
    gt_segments = [(0, 6), (6, 12), (14, 18)]
    assert f1_score(pred_segments, gt_segments, 25) == 0.6666666666666666

def test_with_threshold_10():
    pred_segments = [(0, 5), (6, 10), (12, 16)]
    gt_segments = [(0, 5), (6, 9), (14, 18)]
    assert f1_score(pred_segments, gt_segments, 10) == 0.75

def test_with_threshold_50():
    pred_segments = [(0, 5), (6, 10), (12, 16)]
    gt_segments = [(0, 5), (6, 9), (14, 18)]
    assert f1_score(pred_segments, gt_segments, 50) == 0.5

def test_all_true_positives():
    pred_segments = [(0, 5), (6, 10), (12, 16)]
    gt_segments = [(0, 5), (6, 10), (12, 16), (18, 20)]
    assert f1_score(pred_segments, gt_segments, 25) == 0.8

def test_edge_case_one_pred_segment():
    pred_segments = [(0, 5)]
    gt_segments = [(0, 5), (6, 10)]
    assert f1_score(pred_segments, gt_segments, 25) == 1.0

def test_edge_case_one_gt_segment():
    pred_segments = [(0, 5), (6, 10), (12, 16)]
    gt_segments = [(0, 5)]
    assert f1_score(pred_segments, gt_segments, 25) == 1.0

def test_high_threshold_no_overlap():
    pred_segments = [(0, 5), (6, 10), (12, 16)]
    gt_segments = [(0, 5), (6, 9), (14, 18)]
    assert f1_score(pred_segments, gt_segments, 50) == 0.0