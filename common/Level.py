from typing import Dict, Optional
from common.Vehicle import Vehicle
from SpotManager.SpotManager import SpotManager
from common.ParkingSpot import ParkingSpot

class Level():
    def __init__(self, level_id: int, managers: Dict[Vehicle, SpotManager]):
        self.level_id = level_id
        self.managers = managers

    def get_free_spot(self, v_type: Vehicle) -> Optional[ParkingSpot]:
        s_manager = self.managers[v_type]

        if s_manager:
            return s_manager.get_free_spot()
        
        raise Exception("No spot manager found")
    
    def park(self, v_type: Vehicle, spot: ParkingSpot):
        s_manager = self.managers[v_type]

        if s_manager:
            return s_manager.park()
        
        raise Exception("No spot manager found")

    def unpark(self, v_type: Vehicle, spot: ParkingSpot):
        s_manager = self.managers[v_type]

        if s_manager:
            return s_manager.unpark()
        
        raise Exception("No spot manager found")
        