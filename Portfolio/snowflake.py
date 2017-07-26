

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Snow")

ball_size = 5

class SnowFlake():
    '''
    This class will be used to create the SnowFlake Objects.
    It takes: 
        size - an integer that tells us how big we want the snowflake
        position - a 2 item list that tells us the coordinates of the snowflake (x,y) 
        wind - a boolean that lets us know if there is any wind or not.  
    '''

    def __init__(self, x , y):
    	self.x = x
    	self.y = y
    
    
    def fall(self, speed):
    	
        if self.y >= 500:
            self.y = random.randint(-40, -10)
    
        self.speed = 2
        self.y += self.speed
    	
    def draw(self):
    
        pygame.draw.circle(screen, WHITE, [self.x, self.y], 5)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()



# Speed
speed = 1


#INITIALIZE YOUR SNOWFLAKE

# Snow List
snow_list = []

for i in range(random.randint(300, 600)):
    x = random.randint(0, 700)
    y = random.randint(0, 500)
    snow_ball = SnowFlake(x, y)
    snow_list.append(snow_ball)
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    
    #REPLACE BELOW WITH UR PICTURE
    pic = pygame.image.load("snow.jpg")
    sizephoto = pygame.transform.scale(pic,(700,500))
    screen.blit(sizephoto, (0,0)) 
  

    # --- Drawing code should go here
    # Begin Snow

    for lol in snow_list:
        lol.fall(20)
        lol.draw()

    # End Snow
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() 
