from logic_utils import check_guess


# Bug: app.py corrupts secret to str on even attempts, causing backwards hints

def test_hint_go_higher_int_secret():
    # guess 50, secret 75 → should say go HIGHER
    outcome, message = check_guess(50, 75)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_hint_go_lower_int_secret():
    # guess 90, secret 75 → should say go LOWER
    outcome, message = check_guess(90, 75)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_hint_go_higher_string_secret():
    # same scenario but secret passed as str (even-attempt bug path)
    outcome, message = check_guess(50, "75")
    assert outcome == "Too Low", f"Backwards hint: got '{outcome}', expected 'Too Low'"
    assert "HIGHER" in message

def test_hint_go_lower_string_secret():
    outcome, message = check_guess(90, "75")
    assert outcome == "Too High", f"Backwards hint: got '{outcome}', expected 'Too High'"
    assert "LOWER" in message

def test_win_int_secret():
    outcome, _ = check_guess(75, 75)
    assert outcome == "Win"

def test_win_string_secret():
    outcome, _ = check_guess(75, "75")
    assert outcome == "Win"
