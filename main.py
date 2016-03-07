from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

matrix = [[0,0,0],
          [0,0,0],
          [0,0,0],
          [1,1,1]
          
add_edge(matrix, 10,0,10,0,10,0)
add_edge(matrix, 0,80,0,80,0,80)
add_edge(matrix, 30,30,0,0,0,30)
add_edge(matrix, 10,10,10,10,10,10)
add_edge(matrix, 0,0,0,50,0,0)

matrix = matrix_mult(make_translate(100,100,0),matrix)
matrix = matrix_mult(make_rotZ(pi),matrix)


draw_lines(matrix, screen, color)
display(screen)
