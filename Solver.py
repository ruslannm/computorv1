class Solver:
    def __init__(self, parser):
        self._degree = parser.get_degree()
        self._power_and_coef = parser.get_power_and_coef()
        self._answer = {}
        self.solve()

    def solve(self):
        if self._degree > 2:
            raise BaseException(f"The polynomial degree is strictly greater than 2, I can't solve.")
        elif self._degree == 1:
            self._simple_equation()
        else:
            self._not_equation()

    def _simple_equation(self):
        if self._power_and_coef.get(0, 0.0) == 0.0:
            self._answer[0] = 0
        else:
            a, b = self._power_and_coef.get(0, 0.0), self._power_and_coef.get(1, 0.0)
            self._answer[0] = - a / b
        print("The solution is:")

    def not_equation(self):
        if self._power_and_coef.get(0, 0.0) == 0.0:
            raise BaseException(f"Any real number is a solution")
        else:
            raise BaseException(f"No solutions")
