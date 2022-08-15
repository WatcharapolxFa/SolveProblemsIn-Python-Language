class Rational:
    def __init__(self, a=None, b=None):
        if a == None and b == None:
            self.a = 1
            self.b = 1
        else:
            self.a = a
            self.b = b

    def __str__(self):
        if self.a == self.b == 1:
            return "1"
        else:
            return "{}/{}".format(self.a, self.b)

    def __lt__(self, other):
        return self.a / self.b < other.a / other .b

    def __gt__(self, other):
        return self.a / self.b > other.a / other .b

    def __ge__(self, other):
        return self.a / self.b <= other.a / other .b

    def __eq__(self, other):
        return self.a / self.b == other.a / other .b

    def __ne__(self, other):
        return self.a / self.b != other.a / other .b

    def __add__(self, other):
        sum = self.a+other.a
        num = self.b+other.b
        return "{}/{}".format(sum, num)

    def __sub__(self, other):
        sum = self.a-other.a
        num = self.b-other.b
        return "{}/{}".format(sum, num)

    def __mul__(self, other):
        sum = self.a*other.a
        num = self.b*other.b
        return "{}/{}".format(sum, num)

    def __truediv__(self, other):
        sum = self.a+other.a
        num = self.b+other.b
        return "{}/{}".format(sum, num)

    def __floordiv__(self, other):
        sum = self.a+other.a
        num = self.b+other.b
        return "{}/{}".format(sum, num)


str_input = input("Enter n1 d1 n2 d2 : ")
n1, d1, n2, d2 = [int(e) for e in str_input.split()]
A = Rational(n1, d1)     # A = n1/d1
B = Rational(n2, d2)     # B = n2/d2
C = Rational()          # C = 1/1
print("A=", A, "B=", B)        # method __str__
print("A < B ==> ", A < B)     # method __lt__
print("A > B ==> ", A > B)     # method __gt__
print("A <= B ==> ", A <= B)   # method __ge__
print("A >= B ==> ", A >= B)   # method __ge__
print("A == B ==> ", A == B)   # method __eq__
print("A != B ==> ", A != B)   # method __ne__
print("A + B ==> ", A+B)     # method __add__
print("A - B ==> ", A-B)     # method __sub__
print("A * B ==> ", A*B)     # method __mul__
print("A / B ==> ", A/B)     # method __truediv__
print("A // B ==> ", A//B)     # method __floordiv__
print("A + C ==> ", A+C)
