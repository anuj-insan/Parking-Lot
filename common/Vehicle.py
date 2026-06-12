from Enums.VehicleType import VehicleType

class Vehicle():
    def __init__(self, v_type: VehicleType, v_number: str):
        self.type = v_type
        self.number = v_number

    def get_vehicle_type(self):
        return self.type

    def get_vehicle_number(self):
        return self.number
        