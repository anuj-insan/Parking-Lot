from Strategies.CostComputationStrategy.CostComputationStrategy import CostComputationStrategy
from datetime import datetime

class HourlyPricingStrategy(CostComputationStrategy):
    def __init__(self):
        super().__init__()

    def compute(self, time) -> float:
        dt = datetime.strptime(
            time,
            "%Y-%m-%d %H:%M:%S.%f"
        )
        diff = datetime.now() - dt
        hours = diff.total_seconds() / 3600

        return hours * self.default_amount 
        