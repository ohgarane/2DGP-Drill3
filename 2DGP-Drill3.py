from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
boy = load_image('character.png')

def draw_boy(x,y):
    clear_canvas_now()
    boy.draw_now(x,y)
    delay(0.01)

def run_circle():
    print('CIRCLE')
    r,cx, cy = 300, 800//2, 600//2
    for degree in range(0,360, 3):
        theta = math.radians(degree)
        x = r * math.cos(theta) + cx
        y = r * math.sin(theta) + cy
        draw_boy(x, y)
    pass

def run_top():
    print('top')
    for x in range(0,800,10):
        draw_boy(x,550)
    pass
def run_right():
    print('right')
    for y in range(550, 50,-10):
        draw_boy(790,y)
    pass
def run_bottom():
    print('bottom')
    for x in range(800, 0, -10):
        draw_boy(x, 50)
    pass
def run_left():
    print('LEFT')
    for y in range(50, 550, 10):
        draw_boy(0,y)
    pass


def run_rectangle():
    print('RECTANGLE')
    run_top()
    run_right()
    run_bottom()
    run_left()

    
    pass
def run_triangle():
    print('TRIANGLE')
    x1, y1 = 400, 550
    x2, y2 = 200, 50
    x3, y3 = 600, 50

    for i in range(0, 100, 5):
        t = i/100
        x = (1-t) * x1 + t * x2
        y = (1-t) * y1 + t * y2
        draw_boy(x,y)
    for i in range(0, 100, 5):
        t = i / 100
        x = (1 - t) * x2 + t * x3
        y = (1 - t) * y2 + t * y3
        draw_boy(x, y)
    for i in range(0, 100, 5):
        t = i / 100
        x = (1 - t) * x3 + t * x1
        y = (1 - t) * y3 + t * y1
        draw_boy(x, y)

while True:
    run_rectangle()
    run_circle()
    run_triangle()
    break

close_canvas()
