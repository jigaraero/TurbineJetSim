class Compressor:
    def __init__(self, pr, eta=0.85):
        self.pressure_ratio = pr
        self.efficiency = eta

    # Add method for isentropic work, outlet T, etc.

class Turbine:
    def __init__(self, eta=0.88):
        self.efficiency = eta

    # Methods for work extraction, outlet T

class Nozzle:
    def __init__(self, eta=0.98):
        self.efficiency = eta

    # Methods for expansion, velocity calculation
