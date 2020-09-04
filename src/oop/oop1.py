# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# - Base Class
class Vehicle:
    pass
# - from Vehicle
class GroundVehicle(Vehicle):
    pass
# - from GroundVehicle
class Car(GroundVehicle):
    pass
# - from GroundVehicle
class Motorcycle(GroundVehicle):
    pass
# - from Vehicle
class FlightVehicle(Vehicle):
    pass
# - from FlightVehicle
class Airplane(FlightVehicle):
    pass
# - from FlightVehicle
class Starship(FlightVehicle):
    pass