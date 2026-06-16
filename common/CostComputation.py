from Strategies.CostComputationStrategy.CostComputationStrategy import CostComputationStrategy

class CostComputation():
    def __init__(self, comp_strategy: CostComputationStrategy):
        self.comp_strategy = comp_strategy

    def compute(self, time) -> float:
        return self.comp_strategy.compute(time)