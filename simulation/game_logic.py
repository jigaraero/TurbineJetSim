# simulation/game_logic.py - Game mechanics
# Handles game logic, parameter adjustments, challenges.

class GameLogic:
    def __init__(self):
        self.challenges = ["Max Thrust", "Fuel Efficiency"]
        self.score = 0
    
    def handle_key(self, event, params):
        if event.key == pygame.K_UP:
            params["altitude"] += 100
        elif event.key == pygame.K_DOWN:
            params["altitude"] = max(0, params["altitude"] - 100)
        elif event.key == pygame.K_LEFT:
            params["mach"] = max(0, params["mach"] - 0.1)
        elif event.key == pygame.K_RIGHT:
            params["mach"] += 0.1
        elif event.key == pygame.K_SPACE:
            params["throttle"] = 1.0 if params["throttle"] < 1.0 else 0.5
    
    def update(self, perf_data):
        # Simple scoring example
        self.score += perf_data["thrust"] / 10000 - perf_data["sfc"]
