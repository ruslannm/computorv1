from Parser import Parser
from Solver import Solver, EPS
import pytest

def test_error_sign_1():
    equation = "5 * X^0 + -- 9.3 * X^3 = 1 * X^0"
    with pytest.raises(BaseException) as e_info:
        parser = Parser(equation)

def test_error_sign_2():
    equation = "--5 * X^0 - 9.3 * X^3 = 1 * X^0"
    with pytest.raises(BaseException) as e_info:
        parser = Parser(equation)

def test_error_operator_1():
    equation = "5 * X^0 - 9.3 * 5 * X^3 = 1 * X^0"
    with pytest.raises(BaseException) as e_info:
        parser = Parser(equation)

def test_error_characters():
    equation = "5 eggs = 1 * X^0"
    with pytest.raises(BaseException) as e_info:
        parser = Parser(equation)

def test_error_equal_1():
    equation = "5 * X = 1 * X^0 = 3 * X"
    with pytest.raises(BaseException) as e_info:
        parser = Parser(equation)

def test_error_equal_2():
    equation = "5 * X + 1 * X"
    with pytest.raises(BaseException) as e_info:
        parser = Parser(equation)

def test_coef_to_str_1():
	nb = 1.0
	assert Parser.coef_to_str(nb) == "1"

def test_coef_to_str_2():
	nb = 1.1
	assert Parser.coef_to_str(nb) == "1.1"

def test_reduced_form_1():
    equation = "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
    parser = Parser(equation)
    assert parser.reduced_form == "4 * X^0 + 4 * X^1 - 9.3 * X^2 = 0"
    assert parser.reduced_free_form == "4 + 4 * X - 9.3 * X^2 = 0"

def test_reduced_form_2():
    equation = "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 5 * X^0"
    parser = Parser(equation)
    assert parser.reduced_form == "0 * X^0 + 4 * X^1 - 9.3 * X^2 = 0"
    assert parser.reduced_free_form == "4 * X - 9.3 * X^2 = 0"

def test_degree_1():
    equation = "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
    parser = Parser(equation)
    assert parser.degree == 2

def test_reduced_form_2():
    equation = "5 * X^0 + 4 * X^1 = 4 * X^0"
    parser = Parser(equation)
    assert parser.reduced_form == "1 * X^0 + 4 * X^1 = 0"

def test_degree_2():
    equation = "5 * X^0 + 4 * X^1 = 4 * X^0"
    parser = Parser(equation)
    assert parser.degree == 1

def test_reduced_form_3():
    equation = "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0"
    parser = Parser(equation)
    assert parser.reduced_form == "5 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 0"    

def test_degree_3():
    equation = "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0"
    parser = Parser(equation)
    assert parser.degree == 3

def test_sqrt_1():
    assert abs(Solver.sqrt(0) - 0.0) < EPS

def test_sqrt_2():
    assert abs(Solver.sqrt(1) - 1.0) < EPS

def test_sqrt_3():
    assert abs(Solver.sqrt(4) - 2.0) < EPS

def test_sqrt_4():
    assert abs(Solver.sqrt(5) - 2.236067977) < EPS

def test_sqrt_5():
    assert abs(Solver.sqrt(0.5) - 0.70710678) < EPS

def test_sqrt_6():
    assert abs(Solver.sqrt(100.0) - 10.0) < EPS

def test_0_degree_1():
    equation = "5 * X^0 = 5 * X^0"
    with pytest.raises(BaseException) as e_info:
        parser = Parser(equation)

def test_0_degree_2():
    equation = "4 * X^0 = 8 * X^0"
    with pytest.raises(BaseException) as e_info:
        parser = Parser(equation)
        solver = Solver(parser)

def test_1_degree_1():
    equation = "5 * X^0 = 4 * X^0 + 7 * X^1"
    parser = Parser(equation)
    solver = Solver(parser)        
    assert abs(solver.answer[0] - 0.14285714285714285) < EPS

def test_1_degree_2():
    equation = "5 * X^0 = 4 * X^0 + 2 * X^1"
    parser = Parser(equation)
    solver = Solver(parser)        
    assert abs(solver.answer[0] - 0.5) < EPS    

def test_1_degree_3():
    equation = "500.05 * X^0 = 4 * X^0 + X^1"
    parser = Parser(equation)
    solver = Solver(parser)        
    assert abs(solver.answer[0] - 496.05) < EPS      

def test_1_degree_4():
    equation = "500000000000000000000000000000.05 * X^0 = 4 * X^0 + 20000000 * X^1"
    parser = Parser(equation)
    solver = Solver(parser)        
    assert abs(solver.answer[0] - 2.5000000000000002e+22) < EPS  

def test_1_degree_5():
    equation = "0.0000000000000000000000000000005 * X^0 = 0 * X^0 + X^1"
    parser = Parser(equation)
    solver = Solver(parser)        
    assert abs(solver.answer[0] - 5e-31) < EPS          

def test_2_degree_1():
    equation = "5 * X^0 + 13 * X^1 + 3 * X^2 = 1 * X^0 + 1 * X^1"
    parser = Parser(equation)
    solver = Solver(parser)        
    assert abs(solver.answer[0] + 0.367006838131146) < EPS
    assert abs(solver.answer[1] + 3.6329931618688542) < EPS    

def test_2_degree_2():
    equation = "5 * X^0 + 13 * X^1 + 3 * X^2 = 1 * X^0 + 1 * X^1 + 100"
    parser = Parser(equation)
    solver = Solver(parser)        
    assert abs(solver.answer[0] - 4.0) < EPS
    assert abs(solver.answer[1] + 8.0) < EPS    

def test_2_degree_3():
    equation = "5 * X^0 + 12 * X^1 + 3 * X^2 = 5 * X^0"
    parser = Parser(equation)
    solver = Solver(parser)        
    assert abs(solver.answer[0] - 0.0) < EPS
    assert abs(solver.answer[1] + 4.0) < EPS

def test_2_degree_4():
    equation = "5 * X^0 + 0 * X^1 + 3 * X^2 = 6 * X^0"
    parser = Parser(equation)
    solver = Solver(parser)        
    assert abs(solver.answer[0] - 0.5773502700049091) < EPS
    assert abs(solver.answer[1] + 0.5773502700049091) < EPS

def test_2_degree_zero_3():
    equation = "6 * X^0 + 11 * X^1 + 5 * X^2 = 1 * X^0 + 1 * X^1"
    parser = Parser(equation)
    solver = Solver(parser)        
    assert abs(solver.answer[0] + 1.0) < EPS

def test_2_degree_negative_1():
    equation = "5 * X^0 + 3 * X^1 + 3 * X^2 = 1 * X^0 + 0 * X^1"
    parser = Parser(equation)
    solver = Solver(parser)        
    assert solver.answer[0] == "-0.5 + 1.04083 * i"
    assert solver.answer[1] == "-0.5 - 1.04083 * i"

def test_2_degree_complex_1():
    equation = "5 * X^0 + 0 * X^1 + 3 * X^2 = 4 * X^0"
    parser = Parser(equation)
    solver = Solver(parser)        
    assert solver.answer[0] == "0.57735 * i"
    assert solver.answer[1] == "-0.57735 * i"

def test_3_degree_1():
    equation = "5 * X^0 + 13 * X^1 + 3 * X^2 + 5 * X^3 = 1 * X^0 + 1 * X^1 + 100 + 5 * X^3"
    parser = Parser(equation)
    solver = Solver(parser)        
    assert abs(solver.answer[0] - 4.0) < EPS
    assert abs(solver.answer[1] + 8.0) < EPS
    