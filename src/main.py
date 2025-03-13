from math import sqrt, floor
import random
from time import sleep, time
from ssd1306 import SSD1306_I2C
from machine import Pin, I2C, ADC


WIDTH: int = 128
HEIGHT: int = 64
SPEED: float = 3.0
COLLISION_DIST: int = 4 #a common radious of 2 pixels (2+2 = 4)


i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=400000)
print(i2c.scan()[0])
addres = i2c.scan()[0]
display = SSD1306_I2C(WIDTH, HEIGHT, i2c, addres)

button = Pin(14, Pin.IN, Pin.PULL_DOWN)
startTime = time()
running: bool = True


class Planet:
    planets = []
    
    def __init__(self, mass: float, pos: dict, vel: dict):
        self.mass = mass
        self.pos = pos
        self.vel = vel
        Planet.planets.append(self)
    
    @classmethod
    def GetPlanets(cls, self):
        for item in cls.planets:
            self.vel["x"] += (self.pos["x"] - item.pos["x"])/-100 / (self.mass + item.mass)
            self.vel["y"] += (self.pos["y"] - item.pos["x"])/-100 / (self.mass + item.mass)
            
            
    def DisplayPlanet(self):
        display.rect(int(self.pos.get("x", 0)), int(self.pos.get("y", 0)), floor(sqrt(self.mass)), floor(sqrt(self.mass)), 1)
        
    
    def AddLocation(self):
        self.pos["x"] += self.vel["x"]
        self.pos["y"] += self.vel["y"]
    
    @classmethod
    def CheckCollision(cls, self):
        global running
        cls.planets.remove(self)
        for item in cls.planets:
            if sqrt(abs(self.pos["x"] - item.pos["x"])**2 + abs(self.pos["y"] - item.pos["y"])**2) < COLLISION_DIST:
                print("collision", random.randint(1,10000))
                endTime = time()
                running = False
                print(endTime - startTime)
                display.text("Runtime: " + str(endTime - startTime) + "s", 0, 0, 1)
                break
        cls.planets.append(self)
        

p1 = Planet(3, {"x":0, "y":0}, {"x":0, "y":0.4})
p2 = Planet(15, {"x":80, "y":20}, {"x":0, "y":0})
p3 = Planet(3, {"x":50, "y":10}, {"x":0, "y":2})

while running:
    if button.value():
        print("pressed")

    p1.AddLocation()
    p2.AddLocation()
    p3.AddLocation()
    
    Planet.GetPlanets(p1)
    Planet.GetPlanets(p2)
    Planet.GetPlanets(p3)
    
    p1.DisplayPlanet()
    p2.DisplayPlanet()
    p3.DisplayPlanet()
    
    Planet.CheckCollision(p1)
    Planet.CheckCollision(p2)
    Planet.CheckCollision(p3)
    
    display.show()
    display.fill(0)
    #sleep(0.02)