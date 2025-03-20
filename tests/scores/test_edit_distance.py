import pytest

from tas_helpers.metrics.edit import edit_score

def test_empty_sequences():
    assert edit_score([], []) == 0

def test_identical_sequences():
    assert edit_score([1, 2, 3], [1, 2, 3]) == 0

def test_completely_different_sequences():
    assert edit_score([1, 2, 3], [4, 5, 6]) == 3

def test_partial_match_sequences():
    assert edit_score([1, 2, 3], [1, 3, 2]) == 2

def test_different_lengths():
    assert edit_score([1, 2, 3], [1, 2, 3, 4]) == 1
    assert edit_score([1, 2, 3, 4], [1, 2, 3]) == 1

def test_one_empty_sequence():
    assert edit_score([], [1, 2, 3]) == 3
    assert edit_score([1, 2, 3], []) == 3

def test_string_sequences():
    assert edit_score("kitten", "sitting") == 3
    assert edit_score("saturday", "sunday") == 3

def test_mixed_type_sequences():
    assert edit_score([1, "a", True], [1, "a", True]) == 0
    assert edit_score([1, "a", True], [1, "b", True]) == 1

def test_insertion():
    assert edit_score([1, 2, 3], [1, 4, 2, 3]) == 1

def test_deletion():
    assert edit_score([1, 2, 3, 4], [1, 3, 4]) == 1

def test_substitution():
    assert edit_score([1, 2, 3], [1, 5, 3]) == 1

def test_complex_case():
    assert edit_score([1, 2, 3, 4, 5], [2, 3, 1, 5, 6]) == 3
