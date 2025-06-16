import pytest

from tas_helpers.metrics.mof import mof_score

def test_identical_predictions():
    y_true = [1, 0, 1, 1, 0]
    y_pred = [1, 0, 1, 1, 0]
    assert mof_score(y_true, y_pred) == 1.0

def test_completely_different_predictions():
    y_true = [1, 0, 1, 1, 0]
    y_pred = [0, 1, 0, 0, 1]
    assert mof_score(y_true, y_pred) == 0.0

def test_partial_correct_predictions():
    y_true = [1, 0, 1, 1, 0]
    y_pred = [1, 1, 1, 0, 0]
    assert mof_score(y_true, y_pred) == 0.4

def test_empty_sequences():
    y_true = []
    y_pred = []
    assert mof_score(y_true, y_pred) == 0.0

def test_one_correct_prediction():
    y_true = [1]
    y_pred = [1]
    assert mof_score(y_true, y_pred) == 1.0

def test_one_incorrect_prediction():
    y_true = [1]
    y_pred = [0]
    assert mof_score(y_true, y_pred) == 0.0

def test_large_input():
    y_true = [1] * 1000 + [0] * 1000
    y_pred = [1] * 800 + [0] * 200 + [1] * 100 + [0] * 700
    assert mof_score(y_true, y_pred) == 0.9

def test_all_zero_predictions():
    y_true = [1, 1, 1, 1]
    y_pred = [0, 0, 0, 0]
    assert mof_score(y_true, y_pred) == 0.0

def test_all_one_predictions():
    y_true = [0, 0, 0, 0]
    y_pred = [1, 1, 1, 1]
    assert mof_score(y_true, y_pred) == 0.0

def test_mixed_predictions():
    y_true = [1, 0, 1, 1, 0, 1, 0]
    y_pred = [1, 0, 1, 0, 0, 1, 1]
    assert mof_score(y_true, y_pred) == 0.8571428571428571