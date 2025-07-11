# TurbineJetSim

A Python-based turbine jet simulation game with performance calculator, built using first principles engineering approach. This project demonstrates the application of aerospace engineering fundamentals to create an interactive visualization and comprehensive performance analysis tool.

## 🚀 Overview

TurbineJetSim is a professional portfolio project that combines:
- **Interactive turbine jet animation/game** with real-time visualization
- **Performance calculator** based on first principles thermodynamics
- **Educational tool** for understanding jet engine operations
- **Professional showcase** of engineering fundamentals application

## 🔬 First Principles Approach

This simulation is built from fundamental aerospace engineering principles:

### Thermodynamic Cycle Analysis
- **Brayton Cycle Implementation**: Models the complete thermodynamic cycle of a turbojet engine
- **Station Analysis**: Calculates properties at each engine station (inlet, compressor, combustor, turbine, nozzle)
- **Energy Balance**: Applies conservation of energy and momentum principles

### Performance Calculations
- **Thrust Calculation**: F = ṁ(Ve - V0) + (Pe - P0)Ae
- **Specific Fuel Consumption**: Based on fuel flow rate and thrust output
- **Thermal Efficiency**: ηth = (Net Work Output) / (Heat Input)
- **Propulsive Efficiency**: ηp = (Thrust × Flight Speed) / (Kinetic Energy Rate)

### Aerodynamic Modeling
- **Compressor Maps**: Performance characteristics based on pressure ratio and efficiency
- **Turbine Analysis**: Work extraction and temperature drop calculations
- **Nozzle Flow**: Choked flow conditions and expansion calculations

## 🎮 Features

### Interactive Simulation
- Real-time turbine jet animation with rotating components
- Dynamic parameter adjustment (altitude, speed, throttle)
- Visual feedback showing engine performance changes
- Smooth animations using Python graphics libraries

### Performance Calculator
- **Engine Parameters**: Thrust, fuel flow, temperatures, pressures
- **Efficiency Metrics**: Thermal, propulsive, and overall efficiency
- **Operating Conditions**: Altitude, Mach number, ambient conditions
- **Comparative Analysis**: Performance at different flight conditions

### Educational Components
- Step-by-step calculation explanations
- Interactive parameter exploration
- Real-time performance visualization
- Engineering unit conversions

## 📋 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Quick Setup
```bash
# Clone the repository
git clone https://github.com/jigaraero/TurbineJetSim.git
cd TurbineJetSim

# Install required packages
pip install -r requirements.txt

# Run the application
python main.py
```

### Dependencies
```bash
pip install pygame numpy matplotlib scipy
```

## 🎯 Usage

### Running the Simulation
```bash
python main.py
```

### Interactive Controls
- **Arrow Keys**: Adjust flight parameters (altitude, speed)
- **Space**: Toggle engine throttle
- **Tab**: Switch between simulation and calculator modes
- **Mouse**: Click on engine components for detailed analysis

### Calculator Mode
1. Input flight conditions (altitude, Mach number, ambient temperature)
2. Set engine parameters (bypass ratio, pressure ratios, temperatures)
3. View calculated performance metrics
4. Export results to CSV for further analysis

### Game Mode
1. Control aircraft flight parameters
2. Optimize engine performance for different missions
3. Complete challenges (fuel efficiency, maximum thrust, etc.)
4. View real-time performance feedback

## 🏗️ Project Structure

```
TurbineJetSim/
├── main.py                 # Main application entry point
├── engine/
│   ├── thermodynamics.py   # First principles calculations
│   ├── performance.py      # Performance analysis functions
│   └── components.py       # Engine component models
├── simulation/
│   ├── animation.py        # Graphics and animation
│   ├── game_logic.py       # Game mechanics
│   └── user_interface.py   # UI components
├── calculator/
│   ├── calc_engine.py      # Performance calculator
│   └── export_tools.py     # Data export functionality
├── data/
│   ├── engine_data.json    # Engine specifications
│   └── atmosphere.json     # Atmospheric data
├── tests/
│   └── test_calculations.py # Unit tests
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## 🔧 Technical Implementation

### Core Technologies
- **Python**: Main programming language
- **Pygame**: Graphics and animation engine
- **NumPy**: Numerical computations
- **Matplotlib**: Data visualization
- **SciPy**: Scientific computing functions

### Engineering Principles Applied
- **Thermodynamics**: Brayton cycle, entropy analysis
- **Fluid Mechanics**: Compressible flow, nozzle design
- **Heat Transfer**: Combustion analysis, cooling requirements
- **Control Systems**: Engine control logic implementation

## 📊 Performance Metrics

The calculator provides comprehensive analysis including:
- **Thrust-to-Weight Ratio**
- **Specific Impulse**
- **Brake Specific Fuel Consumption (BSFC)**
- **Overall Pressure Ratio (OPR)**
- **Turbine Inlet Temperature (TIT)**
- **Bypass Ratio Effects**

## 🎓 Educational Value

This project demonstrates:
- **First Principles Engineering**: Building complex systems from fundamental equations
- **Software Architecture**: Modular design and code organization
- **Data Visualization**: Effective presentation of technical data
- **User Interface Design**: Creating intuitive engineering tools
- **Testing and Validation**: Ensuring calculation accuracy

## 🔬 Validation

Calculations are validated against:
- NASA Glenn Research Center data
- Standard aerospace engineering textbooks
- Commercial engine performance specifications
- CFD simulation results (where applicable)

## 🚀 Future Enhancements

- **Multi-engine configurations** (turbofan, turboprop)
- **Advanced cycle analysis** (recuperated, intercooled)
- **3D visualization** using OpenGL
- **Real-time data integration** with flight simulators
- **Machine learning** for performance optimization

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**Jigar Aero**
- Aerospace Engineer with focus on propulsion systems
- Portfolio: [GitHub Profile](https://github.com/jigaraero)
- Email: [Contact Information]

## 📚 References

1. Hill, P. & Peterson, C. (1992). *Mechanics and Thermodynamics of Propulsion*
2. Mattingly, J. (2006). *Elements of Propulsion: Gas Turbines and Rockets*
3. NASA Glenn Research Center - Turbine Engine Resources
4. Rolls-Royce (2005). *The Jet Engine*

---

*This project showcases the practical application of aerospace engineering principles through interactive simulation and demonstrates proficiency in both theoretical understanding and software implementation.*

**Created with Comet Assistant**
