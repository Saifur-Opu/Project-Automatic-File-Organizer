import tkinter as tk
import random

WIDTH, HEIGHT = 700, 700

root = tk.Tk()
root.title("Smart Traffic System (AI Lights)")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="darkgreen")
canvas.pack()

# Roads
canvas.create_rectangle(300, 0, 400, HEIGHT, fill="gray")
canvas.create_rectangle(0, 300, WIDTH, 400, fill="gray")

# Lights
ns_light = "green"
ew_light = "red"

ns_ui = canvas.create_oval(420, 260, 440, 280, fill="green")
ew_ui = canvas.create_oval(260, 420, 280, 440, fill="red")

cars = []

class Car:
    def __init__(self, direction):
        self.direction = direction
        self.speed = 2

        if direction == "NS":
            self.id = canvas.create_rectangle(330, -40, 370, 0, fill="blue")
        else:
            self.id = canvas.create_rectangle(-40, 330, 0, 370, fill="red")

    def move(self):
        coords = canvas.coords(self.id)

        # Stop at red light
        if self.direction == "NS":
            if ns_light == "red" and 280 < coords[3] < 350:
                return
            canvas.move(self.id, 0, self.speed)

            if coords[1] > HEIGHT:
                canvas.coords(self.id, 330, -40, 370, 0)

        else:
            if ew_light == "red" and 280 < coords[2] < 350:
                return
            canvas.move(self.id, self.speed, 0)

            if coords[0] > WIDTH:
                canvas.coords(self.id, -40, 330, 0, 370)

# Spawn cars
def spawn():
    cars.append(Car(random.choice(["NS", "EW"])))
    root.after(1500, spawn)

# Move cars
def update():
    for car in cars:
        car.move()
    root.after(30, update)

# 🔥 Count waiting cars (TRAFFIC DENSITY)
def count_density():
    ns_count = 0
    ew_count = 0

    for car in cars:
        x1, y1, x2, y2 = canvas.coords(car.id)

        if car.direction == "NS" and 250 < y2 < 350:
            ns_count += 1

        if car.direction == "EW" and 250 < x2 < 350:
            ew_count += 1

    return ns_count, ew_count

# 🧠 Smart light controller
def smart_lights():
    global ns_light, ew_light

    ns_count, ew_count = count_density()

    # Decide who gets green
    if ns_count > ew_count:
        ns_light = "green"
        ew_light = "red"
    elif ew_count > ns_count:
        ns_light = "red"
        ew_light = "green"
    else:
        # Equal → alternate
        ns_light = "green" if ns_light == "red" else "red"
        ew_light = "red" if ns_light == "green" else "green"

    # Update UI
    canvas.itemconfig(ns_ui, fill=ns_light)
    canvas.itemconfig(ew_ui, fill=ew_light)

    # ⏱ Dynamic timing (more cars = longer green)
    delay = 2000 + max(ns_count, ew_count) * 500

    root.after(delay, smart_lights)

# Start simulation
spawn()
update()
smart_lights()

root.mainloop()