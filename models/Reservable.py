from abc import ABC,abstractmethod
class Reservable (ABC):
    
    @abstractmethod
    def reserve(self):#حجز الكتاب مثلا (قابل للحجز)
        pass
        