from abc import ABC, abstractmethod

class BaseService(ABC):
    @abstractmethod
    def __call__(self, *args, **kwargs):
        raise NotImplementedError
        
