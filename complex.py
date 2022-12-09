class Complex():
    
    def __init__(self, real, imaginary):
        
        """Create a new complex z = a + ib"""

        self.real = real
        self.imaginary = imaginary
        
    def __str__(self) -> str:
        return "z = " + str(self.real) + " + i" + str(self.imaginary)
        
    def sum(self, complex):
        
        """Return a new Complex number who is the sum between two complex number"""
        
        return Complex(self.real + complex.real, self.imaginary + complex.imaginary)

    def sub(self, complex):
        
        """Return a new Complex number who is the substraction between two complex number"""
        
        return Complex(self.real - complex.real, self.imaginary - complex.imaginary)

    def product(self, complex):
        
        """Return a new Complex number who is the product between two complex number"""
        
        a,b,c,d = self.real, self.imaginary, complex.real, complex.imaginary
        return Complex((a*c - b*d), (a*d+b*c))