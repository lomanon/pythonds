def gcd(m,n):
    while m%n !=0:
        old_m = m
        old_n = n
        m = old_n
        n = old_m%old_n
    return n

class Fraction:
    # the methods go here
    def __init__(self, top, bottom):
        common = gcd(top, bottom)
        self.num = top/common
        self.den = bottom/common

    def show(self):
        print("{}/{}".format(self.num, self.den))

    def __str__(self):
        return "{}/{}".format(self.num, self.den)

    def __add__(self, f2):
        new_num = self.num * f2.den + self.den * f2.num
        new_dem = self.den * f2.den
        return Fraction(new_num, new_dem)

    def __eq__(self, other):
        first_num = self.num * other.den
        second_num = self.den * other.num
        return second_num == first_num

    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        return Fraction(new_num,new_den)

    def __truediv__(self, other):
        return Fraction(self.num * other.den, self.den * other.num)

    def __sub__(self, other):
        new_num = self.num * other.den - self.den * other.num
        new_dem = self.den * other.den
        return Fraction(new_num, new_dem)

    def __le__(self, other):
        return self.num/self.den <= other.num/other.den

fract_1 = Fraction(1,2)
fract_2 = Fraction(3,6)

print(fract_1 <     fract_2)
print(Fraction(1,2) == Fraction(3,6))