from logic_utils import check_guess, update_score, get_range_for_difficulty


def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


def test_hint_too_high_says_go_lower():
    # When guess is too high, player should be told to go lower
    _, message = check_guess(60, 50)
    assert "LOWER" in message


def test_hint_too_low_says_go_higher():
    # When guess is too low, player should be told to go higher
    _, message = check_guess(40, 50)
    assert "HIGHER" in message


def test_update_score_too_high_deducts():
    # Wrong guesses should always deduct, never reward
    score = update_score(100, "Too High", 2)
    assert score < 100


def test_update_score_too_low_deducts():
    score = update_score(100, "Too Low", 1)
    assert score < 100


def test_hard_difficulty_range_harder_than_normal():
    # Hard should have a larger range than Normal
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert hard_high > normal_high
