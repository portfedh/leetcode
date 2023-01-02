# Dev Degree Problem 8.

# Problem:
##########
# They plan to put items in their van arranged from largest to smallest back to front.
# In cases where items are the same size:
# Jaime plans to order them via weight, with heavier objects placed before lighter ones.

# Approaches.
# Not sure if largest meant largest volume, or only length & width. 

# Approach 1: Using volume.
###########################

# I coded this class to calculate the volume of each box.ç
class Box():

    def __init__(self, name, length, width, weight, height=1):
        self.name = name
        self.length = length
        self.width = width
        self.height = height
        self.volume = (self.length * self.width * self.height)
        self.weight = weight

    def __repr__(self):
        return str(self.name) + ', Vol: ' + str(self.volume) +', Weight: '+ str(self.weight)


# I then added the input for all the boxes in the problem:
plastic_table = Box(name='Plastic table', length=96, width=30, height=01, weight=4.50)
dresses       = Box(name='Dresses',       length=16, width=12, height=12, weight=4.50)
socks         = Box(name='Socks',         length=18, width=16, height=18, weight=2.10)
tshirts       = Box(name='Tshirts',       length=18, width=16, height=18, weight=1.53)
metal_table   = Box(name='Metal table',   length=30, width=96, height=01, weight=8.20)
hats          = Box(name='Hats',          length=16, width=12, height=12, weight=2.10)
jackets       = Box(name='Jackets',       length=18, width=18, height=24, weight=12.0)
scarfs        = Box(name='Scarfs',        length=16, width=12, height=12, weight=3.60)


# Then made a list with all the objects.
boxes = [plastic_table, dresses, socks, tshirts,metal_table, 
         hats, jackets, scarfs]

# Finally I sorted  the boxes by weight and volume and printed the output:
boxes.sort(key=lambda x: x.weight, reverse=True)
boxes.sort(key=lambda x: x.volume, reverse=True)

for x in range(len(boxes)):
    print(boxes[x])

# Output:
#########
# Jackets,       Vol: 7776, Weight: 12
# Socks,         Vol: 5184, Weight: 2.1
# Tshirts,       Vol: 5184, Weight: 1.53
# Metal table,   Vol: 2880, Weight: 8.2
# Plastic table, Vol: 2880, Weight: 4.5
# Dresses,       Vol: 2304, Weight: 4.5
# Scarfs,        Vol: 2304, Weight: 3.6
# Hats,          Vol: 2304, Weight: 2.1

# None of the possible answers start with Jackets, so the problem must not be taking into acount height. 


# Approach 2: Using Area.
#########################
# Tables have the largest surface area by far, so They must come first.
# Both tables have the same area.
# Metal table weighs more than plastic table, so it must come first.
# There is only one option where Metal table is first and Plastic table is second.
