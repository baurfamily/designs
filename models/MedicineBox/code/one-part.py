#!sh

#Gui.runCommand('Std_Workbench',19)
#Gui.runCommand('Std_ViewStatusBar',1)
### Begin command Std_Open
#FreeCAD.openDocument('/Users/ebaur/Library/Mobile Documents/com~apple~CloudDocs/Crafts/designs/models/MedicineBox/MedicineBox.FCStd')
# App.setActiveDocument("MedicineBox")
# App.ActiveDocument=App.getDocument("MedicineBox")
# Gui.ActiveDocument=Gui.getDocument("MedicineBox")
#
# ## End command Std_Open
#
# import App
# import Part
import Show
# import Sketcher
import PartDesignGui

from collections import namedtuple
from math import tan, sqrt, radians

# get document above?

# add part
doc = App.newDocument('GeneratedBox')


# setting up a custom vector-ish type
Dimension = namedtuple( 'Dimension', 'x y z')

##################
#  1____________
#  | 2________ |
#  | |       | |
#  | |_______| |
#  | ____*____ |
#  | |       | |
#  | 3_______| |
#  4___________|
#
# ____ or | for inner box is size
#
# 1 -> offset (assuming * as center)
# 2 -> inset (assuming * as center)
# 1 to 4 -> base
# 2 to 3 -> repeatLength
#
##############

size = Dimension( 60, 50, 75 )
count = Dimension( 2, 3, 1 )
padding = 3 # this is dimensionless

base = Dimension._make( [c*s + (c + 1)*padding for s, c in zip( size, count ) ] )
offset = Dimension._make( [s/2 for s in size] )
globalOffset = Dimension._make( [(b-s-2*padding)/2 for s, b in zip(size, base)] )
repeatLength = Dimension._make( [b-s-2*padding for s, b in zip(size, base)] )

# setting up some standard vectors
zero_vector = App.Vector( 0, 0, 0 )
corner_offset_vector = App.Vector( globalOffset.x, globalOffset.y, 0 )
corner_offset_placement = App.Placement( corner_offset_vector, zero_vector, 0 )

### document setup ###

doc.Tip = doc.addObject('App::Part','Part')
doc.Part.Label = 'Scaffolding'
Gui.activateView('Gui::View3DInventor', True)
Gui.activeView().setActiveObject('part', doc.Part)

####################
### helper stuff ###
####################

def pairs(a):
  return zip(a, (a[1:] + a[:1]))

def ints(n):
  return [i for i in range(0, n)]

# creates a continuous polygon and adds coincident constraints
def wireUpVerts( sketch, verts ):
  geoList = []
  for a, b in pairs(verts):
    geoList.append( Part.LineSegment(a,b) )

  sketch.addGeometry(geoList,False)
  conList = []
  for a, b in pairs(ints(len(verts))):
    conList.append( Sketcher.Constraint('Coincident', a, 2, b, 1))

  sketch.addConstraint(conList)


def makeCopies( original, sketch, name ):
  transform = body.newObject('PartDesign::MultiTransform', name)
  transform.Originals = [original]
  transform.Shape = original.Shape

  transformations = []

  if count.x > 1:
    x_transform = body.newObject('PartDesign::LinearPattern', name+'X')
    x_transform.Direction = ( sketch, ['H_Axis'] )
    x_transform.Length = repeatLength.x
    x_transform.Reversed = 1
    x_transform.Occurrences = count.x
    transformations.append(x_transform)

  if count.y > 1:
    y_transform = body.newObject('PartDesign::LinearPattern', name+'Y')
    y_transform.Direction = ( sketch, ['V_Axis'] )
    y_transform.Length = repeatLength.y
    y_transform.Reversed = 1
    y_transform.Occurrences = count.y
    transformations.append(y_transform)

  # "install" the transformations
  transform.Transformations = transformations

  transform.Visibility = True

  return transform

############
### BODY ###
############

body = doc.addObject('PartDesign::Body','Scaffolding-2x3')

Gui.Selection.addSelection(body)
part = doc.Part.addObject(body)

################
### MAIN PAD ###
################

