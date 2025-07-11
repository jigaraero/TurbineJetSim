import numpy as np

R = 287.058  # J/kg/K for air
gamma = 1.4

def isentropic_temperature_ratio(Mach, gamma=1.4):
    return 1 + 0.5 * (gamma - 1) * Mach**2

def stagnation_temperature(T_static, Mach, gamma=1.4):
    return T_static * isentropic_temperature_ratio(Mach, gamma)

def stagnation_pressure(p_static, Mach, gamma=1.4):
    return p_static * isentropic_temperature_ratio(Mach, gamma)**(gamma/(gamma-1))

def ideal_gas_density(P, T, R=R):
    return P / (R * T)
