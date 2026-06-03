from abc import ABC
from abc import abstractmethod


class BaseDetector(ABC):

    @abstractmethod
    def detect(self, frame):
        pass