structure_sketch = body.newObject('Sketcher::SketchObject','StructureSketch')
structure_sketch.Support = (doc.getObject('XY_Plane001'),[''])
structure_sketch.MapMode = 'FlatFace'

vertX = App.Units.Quantity( f'{base.x}/2 mm' )
vertY = App.Units.Quantity( f'{base.y}/2 mm' )

verts = [
  App.Vector(-vertX,  vertY, 0),
  App.Vector( vertX,  vertY, 0),
  App.Vector( vertX, -vertY, 0),
  App.Vector(-vertX, -vertY, 0)
]

### draw ###
wireUpVerts( structure_sketch, verts )

### constraints ###
conList = []

conList.append(Sketcher.Constraint('Horizontal',2))
conList.append(Sketcher.Constraint('Vertical',3))

conList.append(Sketcher.Constraint( 'DistanceX', 0, 1, 0, 2, 2*vertX ))
conList.append(Sketcher.Constraint( 'DistanceY', 1, 1, 1, 2, 2*vertY ))

conList.append(Sketcher.Constraint( 'Symmetric', 0, 1, 0, 2, -2 ))
conList.append(Sketcher.Constraint( 'Symmetric', 1, 1, 1, 2, -1 ))

structure_sketch.addConstraint(conList)
del conList, verts

### pocket ###
structure_pad = body.newObject('PartDesign::Pad','MainStructure')
structure_pad.Profile = structure_sketch
structure_pad.Length = base.z
structure_pad.ReferenceAxis = (structure_sketch, ['N_Axis'])
structure_sketch.Visibility = False


###################
### DATUM PLANE ###
###################

box_plane = body.newObject('PartDesign::Plane', 'DatumPlane')
box_plane.Support = structure_pad
box_plane.MapMode = 'ObjectXY'
box_plane.Visibility = False

######################
### OCTOGON POCKET ###
######################

zone_sketch = body.newObject('Sketcher::SketchObject','ZoneSketch')
zone_sketch.Support = box_plane
zone_sketch.MapMode = 'FlatFace'

############## general shape
#    .____
#   /      \
#  |        |
#  |        |
#   \______/
# dot is first vertext in list

shortSize = 15

vertX = App.Units.Quantity( f'{offset.x} mm' )
vertXshort = App.Units.Quantity( f'({offset.x} - {shortSize}) mm' )
vertXcenter = App.Units.Quantity( f'({offset.x} - (1/sqrt(2))*{shortSize} * tan(radians(22.5)))/2 mm')

vertY = App.Units.Quantity( f'{offset.y} mm' )
vertYshort = App.Units.Quantity( f'({offset.y} - {shortSize}) mm' )
vertYcenter = App.Units.Quantity( f'({offset.y} - (1/sqrt(2))*{shortSize} * tan(radians(22.5)))/2 mm')

verts = [
  App.Vector( -vertXshort,  vertY,      0 ),
  App.Vector(  vertXshort,  vertY,      0 ),
  App.Vector(  vertX,       vertYshort, 0 ),
  App.Vector(  vertX,      -vertYshort, 0 ),
  App.Vector(  vertXshort, -vertY,      0 ),
  App.Vector( -vertXshort, -vertY,      0 ),
  App.Vector( -vertX,      -vertYshort, 0 ),
  App.Vector( -vertX,       vertYshort, 0 )
]

### draw octogon ###
wireUpVerts( zone_sketch, verts )

### constraints ###
conList = []

conList.append(Sketcher.Constraint('Horizontal',4))
conList.append(Sketcher.Constraint('Vertical',6))

conList.append(Sketcher.Constraint( 'DistanceX', 0, 1, 0, 2, 2*vertXshort ))
conList.append(Sketcher.Constraint( 'DistanceY', 2, 2, 2, 1, 2*vertYshort ))

conList.append(Sketcher.Constraint( 'DistanceX', 6, 2, 2, 1, 2*vertX ))
conList.append(Sketcher.Constraint( 'DistanceY', 4, 1, 0, 2, 2*vertY ))

