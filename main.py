import sys

def v_transfer(m1,m2,v1,v2):                    #perfectly elastic collision velocity transfer
    t1 = ((m1-m2)*v1 + 2*m2*v2) / (m1 + m2)
    v2 = ((m2-m1)*v2 + 2*m1*v1) / (m1 + m2)
    v1 = t1
    return v1,v2

def main(argv):
    m1 = 100            #mass of the tiny cube (in decigrams)
    try:
        m2 = int(argv[1]) * 100  # Tries to access argv[1]
    except IndexError:
        print("Error: Missing argument. Please provide a mass integer in kgs as follows: \" python3 main.py *mass* \".")
        sys.exit(1)  # Exits with error code 1

    v1 = 0              #initial velocity of cube1
    v2 = -14000              #   //      //    of cube2
    pos1 = 150000         #initial positions on the 2D line from the wall
    pos2 = 600000
    t = 0
    collisions = 0

    while True:
        if pos2 > pos1:              #there are no collisions between the cubes
            if pos1 <= 0:            #there is a collision with the cube
                v1 = -v1
                collisions += 1
            pos2 = pos2 + v2
            pos1 = pos1 + v1
        else:                        #there is collision between the cubes
            v1,v2 = v_transfer(m1,m2,v1,v2)
            collisions += 1
            pos2 = pos2 + v2
            pos1 = pos1 + v1
        if (v1 >= 0) and (v2 >= 0) and (v2 > v1):       #if the tiny cube will never reach the second one, we already know collisions are done
            break
    
    print(collisions)

if __name__ == "__main__":
   main(sys.argv)