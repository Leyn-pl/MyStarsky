# MYSTARSKY by LEYN1092

import random
import time
import os
import math

# Settings
skyWidth: int = 156
skyHeight: int = 40
starSpawnRate: float = 0.3
sleepMS: int = 20
starLifetimeMultiplier = 2
consoleClearCommand: str = "cls" # Change if using not windows
starCharPool: list = list("qwertyuiopasdfghjklzxcvbnm".upper())

# Build sky
def clearSky():
    global Sky
    Sky = [[" " for _ in range(skyWidth)] for _ in range(skyHeight)]

class Star:
    def __init__(self, x: int, trail: int, lifetime: float):
        self.x = x
        self.y = 0
        self.trail = trail
        self.lifetime = lifetime
        self.char = random.choice(starCharPool)
        self.angle = 0 if random.random() > 0.5 else random.getrandbits(1) * 2 - 1
    def update(self) -> bool:
        # Returns whether this star is alive after update
        self.y += 1
        self.x += self.angle
        self.lifetime -= 1
        if self.lifetime == 0 or self.y - self.trail > skyHeight:
            return False
        else:
            return True
    def draw(self):
        global Sky
        # Draw body
        if self.x > 0 and self.x < skyWidth and self.y > 0 and self.y < skyHeight:
            Sky[self.y][self.x] = self.char
        # Draw trail
        for i in range(self.trail):
            offset = i + 1
            # Out of Y bounds check
            if self.y - offset < 0 or self.y - offset >= skyHeight:
                break
            if self.angle == 0:
                Sky[self.y - offset][self.x] = "|"
            else:
                if self.x - offset*self.angle > 0 and self.x - offset*self.angle < skyWidth:
                    Sky[self.y - offset][self.x - offset*self.angle] = "/" if self.angle < 0 else "\\"

# Main loop
stars = []
while True:
    # Add new star
    if random.random() < starSpawnRate:
        stars.append(Star(random.randrange(0, skyWidth), random.randrange(1, 4), random.randint(int(skyHeight * 0.1), skyHeight + 3) * starLifetimeMultiplier))
    
    # Update and draw all stars
    clearSky()
    for starID in range(len(stars)):
        if stars[starID].update() == False:
            # Mark star for death
            stars[starID] = 0
            continue
        stars[starID].draw()
    # Remove marked for death stars
    stars = list(filter(lambda x: x != 0, stars))
        
    # Print out sky
    os.system(consoleClearCommand)
    for y in range(skyHeight):
        line = ""
        for x in range(skyWidth):
            line += Sky[y][x]
        print(line)
    
    # Delay
    time.sleep(sleepMS / 1000)