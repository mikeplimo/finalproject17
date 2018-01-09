from math import sqrt

class Human():
    def __init__(self, x=100, y=25, z=30):
        self.health = x
        self.defence = y
        self.attack = z

    def increase_stat(self, x_increment=0, y_increment=1, z_increment=1):
        self.health += x_increment
        self.defence += y_increment
        self.attack += z_increment




