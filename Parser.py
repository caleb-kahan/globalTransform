from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         move: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""
def script_display(points,screen,color):
    clear_screen(screen)
    draw_lines(points,screen,color)
    display(screen)

def script_save(fname,points,screen,color):
    clear_screen(screen)
    draw_lines(points,screen,color)
    save_extension(screen,fname)

def parse_file( fname, points, transform, screen, color ):
    f = open(fname,"r")
    currentCommand  = 0
    for line in f:
        line = line.strip()
        array = line.split()
        if not currentCommand and array[0] in ["display","ident","apply","display","quit"]:
            currentCommand = array[0]
        if currentCommand == "quit":
            break
        if currentCommand:
            switcher = {
                "line": lambda array, transform, points, screen, color: add_edge(points,float(array[0]),float(array[1]),float(array[2]),float(array[3]),float(array[4]),float(array[5])),
                "scale": lambda array, transform, points, screen, color: matrix_mult(make_scale(float(array[0]),float(array[1]),float(array[2])),transform),
                "move": lambda array, transform, points, screen, color: matrix_mult(make_translate(float(array[0]),float(array[1]),float(array[2])),transform),
                "rotate": lambda array, transform, points, screen, color: matrix_mult(rotate(array[0],float(array[1])),transform),
                "ident": lambda array, transform, points, screen, color: ident(transform),
                "apply": lambda array, transform, points, screen, color: matrix_mult(transform,points),
                "display": lambda array, transform, points, screen, color: script_display(points,screen,color),
                "save": lambda array, transform, points, screen, color: script_save(array[0],points,screen,color)
            }
            func = switcher.get(currentCommand)(array,transform,points,screen,color)
            currentCommand = 0
        else:
            currentCommand = array[0]
    f.close()
