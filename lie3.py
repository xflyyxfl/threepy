from __future__ import division
import math

import pygame
from pygame.locals import *

import THREE
from THREE.utils import Expando

from OpenGL.GL import *

width = 800
height = 600
renderer = THREE.OpenGLRenderer

pygame.init()
pygame.display.set_mode( (width, height), DOUBLEBUF|OPENGL )
renderer.init()
renderer.setSize( width, height )

texture = THREE.TextureLoader().load("UV_Grid_Sm.jpg")

scene = THREE.Scene()
camera = THREE.PerspectiveCamera( 45, width / height, 1, 2000 )
camera.position.z = 1000

# geometry = THREE.TorusKnotGeometry( 10, 3, 100, 16 )
geometry = THREE.BoxGeometry( 100, 100, 100, 1, 1, 1 )
material = THREE.MeshBasicMaterial( map = texture, side = THREE.DoubleSide )
cube = THREE.Mesh( geometry, material )
scene.add( cube )

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            pygame.quit()
            quit()

    cube.rotation.x += 0.01
    cube.rotation.y += 0.01
    renderer.render( scene, camera )

    pygame.display.flip()
    pygame.time.wait( 10 )