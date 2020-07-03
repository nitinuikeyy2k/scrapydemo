from abc import ABC, abstractmethod

class Store(ABC):

    @abstractmethod
    def create_directory(self, path):
        pass

    @abstractmethod
    def get_path(self):
        pass
    
    @abstractmethod
    def is_path_exist(self, path):
        pass

