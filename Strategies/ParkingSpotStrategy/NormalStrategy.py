from Strategies.ParkingSpotStrategy.ParkingSpotLookupStrategy import ParkingSpotLookupStrategy
from Enums.SpotStatus import SpotStatus
from common.ParkingSpot import ParkingSpot
from typing import List, Optional

class NormalStrategy(ParkingSpotLookupStrategy):
    def select_free_spot(self, spots: List[ParkingSpot]) -> Optional[ParkingSpot]:
        for spot in spots:
            if spot.get_status() == SpotStatus.FREE:
                return spot
            
        return None