from math import pi


class Spherical:

    def __init__(self, r):

        self.radius = r

    def changeR(self, Radius):

        self.radius = Radius

    def findVolume(self):
        self.volume = (4/3)*pi*(self.radius**3)

    def findArea(self):
        self.area = 4*pi*(self.radius**2)

    def __str__(self):
        self.findArea()
        self.findVolume()
        return ("Radius ={} Volumn = {} Area = {}".format(self.radius, self.volume, self.area))


r1, r2 = input("Enter R : ").split()
R1 = Spherical(int(r1))
print(type(R1))
print(dir(R1))
print(R1)
R1.changeR(int(r2))
print(R1)
