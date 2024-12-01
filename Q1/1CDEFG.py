#1CDEFG
class mat:
    def __init__(self, rows, cols, field="real", vectors=None):
        self.rows = rows
        self.cols = cols
        self.field = field
        self.data = self.build_matrix(vectors)

    def build_matrix(self, vectors):
        if vectors:
            if len(vectors) != self.cols or any(len(vec) != self.rows for vec in vectors):
                raise ValueError("Column vectors do not match matrix dimensions.")
            return [[vectors[j][i] for j in range(self.cols)] for i in range(self.rows)]
        else:
            matrix = []
            for i in range(self.rows):
                row = []
                for j in range(self.cols):
                    row.append(self.getting_the_value())
                matrix.append(row)
            return matrix

    def getting_the_value(self):
        if self.field == "real":
            while True:
                try:
                    return float(input("Enter a real number: "))
                except ValueError:
                    print("Invalid input. Please enter a real number.")
        elif self.field == "complex":
            while True:
                try:
                    real = float(input("Enter real part: "))
                    imag = float(input("Enter imaginary part: "))
                    return complex(real, imag)
                except ValueError:
                    print("Invalid input. Please enter valid numbers for the complex value.")

    def display(self):
        if not self.data:
            print("Matrix is empty.")
        else:
            print("Matrix contents:")
            for row in self.data:
                print(row)

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions do not match for addition.")
        return mat(self.rows, self.cols, self.field, [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)])

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Matrix multiplication not possible: Columns of first matrix must equal rows of second.")
        result = []
        for i in range(self.rows):
            row = []
            for j in range(other.cols):
                total = sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                row.append(total)
            result.append(row)
        return mat(self.rows, other.cols, self.field, result)

    def show_row(self, index):
        if 0 <= index < self.rows:
            return self.data[index]
        else:
            raise IndexError("Row index out of range.")

    def show_column(self, index):
        if 0 <= index < self.cols:
            return [self.data[i][index] for i in range(self.rows)]
        else:
            raise IndexError("Column index out of range.")

    def getting_transpose(self):
        return mat(self.cols, self.rows, self.field, [[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)])

    def conj(self):
        if self.field != "complex":
            raise ValueError("Conjugate is only applicable to complex matrices.")
        return mat(self.rows, self.cols, self.field, [[self.data[i][j].conjugate() for j in range(self.cols)] for i in range(self.rows)])

    def conj_transpose(self):
        return self.conj().getting_transpose()


# Example Usage
# Initialize a 2x2 real matrix with manual input
m1 = mat(2, 2, "real")
m1.display()

# Create a matrix using column vectors
m2 = mat(2, 2, "real", [[1, 2], [3, 4]])
m2.display()

# Perform matrix addition
m3 = m1 + m2
m3.display()

# Matrix multiplication
m4 = mat(2, 3, "real", [[1, 2], [3, 4], [5, 6]])
m5 = mat(3, 2, "real", [[7, 9, 11], [8, 10, 12]])
m6 = m4 * m5
m6.display()

# Transpose, Conjugate, and Conjugate-Transpose
m7 = mat(2, 2, "complex")
t = m7.getting_transpose()
t.display()
c = m7.conj()
c.display()
ct = m7.conj_transpose()
ct.display()
