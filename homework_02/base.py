from abc import ABC
import homework_02.exceptions as exceptions


class Vehicle(ABC):
    weight: int = 0
    started = False
    fuel: float = 0
    fuel_consumption: float = 0

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise exceptions.LowFuelError

    def move(self, distance):
        if self.fuel - distance * self.fuel_consumption >= 0:
            self.fuel -= distance * self.fuel_consumption
        else:
            raise exceptions.NotEnoughFuel
