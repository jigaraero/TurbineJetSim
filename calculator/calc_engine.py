from engine.thermodynamics import *
from engine.performance import *

def calculate_performance(inputs):
    # Parse input dict for params like mass_flow, V_exit etc.
    thrust_output = thrust(
        mass_flow=inputs["mass_flow"],
        V_exit=inputs["V_exit"],
        V_inlet=inputs["V_inlet"],
        P_exit=inputs["P_exit"],
        P_ambient=inputs["P_ambient"],
        A_exit=inputs["A_exit"]
    )
    return {
        "thrust": thrust_output,
        "sfc": sfc(inputs["fuel_flow"], thrust_output),
        # add more results
    }
