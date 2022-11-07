import re

class Parser:
  def __init__(self, polynom):
    self._raw_polynom = polynom
    self._polynom = polynom
    self._set_power_and_coef()

  def _set_power_and_coef(self):
    try:
      raw_left, raw_right = self._raw_polynom.split('=')
    except Exception as e:
      raise BaseException(f'ERROR: equation: "{self._raw_polynom}" should has "="')
    left_token = self._get_tokens(raw_left)
    right_tokens = self._get_tokens(raw_right)
    left_token.update({key: left_token[key] - right_tokens[key] for key in right_tokens if key in left_token})
    left_token.update({key: -right_tokens[key] for key in right_tokens if key not in left_token})

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
