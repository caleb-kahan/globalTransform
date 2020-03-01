from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

parse_file( 'script', edges, transform, screen, color )

m= make_translate(3,6,9)
m= make_scale(3,6,9)
m = make_rotX(90)
print_matrix(m)
