import re

class Parser:
    def __init__(self, polynom, simple=False):
        self.raw_polynom = polynom
        self.power_and_coef = {}
        self.degree = 0
        self.reduced_form = ''
        self._simple = simple
        self.is_free_form = False
        self.reduced_free_form = ''
        self._set_power_and_coef()
        self._set_reduced_forms()

    def _set_power_and_coef(self):
        try:
            raw_left, raw_right = self.raw_polynom.split('=')
        except Exception as e:
            raise BaseException(f'ERROR: equation: "{self.raw_polynom}" should has "="')
        left_tokens = self._get_tokens(raw_left)
        right_tokens = {}
        if raw_right.strip() == "0":  
            right_tokens == {}
        else:
            right_tokens = self._get_tokens(raw_right)
        if self._simple:
            self._check_standart_entry_sequence(left_tokens, right_tokens)
        left_tokens.update({key: left_tokens[key] - right_tokens[key] for key in right_tokens if key in left_tokens})
        left_tokens.update({key: -right_tokens[key] for key in right_tokens if key not in left_tokens})
        self.power_and_coef = {power : coef for power, coef in sorted(left_tokens.items()) if coef != 0.0}

    def _get_tokens(self, side: str):
        side = side.replace(" ", "")
        tokens = {}
        pattern_token = re.compile(r'[+-]?[^+-]*')
        pattern = re.compile(r'^((?P<sign>[+-]?)(?P<coef>(\d+\.)?\d*)(\*?(?P<X>X)(\^(?P<power>\d+))?)?)$')
        for raw_token in list(filter(None, pattern_token.findall(side))):
            token = pattern.match(raw_token)
            if token is None or raw_token in ("+", "-"):
                raise BaseException(f'ERROR: equation "{self.raw_polynom}" has bad format')
            sign = token.group('sign')
            coef = float(token.group('coef') or 1)
            x = token.group('X')
            power = int(token.group('power') or 1 if x else 0)
            if token.group('coef') == None or token.group('X') == None or token.group('power') == None:
                self.is_free_form = True
            if sign == '-':
                coef = -coef
            if power in tokens:
                tokens[power] += coef
            else:
                tokens[power] = coef
        return tokens

    def _set_reduced_forms(self):
        if self.power_and_coef:
            self.degree = max(self.power_and_coef)
            min_degree = min(self.power_and_coef)
            for degree in range(self.degree + 1):
                coef = self.power_and_coef.get(degree, 0)
                if coef < 0:
                    if degree == min_degree:                
                        self.reduced_form += "-"
                        self.reduced_free_form += "-"
                    else:
                        self.reduced_form += " - "
                        self.reduced_free_form += " - "
                    coef = -coef
                elif coef >= 0:
                    if degree > min_degree:                
                        self.reduced_form += " + "
                        if degree in self.power_and_coef:
                            self.reduced_free_form += " + "
                coef = self.coef_to_str(coef)
                self.reduced_form += f"{coef} * X^{degree}"
                if degree in self.power_and_coef:
                    if degree == 0:
                        self.reduced_free_form += coef
                    elif degree == 1:
                        self.reduced_free_form += f"{coef} * X"
                    else:
                        self.reduced_free_form += f"{coef} * X^{degree}"
        else:
            raise BaseException(f'ERROR: in equation "{self.raw_polynom}" any real number is a solution')
        self.reduced_form += " = 0"
        self.reduced_free_form += " = 0"
        if self.is_free_form or self._simple:
            print(f"Reduced form: {self.reduced_free_form}")
        else:
            print(f"Reduced form: {self.reduced_form}")
        print(f"Polynomial degree: {self.degree}")

    
    @staticmethod
    def coef_to_str(coef: float):
        coef_int = int(coef)
        if coef - coef_int == 0.0:
            coef = coef_int
        return str(coef)

    def _check_standart_entry_sequence(self, left_tokens, right_tokens):
        degree_prev = -1
        for degree in left_tokens:
            if degree - degree_prev > 1:
                self.is_free_form = True
                return
            degree_prev = degree
        if right_tokens != {}:
            self.is_free_form = True
            return
