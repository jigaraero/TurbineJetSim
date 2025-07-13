# simulation/user_interface.py - UI components
# Draws overlays, buttons, sliders for interactive control, and now a dashboard with gauges.

import pygame
import math

class UserInterface:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("Arial", 24)
        self.small_font = pygame.font.SysFont("Arial", 18)
        self.buttons = []  # List of clickable areas
    
    def draw_simulation_overlay(self, params):
        # Display params (unchanged)
        text = self.font.render(f"Altitude: {params['altitude']} m", True, (255, 255, 255))
        self.screen.blit(text, (10, 10))
        text = self.font.render(f"Mach: {params['mach']:.1f}", True, (255, 255, 255))
        self.screen.blit(text, (10, 40))
        text = self.font.render(f"Throttle: {params['throttle']:.1f}", True, (255, 255, 255))
        self.screen.blit(text, (10, 70))
    
    def draw_calculator(self, results):
        # Display calculation results (unchanged)
        y = 10
        for key, value in results.items():
            text = self.font.render(f"{key.capitalize()}: {value:.2f}", True, (255, 255, 255))
            self.screen.blit(text, (10, y))
            y += 30
    
    def draw_dashboard(self, state):
        """
        Draw a dashboard with gauges for key performance metrics.
        :param state: dict with keys like 'thrust', 'sfc', 'thermal_eff' (from perf_data)
        """
        # Dashboard background panel
        pygame.draw.rect(self.screen, (50, 50, 50), (200, 500, 880, 200), border_radius=10)
        
        # Gauge positions and configs
        gauges = [
            {"label": "Thrust (N)", "value": state.get("thrust", 0), "min_val": 0, "max_val": 50000, "pos": (300, 600), "radius": 80},
            {"label": "SFC (kg/N·s)", "value": state.get("sfc", 0), "min_val": 0, "max_val": 0.0001, "pos": (600, 600), "radius": 80},
            {"label": "Thermal Eff (%)", "value": state.get("thermal_eff", 0) * 100, "min_val": 0, "max_val": 100, "pos": (900, 600), "radius": 80},
        ]
        
        for gauge in gauges:
            self._draw_gauge(
                pos=gauge["pos"],
                radius=gauge["radius"],
                value=gauge["value"],
                min_val=gauge["min_val"],
                max_val=gauge["max_val"],
                label=gauge["label"]
            )
    
    def _draw_gauge(self, pos, radius, value, min_val, max_val, label):
        """Helper to draw a single semi-circular gauge with needle."""
        # Clamp value
        value = max(min_val, min(value, max_val))
        
        # Background arc (semi-circle)
        pygame.draw.arc(self.screen, (100, 100, 100), (pos[0] - radius, pos[1] - radius, 2 * radius, 2 * radius), math.pi, 2 * math.pi, 5)
        
        # Filled arc for progress (optional, for bar-like effect)
        arc_angle = math.pi + (value - min_val) / (max_val - min_val) * math.pi
        pygame.draw.arc(self.screen, (200, 200, 200), (pos[0] - radius, pos[1] - radius, 2 * radius, 2 * radius), math.pi, arc_angle, 5)
        
        # Needle
        needle_angle = math.pi + (value - min_val) / (max_val - min_val) * math.pi
        needle_length = radius * 0.8
        end_x = pos[0] + needle_length * math.cos(needle_angle)
        end_y = pos[1] + needle_length * math.sin(needle_angle)
        # Color needle based on value (green low, red high)
        color = (int(255 * (value - min_val) / (max_val - min_val)), int(255 * (1 - (value - min_val) / (max_val - min_val))), 0)
        pygame.draw.line(self.screen, color, pos, (end_x, end_y), 4)
        
        # Center circle for needle pivot
        pygame.draw.circle(self.screen, (255, 255, 255), pos, 5)
        
        # Value text
        text = self.small_font.render(f"{value:.1f}", True, (255, 255, 255))
        self.screen.blit(text, (pos[0] - text.get_width() / 2, pos[1] + radius / 2 + 5))
        
        # Label
        label_text = self.small_font.render(label, True, (200, 200, 200))
        self.screen.blit(label_text, (pos[0] - label_text.get_width() / 2, pos[1] - radius - 20))
    
    def handle_click(self, pos, params):
        # Placeholder for button clicks, e.g., reset params
        pass
