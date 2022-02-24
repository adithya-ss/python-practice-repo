# Lightweight object type.
from collections import namedtuple
from turtle import clear
from unicodedata import name

Vehicle = namedtuple('Vehicle', 'SportsCar')
vh = Vehicle('Ferrari')
print(vh)
print(vh.SportsCar)
print("")

Desserts = namedtuple('Desserts', 'IceCream, Brownie')
ds = Desserts('Butterscotch', 'Chocolate')
print(ds)
print(ds.IceCream)
print(ds.Brownie)