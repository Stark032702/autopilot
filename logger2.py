import matplotlib 
from collections import deque,defaultdict

class Logger2(): 

    def __init__(self, size, start_x, start_y, goal_x, goal_y, resolution): 
        self.size = size 
        self.start_x = start_x
        self.start_y = start_y 
        self.resolution = resolution 

        if show_animation: 
            