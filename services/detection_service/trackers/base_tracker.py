from abc import ABC
from abc import abstractmethod


class BaseTracker(ABC):

    @abstractmethod
    def update(self, detections):
        pass