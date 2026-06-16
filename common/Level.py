from typing import Dict, Optional
from Enums.VehicleType import VehicleType
from SpotManager.SpotManager import SpotManager
from common.ParkingSpot import ParkingSpot

class Level():
    def __init__(self, level_id: int, managers: Dict[VehicleType, SpotManager]):
        self.level_id = level_id
        self.managers = managers

    def get_free_spot(self, v_type: VehicleType) -> Optional[ParkingSpot]:
        s_manager = self.managers[v_type]

        if s_manager:
            return s_manager.get_free_spot()
        
        raise Exception("No spot manager found")
    
    def park(self, v_type: VehicleType, spot: ParkingSpot):
        s_manager = self.managers[v_type]

        if s_manager:
            return s_manager.park(spot)
        
        raise Exception("No spot manager found")

    def unpark(self, v_type: VehicleType, spot: ParkingSpot):
        s_manager = self.managers[v_type]

        if s_manager:
            return s_manager.unpark(spot)
        
        raise Exception("No spot manager found")
        