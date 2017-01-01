""" A python class to represent vectors """
import math
import operator

class Vector(object):
    def __init__(self, coordinates):
        self.coordinates = tuple(coordinates)
        self.dimension = len(coordinates)

    def __str__(self):
        return "{}".format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __add__(self, v):
        if self.dimension != v.dimension:
            raise ValueError("Vector dimensions must be the same")
        newCoords = []
        for i in range(self.dimension):
            newCoords.append(self.coordinates[i] + v.coordinates[i])
        return Vector(newCoords)

    def __sub__(self, v):
        if self.dimension != v.dimension:
            raise ValueError("Vector dimensions must be the same")
        newCoords = []
        for i in range(self.dimension):
            newCoords.append(self.coordinates[i] - v.coordinates[i])
        return Vector(newCoords)

    def __mul__(self, other):
        if type(other) is Vector:
            theta = math.acos(operator.mul(self.getDirection(), other.getDirection()))
            return operator.mul(self.getMagnitude(), other.getMagnitude(), math.cos(theta))
        else:
            newCoords = []
            for i in range(self.dimension):
                newCoords.append(operator.mul(self.coordinates[i], other))
            return Vector(newCoords)

    def getMagnitude(self):
        coordinatesSquared = [x**2 for x in self.coordinates]
        return math.sqrt(sum(coordinatesSquared))

    def getDirection(self):
        try:
            return self * ((1/self.getMagnitude()))

        except ZeroDivisionError:
            raise exception("Cannot normalize the zero vector")

if __name__ == "__main__":
    myVec1 = Vector([1,2,3])
    myVec2 = Vector([4,5,6])
    print("Vec1 {}".format(myVec1))
    print("Vec2 {}".format(myVec2))
    print("Vec1 + Vec2  = {}".format(myVec1 + myVec2))
    print("Vec1 - Vec2  = {}".format(myVec1 - myVec2))
    print("Vec1 * 2  = {}".format(myVec1 * 2))
    print("Vec1 Magnitude = {}".format(myVec1.getMagnitude()))
    print("Vec2 Magnitude = {}".format(myVec2.getMagnitude()))
