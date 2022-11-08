import re

class Parser:
    def __init__(self, polynom):
        self._raw_polynom = polynom
        self._polynom = polynom
        self._power_and_coef = {}
        self._degree = 0
        self._reduced_form = ''
        self._set_power_and_coef()
        self._set_reduced_forms()

    def _set_power_and_coef(self):
        try:
            raw_left, raw_right = self._raw_polynom.split('=')
        except Exception as e:
            raise BaseException(f'ERROR: equation: "{self._raw_polynom}" should has "="')
        left_tokens = self._get_tokens(raw_left)
        right_tokens = self._get_tokens(raw_right)
        left_tokens.update({key: left_tokens[key] - right_tokens[key] for key in right_tokens if key in left_tokens})
        left_tokens.update({key: -right_tokens[key] for key in right_tokens if key not in left_tokens})
        self._power_and_coef = {power : coef for power, coef in sorted(left_tokens.items()) if coef != 0.0}

    def _get_tokens(self, side: str):
        side = side.replace(" ", "")
        tokens = {}
        pattern_token = re.compile(r'[+-]?[^+-]*')
        pattern = re.compile(r'^((?P<sign>[+-]?)(?P<coef>(\d+\.)?\d+)(\*?(?P<X>X)(\^(?P<power>\d+))?)?)$')
        for raw_token in list(filter(None, pattern_token.findall(side))):
            token = pattern.match(raw_token)
            if token is None:
                raise BaseException(f'ERROR: equation "{self._raw_polynom}" has bad format')
            sign = token.group('sign')
            coef = float(token.group('coef') or 1)
            x = token.group('X')
            power = int(token.group('power') or 1 if x else 0)
            if sign == '-':
                coef = -coef
            if power in tokens:
                tokens[power] += coef
            else:
                tokens[power] = coef
        return tokens

    def _set_reduced_forms(self):
        if self._power_and_coef:
            self._degree = max(self._power_and_coef)
            for degree in range(self._degree + 1):
                coef = self._power_and_coef.get(degree, 0)
                if coef < 0:
                    if degree == 0:                
                        self._reduced_form += "-"
                    else:
                        self._reduced_form += " - "
                    coef = -coef
                elif coef >= 0:
                    if degree > 0:                
                        self._reduced_form += " + "
                coef = self.coef_to_str(coef)
                self._reduced_form += f"{coef} * X^{degree}"
        else:
            raise BaseException(f'ERROR: in equation "{self._raw_polynom}" each real number is a solution')
        self._reduced_form += " = 0"
        print(f"Reduced form: {self._reduced_form}")
        print(f"Polynomial degree: {self._degree}")

    @staticmethod
    def coef_to_str(coef: float):
        coef_int = int(coef)
        if coef - coef_int == 0.0:
            coef = coef_int
        return str(coef)

    def get_degree(self):
        return self._degree

    def get_power_and_coef(self):
        return self._power_and_coef
