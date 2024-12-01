#1A
class CmplxNo:
    def __init__(self, r_part, i_part):
        self.real = r_part
        self.imag = i_part

    def __add__(self, other):
        r_sum = self.real + other.real
        i_sum = self.imag + other.imag
        return CmplxNo(r_sum, i_sum)

    def __mul__(self, other):
        r_prod = self.real * other.real - self.imag * other.imag
        i_prod = self.real * other.imag + self.imag * other.real
        return CmplxNo(r_prod, i_prod)

    def __truediv__(self, other):
        if other.real == 0 and other.imag == 0:
            raise ValueError("Cant divideby zero")
        denom = other.real ** 2 + other.imag ** 2
        r_div = (self.real * other.real + self.imag * other.imag) / denom
        i_div = (self.imag * other.real - self.real * other.imag) / denom
        return CmplxNo(r_div, i_div)

    def abs_value(self):
        return (self.real ** 2 + self.imag ** 2) ** 0.5

    def conjugate(self):
        return CmplxNo(self.real, -self.imag)

    def __str__(self):
        if self.imag < 0:
            return f"{self.real} - {-self.imag}i"
        return f"{self.real} + {self.imag}i"


# Example Usage
a = CmplxNo(3, 4)
b = CmplxNo(1, -2)

# Operations
sum_result = a + b
prod_result = a * b
div_result = a / b
abs_a = a.abs_value()
conj_b = b.conjugate()

# Outputs
print("Addition:", sum_result)
print("Multiplication:", prod_result)
print("Division:", div_result)
print("Absolute Value of a:", abs_a)
print("Conjugate of b:", conj_b)
