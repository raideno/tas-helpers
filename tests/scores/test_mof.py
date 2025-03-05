import pytest

import numpy as np

from tas_helpers.metrics.mof import mean_over_frames

def test_identical_predictions():
    y_true = np.array([1, 0, 1, 1, 0])
    y_pred = np.array([1, 0, 1, 1, 0])
    assert mean_over_frames(y_true, y_pred) == 1.0

def test_completely_different_predictions():
    y_true = np.array([1, 0, 1, 1, 0])
    y_pred = np.array([0, 1, 0, 0, 1])
    assert mean_over_frames(y_true, y_pred) == 0.0

def test_partial_correct_predictions():
    y_true = np.array([1, 0, 1, 1, 0])
    y_pred = np.array([1, 1, 1, 0, 0])
    assert mean_over_frames(y_true, y_pred) == 0.4

def test_empty_sequences():
    y_true = np.array([])
    y_pred = np.array([])
    assert mean_over_frames(y_true, y_pred) == 0.0

def test_one_correct_prediction():
    y_true = np.array([1])
    y_pred = np.array([1])
    assert mean_over_frames(y_true, y_pred) == 1.0

def test_one_incorrect_prediction():
    y_true = np.array([1])
    y_pred = np.array([0])
    assert mean_over_frames(y_true, y_pred) == 0.0

def test_large_input():
    y_true = np.array([1] * 1000 + [0] * 1000)
    y_pred = np.array([1] * 800 + [0] * 200 + [1] * 100 + [0] * 700)
    assert mean_over_frames(y_true, y_pred) == 0.9

def test_all_zero_predictions():
    y_true = np.array([1, 1, 1, 1])
    y_pred = np.array([0, 0, 0, 0])
    assert mean_over_frames(y_true, y_pred) == 0.0

def test_all_one_predictions():
    y_true = np.array([0, 0, 0, 0])
    y_pred = np.array([1, 1, 1, 1])
    assert mean_over_frames(y_true, y_pred) == 0.0

def test_mixed_predictions():
    y_true = np.array([1, 0, 1, 1, 0, 1, 0])
    y_pred = np.array([1, 0, 1, 0, 0, 1, 1])
    assert mean_over_frames(y_true, y_pred) == 0.8571428571428571