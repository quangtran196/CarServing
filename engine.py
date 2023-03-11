from abc import ABC, abstractmethod


class Engine(ABC):
    def __init__(self, last_service_mileage: int, current_mileage: int):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage
    
    @abstractmethod
    def needs_service(self) -> bool:
        pass

    
class CapuletEngine(Engine):
    def __init__(self, last_service_mileage: int, current_mileage: int):
        super().__init__(last_service_mileage, current_mileage)
        
    def needs_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage >= 30000

    
class WilloughbyEngine(Engine):
    def __init__(self, last_service_mileage: int, current_mileage: int):
        super().__init__(last_service_mileage, current_mileage)
        
    def needs_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage >= 60000

    
class SternmanEngine(ABC):
    def __init__(self, last_service_date, warning_light_is_on):
        super().__init__(last_service_date)
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self):
        if self.warning_light_is_on:
            return True
        else:
            return False