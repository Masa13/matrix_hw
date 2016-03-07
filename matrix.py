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
    deg = radians(theta)
    return [[1,0,0,0],
            [0,cos(deg),-sin(deg),0],
            [0,sin(deg),cos(deg),0],
            [0,0,0,1]]

def make_rotY( theta ):
    deg = radians(theta)
    return [[cos(deg),0,-sin(deg),0],
            [0,1,0,0],
            [sin(deg),0,cos(deg),0],
            [0,0,0,1]]

def make_rotZ( theta ):
    deg = radians(theta)
    return [[cos(deg),-sin(deg),0,0],
            [sin(deg),cos(deg),0,0],
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
