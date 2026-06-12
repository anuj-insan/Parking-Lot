from abc import ABC, abstractmethod
from common.ParkingSpot import ParkingSpot
from typing import List

class ParkingSpotLookupStrategy(ABC):

    @abstractmethod
    def select_free_spot(self, spots: List[ParkingSpot]) -> ParkingSpot:
        pass