from display import *
from draw import *
from math import *

screen = new_screen()
color = [ 0, 255, 0 ]

m = [[0,200,200,0],
     [100,0,0,100],
     [0,100,100,0],
     [1,1,1,1]]
          
add_edge(m, 100,0,100,0,100,0)
add_edge(m, 0,200,0,200,0,200)
add_edge(m, 100,100,0,0,0,100)
add_edge(m, 100,100,00,0,0,0)
add_edge(m, 0,0,200,200,0,0)

m = matrix_mult(make_translate(100,100,0),m)
m = matrix_mult(make_rotX(pi),m)


draw_lines(m, screen, color)
display(screen)
