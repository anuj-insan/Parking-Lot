from Enums.SpotStatus import SpotStatus
class ParkingSpot():
    def __init__(self, id):
        self.spot_id = id
        self.status = SpotStatus.FREE

    def get_spot_id(self):
        return self.spot_id
    
    def get_status(self):
        return self.status
    
    def park_vehicle(self):
        self.status = SpotStatus.OCCUPIED

    def unpark_vehicle(self):
        self.status = SpotStatus.FREE