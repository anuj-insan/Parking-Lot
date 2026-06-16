from datetime import datetime
from abc import ABC, abstractmethod

class CostComputationStrategy(ABC):
    def __init__(self):
        self.default_amount = 100

    @abstractmethod
    def compute(self, time: datetime) -> float:
        pass