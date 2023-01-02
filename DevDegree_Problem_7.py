
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

        self.add_error(degrees)


    def add_error(self, degrees):

        # Add error rotation
        print('Attempted rotations: ', self.attempted_rotations)

        self.extra_rotation = 90 * self.attempted_rotations
        print('Extra rotation: 90 *', self.attempted_rotations, ' = ', self.extra_rotation, ' degrees.')

        self.pointing_at += self.extra_rotation
        self.pointing_at = self.pointing_at % 360
        print('Really now point at: ', self.pointing_at, ' degrees.\n')

#   0 = North
#  90 = East
# 180 = South
# 270 = West

chuck = Robot(90)
chuck.turn(-360)
chuck.turn(90)
chuck.turn(-180)
chuck.turn(90)
chuck.turn(-90)
chuck.turn(90)
