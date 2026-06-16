from common.ParkingSpot import ParkingSpot
from Strategies.ParkingSpotStrategy.ParkingSpotLookupStrategy import ParkingSpotLookupStrategy
from typing import List, Optional
from SpotManager.SpotManager import SpotManager

class FourWheelerSpotManager(SpotManager):
    def __init__(self, spots: List[ParkingSpot], strategy: ParkingSpotLookupStrategy):
        super().__init__(spots, strategy)