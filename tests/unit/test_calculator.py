from src.calculator import (
    Summation, 
    Subtraction, 
    Multiplication, 
    Division
)

def test_Summation():
    """
    Testing Summation function
    """
    assert Summation(2, 10) == 12
    assert Summation(3, 5) == 8
    assert Summation(4, 6) == 10

def test_Subtraction():
    """
    Testing Subtraction function
    """
    assert Subtraction(8, 2) == 6
    assert Subtraction(7, 5) == 2
    assert Subtraction(4, 2) == 2

def test_Multiplication():
    """
    Testing Multiplication function
    """
    assert Multiplication(2, 2) == 4
    assert Multiplication(7, 2) == 14
    assert Multiplication(10, 2) == 20

def test_Division():
    """
    Testing Division function
    """
    assert Division(5, 5) == 1
    assert Division(70, 10) == 7
    assert Division(16, 4) == 4