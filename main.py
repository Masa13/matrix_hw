from display import *
from draw import *
from math import *

screen = new_screen()
color = [ 0, 255, 0 ]

m0 = [[0,200,200,0],
     [100,0,0,100],
     [0,100,100,0],
     [1,1,1,1]]

m1 = matrix_mult(make_translate(100,100,0),m0)
m2 =  matrix_mult(make_rotX(pi),m0)

draw_lines(m0,screen,color)
draw_lines(m1,screen,color)
draw_lines(m2,screen,color)


display(screen)
