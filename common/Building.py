from typing import List, Optional
from common.Level import Level
from Enums.VehicleType import VehicleType
from common.Ticket import Ticket
from common.ParkingSpot import ParkingSpot
class Building():
    def __init__(self, levels: List[Level]):
        self.levels = levels

    def allocate(self, v_type: VehicleType) -> Ticket:
        for level in self.levels:
            spot: Optional[ParkingSpot] = level.get_free_spot(v_type)

            if not spot:
                continue

            level.park(v_type, spot)
            ticket = Ticket(v_type, spot, level)
            print(f'Parking allocated at {level.level_id} level at {spot.get_spot_id} spot...!')
            
            return ticket
        
        raise Exception("No vacant Parking Spot Found")
    
    def release(self, ticket: Ticket):
        ticket.get_level().unpark(ticket.get_vehicle(), ticket.get_parking_spot())
                

