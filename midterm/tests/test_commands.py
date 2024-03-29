import pytest
from app import App
import calculator 
from app.plugins.add import AddCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.divide import DivideCommand

def test_add_command():
    a = 2
    b = 1
    assert calculator.add(a, b) == 3
    
def test_subtract_command():
    a = 21
    b = 9
    assert calculator.subtract(a, b) == 12

def test_multiply_command():
    a = 17
    b = 17
    assert calculator.multiply(a, b) == 289

def test_divide_command():
    a = 14
    b = 2 
    assert calculator.divide(a, b) == 7