
from operator import add

from app import greet, greetapp

def test_add():
    assert add(2, 3) == 5
    assert add(0, 0) == 0

def test_greet():
    assert "Hello" in greet("Alice")