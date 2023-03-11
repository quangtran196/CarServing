from car import Car
from engine import CapuletEngine, WilloughbyEngine, SternmanEngine
from battery import SpindlerBattery, NubbinBattery
from datetime import date


class CarFactory:
    def create_calliope(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        return Car(engine, battery)

    def create_glissade(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        return Car(engine, battery)

    def create_palindrome(self, current_date: date, last_service_date: date, warning_light_on: bool) -> Car:
        engine = SternmanEngine()
        battery = NubbinBattery(current_date, last_service_date)
        car = Car(engine, battery)
        if warning_light_on:
            # Do something specific for cars with warning lights on
            pass
        return car

    def create_rorschach(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        return Car(engine, battery)

    def create_thovex(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        return Car(engine, battery)
    
