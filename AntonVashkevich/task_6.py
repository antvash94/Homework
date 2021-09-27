from functools import total_ordering


@total_ordering
class Money:

    RATES = {"USD": 1, "EUR": 0.85, "BYN": 2.5, "RUB": 71}

    def __init__(self, value, currency="USD"):
        self._value = value
        self._currency = currency

    @property
    def value(self):
        return self._value

    @property
    def currency(self):
        return self._currency

    @property
    def exchange(self):
        return self.value/self.RATES.get(self.currency)

    def __add__(self, other):
        value = (self.exchange+other.exchange)*self.RATES.get(self._currency)
        return Money(value, self.currency)

    def __radd__(self, other):
        if isinstance(other, (int, float)):
            return self
        return self.__add__(other)

    def __sub__(self, other):
        value = (self.exchange - other.exchange) * self.RATES.get(self._currency)
        return Money(value, self.currency)

    def __truediv__(self, other):
        return Money(self.value/other)

    def __mul__(self, other):
        return Money(self.value * other)
    __rmul__ = __mul__

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __repr__(self):
        return f"{self.value:.2f} {self.currency}"


x = Money(10, "BYN")
y = Money(11)
z = Money(12.34, "EUR")
print(z + 3.11 * x + y * 0.8)
lst = [Money(10,"BYN"), Money(11), Money(12.01, "RUB")]
s = sum(lst)
print(s)