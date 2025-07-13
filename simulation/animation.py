# simulation/animation.py - Graphics and animation
# Handles cool Pygame-based animation of the engine with rotating parts.

import pygame
import math

class Animation:
    def __init__(self, screen):
        self.screen = screen
        self.engine_image = pygame.Surface((800, 300)).convert_alpha()  # Placeholder for engine
        self.engine_image.fill((0, 0, 0, 0))
        self.draw_engine()
        
        self.rotor_angle = 0
        self.rotor_speed = 0  # Will be set based on throttle
    
    def draw_engine(self):
        # Draw static engine parts
        pygame.draw.rect(self.engine_image, (150, 150, 150), (0, 100, 800, 100))  # Body
        # Inlet
        pygame.draw.polygon(self.engine_image, (100, 100, 100), [(0, 100), (0, 200), (50, 150)])
        # Nozzle
        pygame.draw.polygon(self.engine_image, (100, 100, 100), [(750, 150), (800, 100), (800, 200)])
    
    def update(self, data):
        self.rotor_speed = data["thrust"] / 1000  # Scale for animation
        self.rotor_angle += self.rotor_speed
        self.rotor_angle %= 360
    
    def draw(self):
        # Draw engine base
        self.screen.blit(self.engine_image, (200, 200))
        
        # Draw rotating compressor/turbine blades (cool animation)
        center_x, center_y = 500, 350  # Adjust position
        for i in range(8):  # 8 blades
            angle = math.radians(self.rotor_angle + i * 45)
            x1 = center_x + 50 * math.cos(angle)
            y1 = center_y + 50 * math.sin(angle)
            x2 = center_x + 80 * math.cos(angle)
            y2 = center_y + 80 * math.sin(angle)
            pygame.draw.line(self.screen, (200, 200, 200), (x1, y1), (x2, y2), 5)
        
        # Flame effect for exhaust
        flame_length = 100 + 50 * math.sin(math.radians(self.rotor_angle * 5))
        pygame.draw.polygon(self.screen, (255, 100, 0), [(1000, 300), (1000 + flame_length, 250), (1000 + flame_length, 350)])
