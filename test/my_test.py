# testing-123/test/my_script_test.py

from app.my_script import enlarge


def test_enlarge():
    result = enlarge(3)
    assert result == 300
