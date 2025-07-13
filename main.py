# main.py - Main application entry point
# This script initializes the application, sets up Pygame, and handles mode switching between simulation and calculator.

import pygame
import sys
from simulation.animation import Animation
from simulation.game_logic import GameLogic
from simulation.user_interface import UserInterface
from calculator.calc_engine import CalcEngine
from engine.thermodynamics import Thermodynamics
from engine.performance import Performance
from engine.components import Compressor, Combustor, Turbine, Nozzle

# Constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60

class MainApp:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("TurbineJetSim - Jet Engine Simulation")
        self.clock = pygame.time.Clock()
        
        # Initialize modules
        self.thermo = Thermodynamics()
        self.perf = Performance()
        self.compressor = Compressor()
        self.combustor = Combustor()
        self.turbine = Turbine()
        self.nozzle = Nozzle()
        
        self.animation = Animation(self.screen)
        self.game_logic = GameLogic()
        self.ui = UserInterface(self.screen)
        self.calc_engine = CalcEngine()
        
        # Game state
        self.mode = "simulation"  # or "calculator"
        self.running = True
        self.params = {
            "altitude": 0,
            "mach": 0.0,
            "throttle": 1.0
        }

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    self.mode = "calculator" if self.mode == "simulation" else "simulation"
                self.game_logic.handle_key(event, self.params)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.ui.handle_click(event.pos, self.params)
    
    def update(self):
        # Calculate performance based on params
        thermo_data = self.thermo.calculate(self.params)
        perf_data = self.perf.calculate(thermo_data, self.params)
        self.game_logic.update(perf_data)
        
        if self.mode == "simulation":
            self.animation.update(perf_data)
        else:
            self.calc_engine.update(self.params, perf_data)
    
    def draw(self):
        self.screen.fill((0, 0, 0))  # Black background
        
        if self.mode == "simulation":
            self.animation.draw()
            self.ui.draw_simulation_overlay(self.params)
        else:
            self.ui.draw_calculator(self.calc_engine.results)
        
        pygame.display.flip()

if __name__ == "__main__":
    app = MainApp()
    app.run()
    pygame.quit()
    sys.exit()
