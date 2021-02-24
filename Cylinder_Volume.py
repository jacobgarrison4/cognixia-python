#RADIUS = 4
#HEIGHT = 10
PI = 3.14159265358979323846

def areaofcircle(radius):
    c_area = (PI * radius ** 2)
    return c_area

def volume(base, height):
    print(base * height)
    return None

volume(areaofcircle(4), 10)