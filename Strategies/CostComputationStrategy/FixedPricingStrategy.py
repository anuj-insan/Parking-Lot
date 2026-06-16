from Strategies.CostComputationStrategy.CostComputationStrategy import CostComputationStrategy

class FixedPricingStrategy(CostComputationStrategy):
    def __init__(self):
        super().__init__()

    def compute(self, time) -> float:
        return self.default_amount 
        