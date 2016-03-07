from math import *

def make_translate( x, y, z ):
    return [[1,0,0,x],
            [0,1,0,y],
            [0,0,1,z],
            [0,0,0,1]]

def make_scale( x, y, z ):
    return [[x,0,0,0],
            [0,y,0,0],
            [0,0,z,0],
            [0,0,0,1]]
    
def make_rotX( theta ):   
    return [[1,0,0,0],
            [0,cos(theta),-sin(theta),0],
            [0,sin(theta),cos(theta),0],
            [0,0,0,1]]

def make_rotY( theta ):
    return [[cos(theta),0,-sin(theta),0],
            [0,1,0,0],
            [sin(theta),0,cos(theta),0],
            [0,0,0,1]]

def make_rotZ( theta ):
    return [[cos(theta),-sin(theta),0,0],
            [sin(theta),cos(theta),0,0],
            [0,0,1,0],
            [0,0,0,1]]

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

def print_matrix( matrix ):
    m = ''
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            m += str(matrix[x][y])
            m += '\t'
        m += '\n'
    print m

def ident( matrix ):
    m = new_matrix(len(matrix),len(matrix))
    for x in range(len(matrix)):
        m[x][x] = 1
    return m

def scalar_mult( matrix, n ):
    m = new_matrix(len(matrix[0]), len(matrix))
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            m[x][y] = n * matrix[x][y]
    return m

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    m = new_matrix(len(m2[0]),len(m1))
    for x in range(len(m1)):
        for y in range(len(m2[0])):
            for i in range(len(m2)):
                m[x][y] = m[x][y] + m1[x][i] * m2[i][y]
    return m
    
print_matrix(make_translate(1,2,3))
print
print_matrix(make_scale(4,5,6))
print
print_matrix(make_rotX(30))
print
print_matrix(make_rotY(90))
print
print_matrix(make_rotZ(180))
print
m1 = new_matrix(3,2)
m2 = new_matrix(2,3)
m1[0][0] = 1
m1[0][1] = 2
m1[0][2] = 3
m1[1][0] = 4
m1[1][1] = 5
m1[1][2] = 6
m2[0][0] = 7
m2[0][1] = 8
m2[1][0] = 9
m2[1][1] = 10
m2[2][0] = 11
m2[2][1] = 12
print_matrix(m1)
print
print_matrix(m2)
print
print_matrix(scalar_mult(m1,2))
print
print_matrix(matrix_mult(m1,m2))
