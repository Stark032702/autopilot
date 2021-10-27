import matplotlib.pyplot 
import pygame
from collections import defaultdict, deque

class Logger(): 

    def __init__(self,fps, size, start_x, start_y, goal_x, goal_y): 
        self.fps = fps
        self.size = size 

        pygame.init()
        self.screen = pygame.display.set_mode(self.size, self.size)
        

