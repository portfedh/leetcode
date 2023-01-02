# Dev Degree Problem 7


# Create a class to represent the robots movements:
###################################################

class Robot():

    def __init__(self, degrees):
        self.pointing_at = degrees # Degrees
        self.attempted_rotations = 0 # Attempts

        print('Starting Game:')
        print('Currently pointing at: ', self.pointing_at, ' degrees.')
        print('Attempted rotations: ', self.attempted_rotations, '\n')


    def turn(self, degrees):

        # Increase attempted rotations
        self.attempted_rotations += 1
        print('Turn Number: ', self.attempted_rotations)
        print('###############')

        # See where it should now be pointing at
        self.pointing_at += degrees 
        self.pointing_at = self.pointing_at % 360

        print('Rotate: ', degrees, ' degrees.')
        print('Should now point at: ', self.pointing_at, ' degrees. \n')

        # Add the error that needs replacing
        self.add_error(degrees)


    def add_error(self, degrees):
        '''Whenever Chuck attempts to rotate in a given direction an additional rotation occurs:
        90° clockwise x the total number of attempted rotations '''

        # Get total rotations attempted
        print('Attempted rotations: ', self.attempted_rotations)

        # Calculate the extra rotation
        self.extra_rotation = 90 * self.attempted_rotations
        print('Extra rotation: 90 *', self.attempted_rotations, ' = ', self.extra_rotation, ' degrees.')

        # Add extra rotation and check where Chuck is now facing
        self.pointing_at += self.extra_rotation
        self.pointing_at = self.pointing_at % 360
        print('Really now pointing at: ', self.pointing_at, ' degrees.\n')

# Key to interpret where Chuck is facing:
#########################################

# Degrees grow to the right from 0 - 360.
#   0 = North
#  90 = East
# 180 = South
# 270 = West


# Run Problem 7
###############

# Starts facing the east door.
chuck = Robot(90)

# Chuck moves forward 10ft and attempts to turn 360° to the left.
chuck.turn(-360)

# Chuck moves another 10ft forward and attempts to turn 90° to the right
chuck.turn(90)

# Chuck realizes they are facing the wrong direction and attempts to turn 180° to the left
chuck.turn(-180)

# Chuck attempts to turn 90° to the right and moves forward 15ft.
chuck.turn(90)

# Chuck attempts to turn 90° to the left, moves forward 8ft 
chuck.turn(-90)

# and attempts to turn 90° to the right.
chuck.turn(90)

# Output:
#########

# Starting Game:
# Currently pointing at:  90  degrees.
# Attempted rotations:  0 

# Turn Number:  1
# ###############
# Rotate:  -360  degrees.
# Should now point at:  90  degrees. 

# Attempted rotations:  1
# Extra rotation: 90 * 1  =  90  degrees.
# Really now pointing at:  180  degrees.

# Turn Number:  2
# ###############
# Rotate:  90  degrees.
# Should now point at:  270  degrees. 

# Attempted rotations:  2
# Extra rotation: 90 * 2  =  180  degrees.
# Really now pointing at:  90  degrees.

# Turn Number:  3
# ###############
# Rotate:  -180  degrees.
# Should now point at:  270  degrees. 

# Attempted rotations:  3
# Extra rotation: 90 * 3  =  270  degrees.
# Really now pointing at:  180  degrees.

# Turn Number:  4
# ###############
# Rotate:  90  degrees.
# Should now point at:  270  degrees. 

# Attempted rotations:  4
# Extra rotation: 90 * 4  =  360  degrees.
# Really now pointing at:  270  degrees.

# Turn Number:  5
# ###############
# Rotate:  -90  degrees.
# Should now point at:  180  degrees. 

# Attempted rotations:  5
# Extra rotation: 90 * 5  =  450  degrees.
# Really now pointing at:  270  degrees.

# Turn Number:  6
# ###############
# Rotate:  90  degrees.
# Should now point at:  0  degrees. 

# Attempted rotations:  6
# Extra rotation: 90 * 6  =  540  degrees.
# Really now pointing at:  180  degrees.

