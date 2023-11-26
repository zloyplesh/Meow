#Task 1

from drawbot_skia.drawbot import oval, polygon, fill, saveImage, newDrawing
y = 50
step = 100
for i in range(9):
    oval(500, y, 100, 100)
    y = y + step
saveImage("task-1.pdf")


#Task 2
newDrawing()
x = 50
y = 50
step = 100
for i in range(9):
    for j in range (9):
        oval(x, y, 100, 100)
        y = y + step
    y = 50
    x = x + step
    
saveImage("task-2.pdf")


#Task 3 
#творческая композиция №404
newDrawing()
polygon ((100, 100), (100, 900), (900, 900), (200, 800), close = True)
polygon((100, 100), (900, 100), (900, 900), (800, 200), close = True)
x = 150
y = 150
step = 100
for i in range(7):
    fill(1, 0, 0, .5)
    oval (x, y, 100, 100)
    x = x + step
    y = y + step

x = 200
y = 750
step = 50
for i in range (13):
    fill(0, .5)
    oval(x, y, 50, 50)
    x = x + step
    y = y - step

y = 160
step = 50
for i in range (14):
    fill(1, 0, 0)
    oval(500, y, 30, 30)
    y = y + step

x = 170
step = 30
for i in range (24):
    fill(0)
    oval(x, 500, 10, 10)
    x = x + step
saveImage("task-3.pdf")

