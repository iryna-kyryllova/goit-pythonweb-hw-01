from abc import ABC, abstractmethod
import logging

logging.basicConfig(level=logging.INFO)


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self) -> None:
        pass


class Car(Vehicle):
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model}: Двигун запущено")


class Motorcycle(Vehicle):
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model}: Мотор заведено")


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Vehicle:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, f"{model} (US Spec)")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, f"{model} (US Spec)")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, f"{model} (EU Spec)")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, f"{model} (EU Spec)")


# Використання
us_factory = USVehicleFactory()
eu_factory = EUVehicleFactory()

# Створення транспортних засобів для США
vehicle1 = us_factory.create_car("Ford", "Mustang")
vehicle1.start_engine()

vehicle2 = us_factory.create_motorcycle("Harley-Davidson", "Sportster")
vehicle2.start_engine()

# Створення транспортних засобів для ЄС
vehicle3 = eu_factory.create_car("Volkswagen", "Golf")
vehicle3.start_engine()

vehicle4 = eu_factory.create_motorcycle("BMW", "R1250")
vehicle4.start_engine()
