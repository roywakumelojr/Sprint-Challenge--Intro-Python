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

### This is the primary base for the classes ###


class Vehicle(object):
    pass


##### [Vehicle] #####
# The base class for Ground Vehicle is Vehicle
class GroundVehicle(Vehicle):
    pass


# The base class for Fright Vehicle is Vehicle
class FlightVehicle(Vehicle):
    pass


##### [GroundVehicle] #####
# The base class for the Car is GroundVehicle
class Car(GroundVehicle):
    pass


# The base class for the Motorcycle is GroundVehicle
class Motorcycle(GroundVehicle):
    pass


##### [FlightVehicle] #####
# The base class for the Airplane is FrightVehicle
class Airplane(FlightVehicle):
    pass


# The base class for the Starship is FrightVehicle
class Starship(FlightVehicle):
    pass
