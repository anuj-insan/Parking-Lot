from abc import ABC, abstractmethod
from common.ParkingSpot import ParkingSpot
from Strategies.ParkingSpotStrategy.ParkingSpotLookupStrategy import ParkingSpotLookupStrategy
from typing import List, Optional
import threading

class SpotManager(ABC):
    def __init__(self, spots: List[ParkingSpot], strategy: ParkingSpotLookupStrategy):
        self.spots = spots
        self.spot_lookup_strategy = strategy
        self.lock = threading.RLock()

    @abstractmethod
    def get_free_spot(self) -> Optional[ParkingSpot]:
        pass
    
    @abstractmethod
    def park(self, spot: ParkingSpot):
        pass

    @abstractmethod
    def unpark(self, spot: ParkingSpot):
        pass