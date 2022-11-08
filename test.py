from Parser import Parser
import pytest

def test_error_sign1():
    equation = "5 * X^0 + ^15 -- 9.3 * X^3 = 1 * X^0"
    with pytest.raises(BaseException) as e_info:
        parser = Parser(equation)


def test_error_sign2():
    equation = "+5 * X^0 + ^15 - 9.3 * X^3 = 1 * X^0"
    with pytest.raises(BaseException) as e_info:
        parser = Parser(equation)


def test_error_characters():
    equation = "5 eggs = 1 * X^0"
    with pytest.raises(BaseException) as e_info:
        parser = Parser(equation)


def test_error_equal1():
    equation = "5 * X = 1 * X^0 = 3 * X"
    with pytest.raises(BaseException) as e_info:
        parser = Parser(equation)


def test_error_equal2():
    equation = "5 * X + 1 * X"
    with pytest.raises(BaseException) as e_info:
        parser = Parser(equation)