conList.append(Sketcher.Constraint( 'Symmetric', 0, 1, 0, 2, -2 ))
conList.append(Sketcher.Constraint( 'Symmetric', 2, 1, 2, 2, -1 ))
conList.append(Sketcher.Constraint( 'Symmetric', 0, 1, 4, 2, -1 ))
conList.append(Sketcher.Constraint( 'Symmetric', 2, 1, 6, 2, -2 ))

conList.append(Sketcher.Constraint('Equal', 0, 4))
conList.append(Sketcher.Constraint('Equal', 2, 6))

zone_sketch.addConstraint(conList)
del verts, conList

### draw circles ###
zone_sketch.addGeometry( Part.Circle( App.Vector( -vertXinset,  vertYinset, 0), App.Vector(0,0,1), 3 ), False)
zone_sketch.addGeometry( Part.Circle( App.Vector(  vertXinset,  vertYinset, 0), App.Vector(0,0,1), 3 ), False)
zone_sketch.addGeometry( Part.Circle( App.Vector(  vertXinset, -vertYinset, 0), App.Vector(0,0,1), 3 ), False)
zone_sketch.addGeometry( Part.Circle( App.Vector( -vertXinset, -vertYinset, 0), App.Vector(0,0,1), 3 ), False)

### circle constaints ###
zone_sketch.addConstraint(Sketcher.Constraint('Radius', 8, 3))
zone_sketch.addConstraint(Sketcher.Constraint('Radius', 9, 3))
zone_sketch.addConstraint(Sketcher.Constraint('Radius',10, 3))
zone_sketch.addConstraint(Sketcher.Constraint('Radius',11, 3))

### pocket ###
zone_sketch.AttachmentOffset = corner_offset_placement

center_pocket = body.newObject('PartDesign::Pocket','CenterPocket')
center_pocket.Profile = zone_sketch
center_pocket.Length = base.z
center_pocket.Reversed = 1
center_pocket.ReferenceAxis = (zone_sketch, ['N_Axis'])
zone_sketch.Visibility = False

### copies ###
makeCopies( center_pocket, zone_sketch, 'CenterPocketTransform' )

#####################
### SQUARE POCKET ###
#####################

zone_fill_sketch = body.newObject('Sketcher::SketchObject','ZoneFillSketch')
zone_fill_sketch.Support = box_plane
zone_fill_sketch.MapMode = 'FlatFace'

vertX = App.Units.Quantity( f'{offset.x} mm' )
vertY = App.Units.Quantity( f'{offset.y} mm' )

verts = [
  App.Vector( -vertX,  vertY, 0 ),
  App.Vector(  vertX,  vertY, 0 ),
  App.Vector(  vertX, -vertY, 0 ),
  App.Vector( -vertX, -vertY, 0 )
]

### draw ###
wireUpVerts( zone_fill_sketch, verts )

### constraints ###
conList = []

conList.append(Sketcher.Constraint( 'DistanceX', 0, 1, 0, 2, 2*vertX ))
conList.append(Sketcher.Constraint( 'DistanceY', 1, 2, 1, 1, 2*vertY ))

conList.append(Sketcher.Constraint( 'Symmetric', 0, 1, 0, 2, -2 ))
conList.append(Sketcher.Constraint( 'Symmetric', 1, 1, 1, 2, -1 ))

conList.append(Sketcher.Constraint('Equal', 0, 2))
conList.append(Sketcher.Constraint('Equal', 1, 3))

zone_fill_sketch.addConstraint(conList)
del verts, conList

### pocket ###
zone_fill_sketch.AttachmentOffset = corner_offset_placement

fill_pocket = body.newObject('PartDesign::Pocket','CenterFillPocket')
fill_pocket.Profile = zone_fill_sketch
fill_pocket.Length = base.z - padding
fill_pocket.Reversed = 1
fill_pocket.ReferenceAxis = (zone_fill_sketch, ['N_Axis'])
zone_fill_sketch.Visibility = False

### copies ###
transform = makeCopies( fill_pocket, zone_fill_sketch, 'CenterFillTransform' )

doc.recompute()
Gui.Selection.addSelection(transform)
