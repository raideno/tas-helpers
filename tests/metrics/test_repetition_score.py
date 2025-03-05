import pytest

from tas_helpers.scores.repetition_score import repetition_score

def test_empty_sequence():
    assert repetition_score([]) == 0.0

def test_single_action_sequence():
    assert repetition_score(['fry pancake', 'fry pancake', 'fry pancake']) == 0

def test_no_repetition_sequence():
    assert repetition_score(['fry pancake', 'pour water', 'fry egg', 'stir fry egg']) == 0.0

def test_some_repetition_sequence():
    assert repetition_score(['fry pancake', 'pour water', 'fry pancake', 'fry egg', 'fry pancake']) == 1 - (3 / 5)

def test_all_repeated_actions():
    assert repetition_score(['fry pancake', 'fry pancake', 'fry pancake', 'fry pancake']) == 0

def test_multiple_unique_actions():
    assert repetition_score(['fry pancake', 'pour water', 'fry egg', 'cut fruit']) == 0.0

def test_repetition_within_long_sequence():
    assert repetition_score(['fry pancake', 'pour water', 'cut fruit', 'fry pancake', 'pour water', 'cut fruit']) == 1 - (3 / 6)

def test_large_sequence_with_no_repetition():
    assert repetition_score(['action' + str(i) for i in range(100)]) == 0.0

def test_large_sequence_with_full_repetition():
    assert repetition_score(['action'] * 100) == 0

def test_sequence_with_background_action():
    sequence = ['fry pancake', 'pour water', 'SIL', 'fry pancake', 'pour water', 'SIL']
    assert repetition_score(sequence) == 1 - (3 / 6)

def test_single_action_with_intermittent_change():
    sequence = ['fry pancake', 'pour water', 'fry pancake']
    assert repetition_score(sequence) == 1 - (2 / 3)