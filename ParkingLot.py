from common.Building import Building
from common.EntryGate import EntryGate
from common.ExitGate import ExitGate
from common.Ticket import Ticket
from common.Vehicle import Vehicle
from Payment.Payment import Payment

class ParkingLot():
    def __init__(self, building: Building, entry_gate: EntryGate, exit_gate: ExitGate):
        self.building = building
        self.entry_gate = entry_gate
        self.exit_gate = exit_gate

    def vehicle_arrives(self, vehicle: Vehicle) -> Ticket:
        return self.entry_gate.enter_vehicle(vehicle)
    
    def vehicle_exits(self, ticket: Ticket, payment: Payment) -> None:
        self.exit_gate.exit(ticket, payment)