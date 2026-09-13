class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    def show(self):
        print(self.real, "i +" , self.img, "j")
    def add(self, num2):
        newreal = self.real + num2.real
        newimg = self.img + num2.img
        return Complex(newreal, newimg)
num1 = Complex(2, 6)
num1.show()
num2 = Complex(6, 8)
num2.show()
num3 = num1.add(num2)
num3.show()

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    def show(self):
        print(self.real, "i +", self.img, "j")
    def __add__(self, num2):
        newreal = self.real + num2.real
        newimg = self.img + num2.img
        return Complex(newreal, newimg)
num1 = Complex(2, 6)
num1.show()
num2 = Complex(6, 8)
num2.show()
num3 = num1 + num2
num3.show()