from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.sky import Sky

app = Ursina()

sun = Entity(model="sphere", texture="./img/sun.png", scale=15, position=(0, 0, 0))
mercury = Entity(model="sphere", texture="./img/mercury.png", scale=1, position=(20, 0, 10))
venus = Entity(model="sphere", texture="./img/venus.png", scale=2, position=(40, 0, 5))
earth = Entity(model="sphere", texture="./img/earth.png", scale=2, position=(60, 0, 15))
earth = Entity(model="sphere", texture="./img/earth.png", scale=2, position=(60, 0, 15))
mars = Entity(model="sphere", texture="./img/mars.png", scale=1.5, position=(80, 0, 20))
jupiter = Entity(model="sphere", texture="./img/jupiter.png", scale=5, position=(110, 0, 30))
saturn = Entity(model="sphere", texture="./img/saturn.png", scale=4.5, position=(150, 0, 35))
uranus = Entity(model="sphere", texture="./img/uranus.png", scale=3.5, position=(180, 0, 25), roataion_x=90)
neptune = Entity(model="sphere", texture="./img/neptune.png", scale=4.5, position=(200, 0, 20))
saturnring = Entity(model="cube", texture="./img/saturnring.png", scale=(10, 0, 10), position=(150, 0, 35))

Text.default_font = 'font/DroidSansFallback.ttf'
text2 = Text(text='按下m键切换鼠标锁定状态', origin=(2,-18), scale=1)

def input(key):
    if key == 'm':
        mouse.locked = not mouse.locked
        print(mouse.velocity)



player = EditorCamera()
player = FirstPersonController(gravity=0, speed=20)
camera.overlay = None

sky = Sky(texture="./img/sky.png")
app.run()
