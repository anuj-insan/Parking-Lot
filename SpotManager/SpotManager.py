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

    def get_free_spot(self) -> Optional[ParkingSpot]:
        with self.lock:
            return self.spot_lookup_strategy.select_free_spot(self.spots)
    
    def park(self, spot: ParkingSpot):
        with self.lock:
            spot.park_vehicle()

    def unpark(self, spot: ParkingSpot):
        with self.lock:
            spot.unpark_vehicle()