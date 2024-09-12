import math

def getCylinderVolume(radius, height):
    volume = math.pi * (radius ** 2) * height
    return volume

x = getCylinderVolume(10, 12)
y = getCylinderVolume(2, 6)
print(round(x,4))
print(round(y,4))
print(int(y))

def getNumberOfSlices(radius, height, volumeofslice):
    volume = getCylinderVolume(radius, height)
    numberofslices = volume/volumeofslice
    return int(numberofslices)
numberofslice1 = getNumberOfSlices(10, 10, 100)
print(numberofslice1)