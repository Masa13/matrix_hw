from display import *
from draw import *
from math import *

screen = new_screen()
color1 = [ 0, 0, 255 ]
color2 = [255,0,0]

m0 = [[0,200,200,0],
     [100,0,0,100],
     [0,100,100,0],
     [1,1,1,1]]

m1 = [[100,100,100,100],
      [200,200,0,0],
      [0,0,300,300],
      [1,1,1,1]]
#m1 = matrix_mult(make_translate(100,100,0),m0)
i = 0
while i < 500:
     n = 0
     n = 0
     m2 = m0
     m3 = m1
     x = 0
     y = 0
     while n < 360:
          m2 = matrix_mult(make_translate(x,y,0),m2)
          m3 = matrix_mult(make_translate(x,y,0),m2)
          
          m2 = matrix_mult(make_rotX(pi/13),m2)
          m3 = matrix_mult(make_scale(1.1,1.1,1),m2)  
          draw_lines(m2,screen,color1)
          draw_lines(m3,screen,color2)
          n+=1
     x+=20
     y+=20
     i+=1

    
#draw_lines(m0,screen,color)
#draw_lines(m1,screen,color)
#draw_lines(m2,screen,color)

display(screen)
