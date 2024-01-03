from abc import ABC, abstractmethod

class BaseService(ABC):
    @abstractmethod
    def subscribe(self, *args, **kwargs):
        raise NotImplementedError
    
    @abstractmethod
    def unsubscribe(self, *args, **kwargs):
        raise NotImplementedError
    