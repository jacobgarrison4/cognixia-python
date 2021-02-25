class Car():

    wheels = 4
    doors = True

    def __init__(self, color, make, year, HP):     #Dunder method - double underscore: works bts in python
        #attributes
        self.color = color
        self.make = make
        self.year = year
        self.HP = HP
    
    #methods
    def start_car(self):
        print("Vroom")

    def paint_car(self, new_color):
        self.color = new_color
        print("Painted car", new_color)

    #Dunder methods
    def __gt__(self, other):
        return self.HP > other.HP

    def __str__(self):
        return self.color + " " + self.make
    
my_car = Car("White", "Aston Martin DB11", 2021, 630)
my_car.paint_car("Black")
my_car.start_car()
print(my_car)

your_car = Car("green", "Aventador", 2021, 580)
print(my_car > your_car)























