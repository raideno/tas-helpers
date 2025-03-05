import pytest

from tas_helpers.metrics.edit_distance import edit_distance

def test_empty_sequences():
    assert edit_distance([], []) == 0

def test_identical_sequences():
    assert edit_distance([1, 2, 3], [1, 2, 3]) == 0

def test_completely_different_sequences():
    assert edit_distance([1, 2, 3], [4, 5, 6]) == 3

def test_partial_match_sequences():
    assert edit_distance([1, 2, 3], [1, 3, 2]) == 2

def test_different_lengths():
    assert edit_distance([1, 2, 3], [1, 2, 3, 4]) == 1
    assert edit_distance([1, 2, 3, 4], [1, 2, 3]) == 1

def test_one_empty_sequence():
    assert edit_distance([], [1, 2, 3]) == 3
    assert edit_distance([1, 2, 3], []) == 3

def test_string_sequences():
    assert edit_distance("kitten", "sitting") == 3
    assert edit_distance("saturday", "sunday") == 3

def test_mixed_type_sequences():
    assert edit_distance([1, "a", True], [1, "a", True]) == 0
    assert edit_distance([1, "a", True], [1, "b", True]) == 1

def test_insertion():
    assert edit_distance([1, 2, 3], [1, 4, 2, 3]) == 1

def test_deletion():
    assert edit_distance([1, 2, 3, 4], [1, 3, 4]) == 1

def test_substitution():
    assert edit_distance([1, 2, 3], [1, 5, 3]) == 1

def test_complex_case():
    assert edit_distance([1, 2, 3, 4, 5], [2, 3, 1, 5, 6]) == 3
