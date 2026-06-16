from datetime import datetime
from Enums.VehicleType import VehicleType
from common.ParkingSpot import ParkingSpot
from common.Level import Level

class Ticket():
    def __init__(self, v_type: VehicleType, parkingSpot: ParkingSpot, level: Level):
        self.time = datetime.now()
        self.vehicle = v_type
        self.parking_spot = parkingSpot
        self.level = level

    def get_parking_time(self):
        return self.time
    
    def get_vehicle(self) -> VehicleType:
        return self.vehicle
    
    def get_parking_spot(self):
        return self.parking_spot
    
    def get_level(self):
        return self.level