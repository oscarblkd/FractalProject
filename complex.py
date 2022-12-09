class Complex():


    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def sum(self, unComplexe):
        return self.real + unComplexe.real, self.imaginary + unComplexe.imaginary

    def sub(self, unComplexe):
        return self.real - unComplexe.real, self.imaginary - unComplexe.imaginary

    def product(self, unComplexe):
        a,b,c,d = self.real, self.imaginary, unComplexe.real, unComplexe.imaginary
        return (a*c - b*d), (a*d+b*c)

    def divide(self, unComplexe):
        return


   












#-------------------------------------USINE--------------------------------------------------------------------








