# Fitts' test
import pygame
import random
import math
import time

# Constants for the experiment
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TARGET_RADIUS = 30
NUM_TRIALS = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fitts' Law Test")

# Function to calculate the distance between two points
def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Main loop
running = True
targets = []
trial = 0

while trial < NUM_TRIALS and running:
    trial += 1
    pygame.time.delay(1000)  # Pause for 1 second between trials
    screen.fill(WHITE)
    
    # Generate random target position
    target_x = random.randint(TARGET_RADIUS, SCREEN_WIDTH - TARGET_RADIUS)
    target_y = random.randint(TARGET_RADIUS, SCREEN_HEIGHT - TARGET_RADIUS)
    targets.append((target_x, target_y))
    
    # Draw the target
    pygame.draw.circle(screen, BLACK, (target_x, target_y), TARGET_RADIUS)
    pygame.display.flip()
    
    # Record the start time
    start_time = time.time()
    
    # Event handling
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                time_elapsed = time.time() - start_time
                dist_to_target = distance(x, y, target_x, target_y)
                print(f"Trial {trial}: Time Elapsed = {time_elapsed:.2f}s, Distance to Target = {dist_to_target:.2f}px")
                break

# Clean up and quit
pygame.quit()
