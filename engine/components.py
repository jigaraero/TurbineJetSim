# engine/components.py - Engine component models
# Defines classes for each engine component.

class Compressor:
    def __init__(self):
        self.pressure_ratio = 10
        self.efficiency = 0.85

class Combustor:
    def __init__(self):
        self.max_temp = 1400  # K
        self.efficiency = 0.98

class Turbine:
    def __init__(self):
        self.efficiency = 0.88

class Nozzle:
    def __init__(self):
        self.efficiency = 0.95
