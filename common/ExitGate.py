from common.Ticket import Ticket
from common.CostComputation import CostComputation
from common.Building import Building
from Payment.Payment import Payment

class ExitGate():
    def __init__(self, cost_computer: CostComputation, building: Building):
        self.cost_computer = cost_computer
        self.building = building

    def compute_cost(self, ticket: Ticket) -> float:
        return self.cost_computer.compute(ticket.get_parking_time())

    def exit(self, ticket: Ticket, payment: Payment) -> None:
        amount = self.compute_cost(ticket)
        payment_status = payment.pay(amount)

        if payment_status:
            self.building.release(ticket)
            print("Exit from the parking successfully")

        