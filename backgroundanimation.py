import pygame
import os

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Video Simulation in Pygame')

# Load video frames (assuming they are in a folder named 'frames')
frame_folder = 'frames'
frame_files = [os.path.join(frame_folder, f) for f in os.listdir(frame_folder) if f.endswith(('.png', '.jpeg'))]
frame_files.sort()  # Ensure frames are in the correct order
frames = [pygame.image.load(f).convert() for f in frame_files]

# Set frame rate (frames per second)
frame_rate = 30
clock = pygame.time.Clock()

# Main loop
running = True
current_frame = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Display the current frame
    screen.blit(frames[current_frame], (0, 0))
    pygame.display.flip()
    
    # Move to the next frame
    current_frame = (current_frame + 1) % len(frames)
    
    # Control frame rate
    clock.tick(frame_rate)

# Quit Pygame
pygame.quit()
