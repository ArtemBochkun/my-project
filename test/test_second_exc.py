import pytest
from zadachi.second_exc import solution_choice

def test_second_exc():
    assert solution_choice("+", 1, 2) == 3
    assert solution_choice("-", 1, 2) == -1
