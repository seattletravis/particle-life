## A simple Python port - You need: pip install pygame. Note the code here is not efficient but it's made to be educational and easy
import pygame
import random

atoms=[]
window_width = 750
window_height = 750
pygame.init()
window = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)


def draw(surface, x, y, color, size):
    for i in range(0, size):
        pygame.draw.line(surface, color, (x, y-1), (x, y+2), abs(size))
               
def atom(x, y, c):
    return {"x": x, "y": y, "vx": 0, "vy": 0, "color": c}

def randomxy():
    return round(random.random()*window_width + 1)

def create(number, color):
    group = []
    for i in range(number):
        group.append(atom(randomxy(), randomxy(), color))
        atoms.append((group[i]))
    return group

def rule(atoms1, atoms2, g):
    for i in range(len(atoms1)):
        fx = 0
        fy = 0
        for j in range(len(atoms2)):
            a = atoms1[i]
            b = atoms2[j]
            dx = a["x"] - b["x"]
            dy = a["y"] - b["y"]
            d = (dx*dx + dy*dy)**0.5
            if( d > 0 and d < 80):
                F = g/d
                fx += F*dx
                fy += F*dy
        a["vx"] = (a["vx"] + fx)*0.5
        a["vy"] = (a["vy"] + fy)*0.5
        a["x"] += a["vx"]
        a["y"] += a["vy"]
        # Bounce Off Wall Logic
        if(a["x"] <= 0 or a["x"] >= window_width):
            a["vx"] *=-2
        if(a["y"] <= 0 or a["y"] >= window_height):
            a["vy"] *=-2 
        # Pass Through Wall Logic      
        # if(a["x"] <= 0):
        #     a["x"] = window_width
        # elif(a["x"] >= window_width):
        #     a["x"] = 0
        # if(a["y"] <= 0):
        #     a["y"] = window_height
        # elif(a["y"] >= window_height):
        #     a["y"] = 0

yellow = create(100, "yellow")
red = create(100, "red")
blue = create(100, "blue")
green = create(100, "green")

run = True
while run:
    window.fill(0)
    rule(yellow, yellow, -0.2)
    rule(red, red, -0.2)
    rule(blue, blue, -0.2)
    rule(green, green, -0.2)

    rule(yellow, red, 0.1)
    rule(yellow, blue, 0.1)
    rule(yellow, green, 0.1)

    rule(red, yellow, -0.1)
    rule(red, blue, 0.1)
    rule(red, green, 0.1)

    rule(blue, red, -0.1)
    rule(blue, yellow, 0.1)
    rule(blue, green, 0.1)

    rule(green, blue, -0.2)
    rule(green, yellow, 0.1)
    rule(green, red, 0.1)

    # rule(red, yellow, 0.1)
    # rule(blue, yellow, 0.1)
    # rule(green, yellow, 0.1)

    # rule(yellow, red, -0.1)
    # rule(blue, red, 0.1)
    # rule(green, red, 0.1)

    # rule(red, blue, -0.1)
    # rule(yellow, blue, 0.1)
    # rule(green, blue, 0.1)

    # rule(blue, green, -0.1)
    # rule(yellow, green, 0.1)
    # rule(red, green, 0.1)


    for i in range(len(atoms)):
        draw(window,  atoms[i]["x"], atoms[i]["y"], atoms[i]["color"], 2)
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()
exit()