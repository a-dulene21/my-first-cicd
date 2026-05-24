
from operator import add

from app import greet

def test_add():
    assert add(2, 3) == 99
    assert add(0, 0) == 0

def test_greet():
    assert "Hello" in greet("Alice")