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
	    takes 2 arguments (axis, theta) axis should be x, y or z
	 apply: apply the current transformation matrix to the 
	    edge matrix
	 display: draw the lines of the edge matrix to the screen
	    display the screen
	 save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 quit: end parsing

See the file script for an example of the file format
"""

def parse_file( fname, points, transform, screen, color ):
    with open(fname, "r") as file:
    	command = file.readline().strip()
    	while (command != "quit" and command != ""):

            if command == "line":
    			command = file.readline().strip()
    			args = command.split(" ")
    			if len(args) != 6:
    				print "Wrong number of arguments for line"
    			else:
    				add_edge(points, float(args[0]), float(args[1]), float(args[2]), float(args[3]), float(args[4]), float(args[5]))

            elif command == "ident":
    			ident(transform)

            elif command == "scale":
    			command = file.readline().strip()
    			args = command.split(" ")
    			if len(args) != 3:
    				print "Wrong number of arguments for scale"
    			else:
					smatrix = make_scale(float(args[0]),float(args[1]),float(args[2]))
					matrix_mult(smatrix, transform)

            elif command == "move":
    			command = file.readline().strip()
    			args = command.split(" ")
    			if len(args) != 3:
    				print "Wrong number of arguments for move"
    			else:
					tmatrix = make_translate(float(args[0]),float(args[1]),float(args[2]))
					matrix_mult(tmatrix, transform)

            elif command == "rotate":
    			command = file.readline().strip()
    			args = command.split(" ")
    			if len(args) != 2:
    				print "Wrong number of arguments for rotate"
    			else:
					if args[0] == "x":
						rmatrix = make_rotX(float(args[1]))
						matrix_mult(rmatrix, transform)
					elif args[0] == "y":
						rmatrix = make_rotY(float(args[1]))
						matrix_mult(rmatrix, transform)
					elif args[0] == "z":
						rmatrix = make_rotZ(float(args[1]))		
						matrix_mult(rmatrix, transform)
					else:
						print "Wrong Axis input, not x/y/z"

            elif command == "apply":
                matrix_mult(transform, points)

            elif command == "display":
                clear_screen(screen)
                draw_lines(points, screen, color)
                display(screen)

            elif command == "save":
                command = file.readline().strip()
                args = command.split(" ")
                if len(args) != 1:
                    print "Wrong number of args for save"
                else:
                    clear_screen(screen)
                    draw_lines(points, screen, color)
                    save_extension(screen,args[0])

            else:
                print "Command not found:" + command

            command = file.readline().strip() 
