""" A python class to represent vectors """
import math

class Vector(object):
    def __init__(self, coordinates, tolerance=1e-10):
        self.coordinates = tuple(coordinates)
        self.dimension = len(coordinates)
        self.tolerance = tolerance

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
            selfMag = self.getMagnitude()
            otherMag = other.getMagnitude()
            allOfProducts = [x*y for x,y in zip(self.coordinates,  other.coordinates)]
            return sum(allOfProducts)

        else:
            newCoords = []
            for i in range(self.dimension):
                newCoords.append(self.coordinates[i] * other)
            return Vector(newCoords)

    def getMagnitude(self):
        """ Returns the magnitude (length) of the given Vector """
        coordinatesSquared = [x**2 for x in self.coordinates]
        return math.sqrt(sum(coordinatesSquared))

    def getNormalization(self):
        """ Returns the unit vector representation of the given Vector """
        selfMag = self.getMagnitude()
        try:
            return self * ((1/selfMag))

        except ZeroDivisionError:
            raise exception("Cannot normalize the zero vector")

    def isZero(self):
        return self.getMagnitude() < self.tolerance

    def angleDiff(self, other, units="rad"):
        """ Returns the angle between two vectors """
        rads = math.acos((self * other) / (self.getMagnitude() * other.getMagnitude()))
        if units == "rad":
            return rads
        else:
            return math.degrees(rads)

    def orthogonalTo(self, other):
        """ Returns true of the vectors are orthogonal to each other """
        return abs(self * other) < self.tolerance

    def parallelTo(self, other):
        """ Returns true if the vectors are parallel to each other """
        return (self.isZero() or other.isZero() or 
                self.angleDiff(other, "deg") == 0 or
                self.angleDiff(other, "deg") == 180)

if __name__ == "__main__":
    myVec1 = Vector([1,2,3])
    myVec2 = Vector([-2,0,5])
    print("Vec1 {}".format(myVec1))
    print("Vec2 {}".format(myVec2))
    print("Vec1 + Vec2  = {}".format(myVec1 + myVec2))
    print("Vec1 - Vec2  = {}".format(myVec1 - myVec2))
    print("Vec1 * 2  = {}".format(myVec1 * 2))
    print("Vec1 * Vec2  = {}".format(myVec1 * myVec2))
    print("Vec1 Magnitude = {}".format(myVec1.getMagnitude()))
    print("Vec2 Normalized = {}".format(myVec2.getNormalization()))
