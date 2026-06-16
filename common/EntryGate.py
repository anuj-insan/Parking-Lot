from common.Building import Building
from common.Vehicle import Vehicle

class EntryGate():
    def __init__(self, building: Building):
        self.building = building

    def enter_vehicle(self, vehicle: Vehicle):
        return self.building.allocate(vehicle.get_vehicle_type())