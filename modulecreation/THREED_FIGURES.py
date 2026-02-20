
import math
# -------- CUBE --------
def cube_volume(side):
    return side ** 3

def cube_surface_area(side):
    return 4*side*side

def cube_totalarea(side):
    return 6*side*side
    #------CUBOID------
def cuboid_volume(length, breadth, height):
    return length * breadth * height

def cuboid_totalsurface_area(length, breadth, height):
    return 2 * (length * breadth + breadth * height + height * length)
def cuboid_surface_area(length,breadth,height):
    return 2*height*(length+breadth)
# -------- CYLINDER --------
def cylinder_volume(radius, height):
    return math.pi * radius ** 2 * height

def cylinder_Tsurface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)
def cylinder_curved_surface_area(radius, height):
    return 2 * math.pi * radius * height
#-----HEMISHERE-----
def hemisphere_volume(radius):
    return (2/3) * math.pi * radius ** 3

def hemisphere_surface_area(radius):
    return 3 * math.pi * radius ** 2
# -------- SPHERE --------
def sphere_volume(radius):
    return (4/3) * math.pi * radius ** 3

def sphere_surface_area(radius):
    return 4 * math.pi * radius ** 2
# -------- CONE --------

def cone_volume(radius, height):
    """
    Returns the volume of cone
    Formula: (1/3) * π * r^2 * h
    """
    return (1/3) * math.pi * radius ** 2 * height


def cone_curved_surface_area(radius, height):
    """
    Returns curved surface area of cone
    Formula: π * r * l
    where l = slant height
    """
    slant_height = math.sqrt(radius ** 2 + height ** 2)
    return math.pi * radius * slant_height


def cone_total_surface_area(radius, height):
    """
    Returns total surface area of cone
    Formula: π * r * (r + l)
    """
    slant_height = math.sqrt(radius ** 2 + height ** 2)
    return math.pi * radius * (radius + slant_height)



