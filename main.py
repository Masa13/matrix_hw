from display import *
from draw import *
from math import *

screen = new_screen()
color = [ 0, 255, 0 ]

m = [[0,200,200,0],
     [10,0,0,100],
     [0,0,0,0],
     [1,1,1,1]]
          
add_edge(m, 10,0,10,0,10,0)
add_edge(m, 0,80,0,80,0,80)
add_edge(m, 30,30,0,0,0,30)
add_edge(m, 10,10,10,10,10,10)
add_edge(m, 0,0,0,50,0,0)

m = matrix_mult(make_translate(100,100,0),m)
m = matrix_mult(make_rotX(pi),m)


draw_lines(m, screen, color)
display(screen)
