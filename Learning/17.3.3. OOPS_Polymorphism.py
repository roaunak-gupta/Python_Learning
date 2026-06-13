class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(f"{self.real} i + {self.img} j")

    def add(self, num2):  # This is traditional method for adding two numbers
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)

    def __add__(self, num2):  # This is addition of Dunder Funtions for adding two
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)


num1 = Complex(2, 5)
num1.showNumber()

num2 = Complex(3, 7)
num2.showNumber()

# Traditional Method for Adding
num3 = num1.add(num2)
num3.showNumber()

# Operator Overloading
num4 = num1 + num2 # Here we directly add two complex numbers using with dunder funtions
num4.showNumber()
