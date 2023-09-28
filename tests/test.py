import pytest
from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding(self):
        assert self.calc.adding(self, 2, 2) == 4

    def test_multiply(self):
        assert self.calc.multiply(self, 5, 5) == 25

    def test_division(self):
        assert self.calc.division(self, 49, 7) == 7

    def test_subtraction(self):
        assert self.calc.subtraction(self, 50, 10) == 40

