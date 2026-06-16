from common.Vehicle import Vehicle
from Enums.VehicleType import VehicleType
from common.ParkingSpot import ParkingSpot
from Strategies.ParkingSpotStrategy.NormalStrategy import NormalStrategy 
from SpotManager.TwoWheelerSpotManager import TwoWheelerSpotManager
from SpotManager.FourWheelerSpotManager import FourWheelerSpotManager
from common.Level import Level
from common.Building import Building
from common.EntryGate import EntryGate
from common.ExitGate import ExitGate
from Strategies.CostComputationStrategy.FixedPricingStrategy import FixedPricingStrategy
from Strategies.CostComputationStrategy.HourlyPricingStrategy import HourlyPricingStrategy
from common.CostComputation import CostComputation
from ParkingLot import ParkingLot
from Payment.UpiPayment import UpiPayment
def create_parking_lot():
    two_wheeler_spots = [ParkingSpot(i) for i in range(0, 6)]
    four_wheeler_spots = [ParkingSpot(i) for i in range(6, 11)]

    normal_parking_strategy = NormalStrategy()

    two_wheeler_spot_manager = TwoWheelerSpotManager(two_wheeler_spots, normal_parking_strategy)
    four_wheeler_spot_manager = FourWheelerSpotManager(four_wheeler_spots, normal_parking_strategy)

    parking_levels = []
    
    for i in range(0, 6):
        level = Level(i, managers = {
            VehicleType.TWO_WHEELER: two_wheeler_spot_manager,
            VehicleType.FOUR_WHEELER: four_wheeler_spot_manager
        })

        parking_levels.append(level)

    building = Building(levels = parking_levels)

    fixed_pricing_strategy = FixedPricingStrategy()
    hourly_pricing_strategy = HourlyPricingStrategy()

    cost_computator = CostComputation(fixed_pricing_strategy)

    entry_gate = EntryGate(building)
    exit_gate = ExitGate(cost_computator, building)

    parking_lot = ParkingLot(building, entry_gate, exit_gate)

    return parking_lot


if __name__ == "__main__":
    parking_lot = create_parking_lot()
    vehicle = Vehicle(VehicleType.TWO_WHEELER, "HR08J2004")

    ticket = parking_lot.vehicle_arrives(vehicle)
    print("ticket", ticket)
    payment_strat = UpiPayment()
    parking_lot.vehicle_exits(ticket, payment_strat)
    
    