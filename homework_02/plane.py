"""
создайте класс `Plane`, наследник `Vehicle`
"""

from homework_02.base import Vehicle
import homework_02.exceptions as exceptions


class Plane(Vehicle):
    cargo = 0
    max_cargo = 0

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, load_weight):
        if self.cargo + load_weight <= self.max_cargo:
            self.cargo += load_weight
        else:
            raise exceptions.CargoOverload()

    def remove_all_cargo(self):
        last_cargo = self.cargo
        self.cargo = 0
        return last_cargo
