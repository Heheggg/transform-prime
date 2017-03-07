import math

def make_translate( x, y, z ):
    output = [[1,0,0,a],[0,1,0,b],[0,0,1,c],[0,0,0,1]];
    return output

def make_scale( x, y, z ):
    output = [[a,0,0,0],[0,b,0,0],[0,0,c,0],[0,0,0,1]];
    return output

def make_rotX( theta ):
    output = [[1,0,0,0],
              [0,cos(theta),-sin(theta),0],
              [0, sin(theta),cos(theta),0],
              [0,0,0,1]]
    return output

def make_rotY( theta ):
    output = [[cos(theta),0,sin(theta),0],
              [0,1,0,0],
              [cos(theta),0,sin(theta),0],
              [0,0,0,1]]

def make_rotZ( theta ):
    cos = math.cos 
    output = [[cos(theta), - sin(theta), 0 , 0],
              [sin(theta, cos(feta)), 0 ,0],
              [0,0,1,0],
              [0,0,0,1]]
    return output

def print_matrix( matrix ):
    s = ''
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            s+= str(matrix[c][r]) + ' '
        s+= '\n'
    print s

def ident( matrix ):
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            if r == c:
                matrix[c][r] = 1
            else:
                matrix[c][r] = 0

def scalar_mult( matrix, s ):
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            matrix[c][r]*= s
            
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):

    point = 0
    for row in m2:
        #get a copy of the next point
        tmp = row[:]
        
        for r in range(4):
            m2[point][r] = (m1[0][r] * tmp[0] +
                            m1[1][r] * tmp[1] +
                            m1[2][r] * tmp[2] +
                            m1[3][r] * tmp[3])
        point+= 1


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
