from abc import ABC, abstractmethod


class OutComingStructure(ABC):

    @abstractmethod
    def send(self, alert: dict):
        pass
