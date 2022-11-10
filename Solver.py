EPS = 0.00000001

class Solver:
    def __init__(self, parser, verbose=False):
        self._degree = parser.degree
        self._power_and_coef = parser.power_and_coef
        self._verbose = verbose
        self.answer = []
        self._solve()
        self._print()

    def _solve(self):
        if self._degree > 2:
            raise BaseException(f"The polynomial degree is strictly greater than 2, I can't solve.")
        elif self._degree == 2:
            self._square_equation()
        elif self._degree == 1:
            self._simple_equation()
        else:
            self._not_equation()

    def _square_equation(self):
        count_coefs = len(self._power_and_coef)
        if self._verbose:
            print(f"Number of terms in the equation 'ax^2 + bx + c = 0' : {count_coefs}")
        if count_coefs == 3:
            c, b, a = [value for _, value in self._power_and_coef.items()]
            discriminant = b ** 2 - 4 * a * c
            term_1 = -b / (2.0 * a)
            if self._verbose:
                print(f"a = {a}, b = {b}, c = {c}")
                print(f"Discriminant d = b^2 - 4ac = {discriminant}")
                print(f"First term of solution = -b / 2a = {term_1:.6}")
            if discriminant > 0:
                print(f"Discriminant is strictly positive, the two solutions are:")
                term_2 = self.sqrt(discriminant) / (2.0 * a)            
                self.answer.append(term_1 + term_2)
                self.answer.append(term_1 - term_2)
                if self._verbose:
                    print(f"Second term of solution sqrt(d) / 2a = {term_2:.6}")
                    print(f"Solutions: term_1 + term2, term_1 - term2")
            elif discriminant == 0:
                print("Discriminant is zero, the solutions is:")
                self.answer.append(term_1)
                if self._verbose:
                    print(f"Solution: -b / 2a")
            else:
                print(f"Discriminant < 0: the two complex solutions are:")
                term_2 = self.sqrt(-discriminant) / (2.0 * a)
                self.answer.append(f"{term_1:.6} + {term_2:.6} * i")
                self.answer.append(f"{term_1:.6} - {term_2:.6} * i")
                if self._verbose:
                    print(f"Second term of solution sqrt(d) / 2a = {term_2:.6}")
                    print(f"Solutions: term_1 + term2 * i, term_1 - term2 * i")
        elif count_coefs == 2:
            if self._power_and_coef.get(0, 0) == 0:
                b, a = [value for _, value in self._power_and_coef.items()]    
                self.answer.append(0)
                self.answer.append(-b / a)
                if self._verbose:
                    print(f"a = {a}, b = {b}, c = 0")
                    print(f"Solutions: 0, -b / a")
            elif self._power_and_coef.get(1, 0) == 0:
                c, a = [value for _, value in self._power_and_coef.items()]    
                term_2 = -c / a
                if self._verbose:
                    print(f"a = {a}, b = 0, c = {c}")
                    print(f"First step of solution = -c / a = {term_2:.6}")
                if term_2 > 0:
                    term_2 = self.sqrt(term_2)
                    self.answer.append(term_2)
                    self.answer.append(-term_2)
                    if self._verbose:
                        print(f"Second step of solution term = sqrt(-c / a) = {term_2:.6}")
                        print(f"Solutions: sqrt(-a /c), -sqrt(-a /c)")
                else:
                    print(f"The two complex solutions are:")      
                    term_2 = self.sqrt(-term_2)
                    self.answer.append(f"{term_2:.6} * i")
                    self.answer.append(f"{-term_2:.6} * i")
                    if self._verbose:
                        print(f"Second step of solution term = sqrt(c / a) = {term_2:.6}")
                        print(f"Solutions: sqrt(a /c) * i, -sqrt(a /c) * i")
        else:
            self.answer.append(0)

    def _simple_equation(self):
        count_coefs = len(self._power_and_coef)
        if self._verbose:
            print(f"Number of terms in the equation 'bx + c = 0' : {count_coefs}")
        if count_coefs == 1:
            self.answer.append(0)
            if self._verbose:
                print(f"c = 0\nSolution: 0")
        else:
            c, b = self._power_and_coef.get(0, 0.0), self._power_and_coef.get(1, 0.0)
            self.answer.append(-c / b)
            if self._verbose:
                print(f"b = {b}, c = {c}")
                print(f"Solutions: -c / b")
        print("The solution is:")

    def _not_equation(self):
        if self._power_and_coef.get(0, 0.0) == 0.0:
            raise BaseException(f"Any real number is a solution")
        else:
            raise BaseException(f"ERROR: No solutions")

    def _print(self):
        for answer in self.answer:
            if isinstance(answer, float):
                print(f"{answer:.6}")
            else:
                print(answer)


    @staticmethod
    def sqrt(n):
        if n in (0.0, 1.0):
            return n
        x = 1.0
        while True:
            x_next = (x + n / x) / 2.0
            if abs(x - x_next) < EPS:
                break
            x = x_next
        return x


