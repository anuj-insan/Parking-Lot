from abc import ABC, abstractmethod
from common.ParkingSpot import ParkingSpot
from Strategies.ParkingSpotStrategy.ParkingSpotLookupStrategy import ParkingSpotLookupStrategy
from typing import List, Optional
from SpotManager.SpotManager import SpotManager

class TwoWheelerSpotManager(SpotManager):
    def __init__(self, spots: List[ParkingSpot], strategy: ParkingSpotLookupStrategy):
        super().__init__(spots, strategy)

    def get_free_spot(self) -> Optional[ParkingSpot]:
        return self.spot_lookup_strategy.select_free_spot(self.spots)
    
    def park(self, spot: ParkingSpot):
        spot.park_vehicle()

    def unpark(self, spot: ParkingSpot):
        spot.unpark_vehicle()