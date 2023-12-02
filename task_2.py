#Task_1

from drawbot_skia.drawbot import rect, oval, newPage, saveImage, fill, stroke, strokeWidth, newDrawing
rules = [1, 0, 1, 0, 2, 0, 1, "еж"] * 20
w, h = 742.5, 1050
newPage(w, h)

margin = 80
x = margin
y = h - margin

step = (w - margin * 2) / 6
size = step

for rule in rules:
    if rule == 0:
        fill(0)
        stroke(0, 0, 0)
        strokeWidth(3)
        oval(x, y - step, size, size)
    elif rule == 1:
        fill(0)
        stroke(0, 0, 0)
        strokeWidth(3)
        rect(x, y - step, size, size)
    elif rule == 2:
        fill(None)
        stroke(0, 0, 0)
        strokeWidth(3)
        oval (x, y - step, size, size)
    else:
        print(rule, "<— неизвестное правило")
    
    x += step

    if x >= w - margin:
        x = margin
        y -= step

    if y - step < margin:
        newPage(w, h)
        x = margin
        y = h - margin

saveImage("task.pdf")


#Task_2
newDrawing()
rules = [1, 0, 2, 1, 0, 2, 0, 1] * 20
w, h = 742.5, 1050
newPage(w, h)

margin = 80
x = margin
y = h - margin

step = (w - margin * 2) / 6
size = step

for rule in rules:
    if rule == 0:
        fill(1, 0, 0, .5)
        stroke(0, 0, 0)
        strokeWidth(3)
        oval(x, y - step, size, size)
    elif rule == 1:
        fill(0, .5)
        stroke(0, 0, 0)
        strokeWidth(3)
        rect(x, y - step, size, size)
    elif rule == 2:
        fill(None)
        stroke(1, 0, 0)
        strokeWidth(3)
        oval (x, y - step, size, size)
    else:
        print(rule, "<— неизвестное правило")
    
    x += step

    if x >= w - margin:
        x = margin
        y -= step

    if y - step < margin:
        newPage(w, h)
        x = margin
        y = h - margin

saveImage("free_task.pdf")