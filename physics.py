from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.sky import Sky
from ursina.shaders import lit_with_shadows_shader

app = Ursina()

plane = Entity(model="cube", texture="img/grass.png", scale=(100, 1, 100), position=(0, 0, 0), collider='box', shader=lit_with_shadows_shader)

car1 = Entity(model="model/blue_car.obj", texture="model/blue_car.mtl", scale=(0.2, 0.1, 0.1), position=(-10, 0.6, 0), collider='box', shader=lit_with_shadows_shader)
# desk = Entity(model="cube", texture="white_cube", scale=(8, 1, 1.5), position=(0, 1, 0), collider='box', shader=lit_with_shadows_shader)
wenzi1 = Entity(model="model/wenzi1.obj", scale=(1, 1, 1), position=(-10, 6, 0), rotation_x=90, rotation_y=180, shader=lit_with_shadows_shader)

car2 = Entity(model="model/blue_car.obj", texture="model/blue_car.mtl", scale=(0.2, 0.1, 0.1), position=(-10, 0.6, 22), collider='box', shader=lit_with_shadows_shader)
car3 = Entity(model="model/red_car.obj", texture="model/red_car.mtl", scale=(0.2, 0.1, 0.1), position=(-10, 0.6, 20), collider='box', shader=lit_with_shadows_shader)
wenzi2 = Entity(model="model/wenzi2.obj", scale=(1, 1, 1), position=(-10, 10, 20), rotation_x=90, rotation_y=180, shader=lit_with_shadows_shader)

water = Entity(model="cube", texture="img/water.png", scale=(2, 1, 2), position=(-10, 1, 30), shader=lit_with_shadows_shader)
water_block = Entity(model="cube", texture="white_cube", scale=(0.5, 0.5, 0.5), position=(-10, 1, 30), shader=lit_with_shadows_shader)
water_block = Entity(model="cube", texture="white_cube", scale=(0.5, 0.5, 0.5), position=(-10, 2.2, 30), shader=lit_with_shadows_shader, collider='box')
wenzi3 = Entity(model="model/wenzi3.obj", scale=(1, 1, 1), position=(-10, 8, 30), rotation_x=90, rotation_y=180, shader=lit_with_shadows_shader)

car1.animate_x(0, duration=3, loop=True)
car2.animate_x(1, duration=5, loop=True)
car3.animate_x(3, duration=3, loop=True)

Text.default_font = 'font/DroidSansFallback.ttf'


pivot = Entity()
DirectionalLight(parent=pivot, x=1000, y=100, z=-10, shadows=True)

# player = EditorCamera()
player = FirstPersonController(speed=20, position=(0,2,-10))
camera.overlay = None

sky = Sky()
app.run()
