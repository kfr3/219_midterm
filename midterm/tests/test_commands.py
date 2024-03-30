"""importing calculator"""
import calculator

def test_add_command():
    """testing to see if add command works"""
    a = 2
    b = 1
    assert calculator.add(a, b) == 3

def test_subtract_command():
    """testing to see if subtract command works, takes two numbers and subtracts them"""
    a = 21
    b = 9
    assert calculator.subtract(a, b) == 12

def test_multiply_command():
    """testing to see if multiply command works"""
    a = 17
    b = 17
    assert calculator.multiply(a, b) == 289

def test_divide_command():
    """testing to see if divide command works"""
    a = 14
    b = 2
    assert calculator.divide(a, b) == 7
