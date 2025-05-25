from math import gcd


class Rational:
    def __init__(self, numerator=0, denominator=1):
        if isinstance(numerator, Rational):
            self.n = numerator.n
            self.d = numerator.d
            return

        if isinstance(numerator, str):
            if '/' in numerator:
                parts = numerator.split('/')
                numerator = int(parts[0])
                denominator = int(parts[1])
            else:
                numerator = int(numerator)
