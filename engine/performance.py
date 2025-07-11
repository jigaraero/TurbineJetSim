def thrust(mass_flow, V_exit, V_inlet=0, P_exit=0, P_ambient=0, A_exit=1):
    # Momentum plus pressure thrust
    momentum = mass_flow * (V_exit - V_inlet)
    pressure = (P_exit - P_ambient) * A_exit
    return momentum + pressure

def sfc(fuel_flow, thrust):
    return fuel_flow / thrust

def thermal_efficiency(thrust, V_0, fuel_energy):
    return (thrust * V_0) / fuel_energy
