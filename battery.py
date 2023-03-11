from abc import ABC, abstractmethod


class Battery(ABC):
    def __init__(self, last_service_date: str, current_date: str):
        self.last_service_date = last_service_date
        self.current_date = current_date
        
    @abstractmethod
    def needs_service(self) -> bool:
        pass

    
class SpindlerBattery(Battery):
    def __init__(self, last_service_date: str, current_date: str):
        super().__init__(last_service_date, current_date)
        
    def needs_service(self) -> bool:
        return self.current_date - self.last_service_date >= 365*2

    
class NubbinBattery(Battery):
    def __init__(self, last_service_date: str, current_date: str):
        super().__init__(last_service_date, current_date)
        
    def needs_service(self) -> bool:
        return self.current_date - self.last_service_date >= 365*4