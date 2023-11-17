from vpython import *

scene = canvas(width=800, height=600, center=vector(0, 0, 0), background=color.black)

earth = sphere(pos=vector(10, 0, 0), radius=2, color=color.cyan)
sun = sphere(pos=vector(0, 0, 0), radius=5, color=color.red)

# 공전 애니메이션
while True:
    rate(30)
    earth.rotate(angle=0.02, axis=vector(0, 1, 0), origin=vector(0, 0, 0))
