from display import *
from draw import *
from Parser import *
from matrix import *

screen = new_screen()
color = [ 255, 165, 0 ]
edges = []
transform = new_matrix()

parse_file( 'script', edges, transform, screen, color )
'''
script = open('coneScript','w')
miniEdges = []
add_edge(miniEdges,0,0,0,5,20,0)
add_edge(miniEdges,5,20,0,10,0,0)
add_edge(miniEdges,0,0,0,10,0,0)

for theta in range(100):
    matrix_add(edges,miniEdges)
    rotationMatrix = rotate("y",3.6)
    matrix_mult(rotationMatrix,miniEdges)

rotationMatrix = make_rotX(30)
matrix_mult(rotationMatrix,edges)
rotationMatrix = make_rotY(30)
matrix_mult(rotationMatrix,edges)
rotationMatrix = make_rotZ(30)
matrix_mult(rotationMatrix,edges)


scalingMatrix = make_scale(15,15,0)
matrix_mult(scalingMatrix,edges)

translationMatrix = make_translate(250,150,0)
matrix_mult(translationMatrix,edges)

script_display(edges,screen,color)
'''
