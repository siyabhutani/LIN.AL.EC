#1B
class vec:
    def __init__(self, field, length):
        if field not in [float, complex]:
            raise ValueError("Field must be float or complex")
        if not isinstance(length, int) or length <= 0:
            raise ValueError("Length must be a positive integer")
        self.field_type = field
        self.vector_size = length
        self.vals = [self.field_type(input(f"Enter value {i + 1}: ")) for i in range(self.vector_size)]

    def __str__(self):
        return "Vector: " + " ".join(str(x) for x in self.vals)
# Example: Initialize a vector with real numbers and length 3
a = vec(float, 3)
print(a)

# Example: Initialize a vector with complex numbers and length 2
b = vec(complex, 2)
print(b)
