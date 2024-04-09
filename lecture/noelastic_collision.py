import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Inelastic Collision Example")

# Object properties
mass1 = 55.0  # Mass of object 1 (Jack)
mass2 = 48.0  # Mass of object 2 (Jill)
velocity1 = 0.10  # Initial velocity of Jack (m/s)
angle1_degrees = 20.0  # Angle in degrees (east direction)
angle1_radians = math.radians(angle1_degrees)  # Convert to radians

# Calculate initial velocity components
vx1 = velocity1 * math.cos(angle1_radians)
vy1 = velocity1 * math.sin(angle1_radians)

# Combined mass
total_mass = mass1 + mass2

# Calculate final velocity components after collision
vx_combined = (mass1 * vx1 + mass2 * 0) / total_mass
vy_combined = (mass1 * vy1 + mass2 * 0) / total_mass

# Convert back to magnitude and angle
combined_velocity = math.sqrt(vx_combined**2 + vy_combined**2)
combined_angle_radians = math.atan2(vy_combined, vx_combined)
combined_angle_degrees = math.degrees(combined_angle_radians)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw the combined object (stick together after collision)
    pygame.draw.circle(screen, (255, 0, 0), (int(WIDTH / 2), int(HEIGHT / 2)), 20)

    # Update the display
    pygame.display.flip()

    # Print the results
    print(f"Combined velocity: {combined_velocity:.2f} m/s")
    print(f"Combined angle: {combined_angle_degrees:.2f} degrees")

    # You can add more objects and collision logic here

    pygame.time.Clock().tick(60)