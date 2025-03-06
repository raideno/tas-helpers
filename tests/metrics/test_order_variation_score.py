import pytest

from tas_helpers.scores.order_variation import order_variation_score

def test_empty_sequence():
    assert order_variation_score([[]]) == 1.0

def test_single_video_sequence():
    assert order_variation_score([['fry pancake', 'pour water', 'fry egg']]) == 1.0

def test_identical_sequences():
    sequence = [['fry pancake', 'pour water', 'fry egg'], ['fry pancake', 'pour water', 'fry egg']]
    assert order_variation_score(sequence) == 1.0

def test_completely_different_sequences():
    sequence = [['fry pancake', 'pour water', 'fry egg'], ['cut fruit', 'pour milk', 'stir tea']]
    assert order_variation_score(sequence) == 0.0

def test_partial_match_sequences():
    sequence = [['fry pancake', 'pour water', 'fry egg'], ['fry pancake', 'pour milk', 'stir tea']]
    assert order_variation_score(sequence) < 1.0

def test_multiple_different_sequences():
    sequence = [['fry pancake', 'pour water', 'fry egg'],
                ['cut fruit', 'pour milk', 'stir tea'],
                ['fry egg', 'pour water', 'cut fruit']]
    assert order_variation_score(sequence) < 1.0

def test_sequence_with_background_action():
    sequence = [['fry pancake', 'pour water', 'SIL', 'fry egg'],
                ['fry pancake', 'SIL', 'pour water', 'fry egg']]
    assert order_variation_score(sequence) < 1.0

def test_large_identical_sequences():
    sequence = [['fry pancake', 'pour water', 'fry egg']] * 100
    assert order_variation_score(sequence) == 1.0

def test_large_different_sequences():
    sequence = [['fry pancake', 'pour water', 'fry egg'], 
                ['cut fruit', 'pour milk', 'stir tea']] * 50
    assert round(order_variation_score(sequence), 1) == 0.5