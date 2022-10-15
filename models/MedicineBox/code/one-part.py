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

# get document above?

# add part
doc = App.newDocument('GeneratedBox')

# some general variables
baseX = 60
baseY = 50
baseZ = 75

xCount = 2
yCount = 3

zero_vector = App.Vector( 0, 0, 0 )
corner_offset_vector = App.Vector( baseX*(xCount-1)/2 + 1, baseY*(yCount-1)/2 + 1, 0 )
corner_offset_placement = App.Placement( corner_offset_vector, zero_vector, 0 )

doc.Tip = doc.addObject('App::Part','Part')
doc.Part.Label = 'Scaffolding'
Gui.activateView('Gui::View3DInventor', True)
Gui.activeView().setActiveObject('part', doc.Part)

### helper stuff ###
def pairs(a):
  return zip(a, (a[1:] + a[:1]))

def ints(n):
  return [i for i in range(0, n)]

def makeCopies( original, sketch, name ):
  transform = body.newObject('PartDesign::MultiTransform', name)
  transform.Originals = [original]
  transform.Shape = original.Shape

  x_transform = body.newObject('PartDesign::LinearPattern', name+'X')
  x_transform.Direction = ( sketch, ['H_Axis'] )
  x_transform.Length = baseX*(xCount-1) + xCount # small padding?
  x_transform.Reversed = 1
  x_transform.Occurrences = xCount

  y_transform = body.newObject('PartDesign::LinearPattern', name+'Y')
  y_transform.Direction = ( sketch, ['V_Axis'] )
  y_transform.Length = baseY*(yCount-1) + yCount # small padding?
  y_transform.Reversed = 1
  y_transform.Occurrences = yCount

  # "install" the transformations
  transform.Transformations = [x_transform, y_transform]

  transform.Visibility = True

  return transform


# add body
body = doc.addObject('PartDesign::Body','Scaffolding-2x3')

# ???
Gui.Selection.addSelection(body)
part = doc.Part.addObject(body)

### make a sketch for the main structure ###
structure_sketch = body.newObject('Sketcher::SketchObject','StructureSketch')
structure_sketch.Support = (doc.getObject('XY_Plane001'),[''])
structure_sketch.MapMode = 'FlatFace'

vertX = App.Units.Quantity( f'{baseX+2}*{xCount}/2 mm' )
vertY = App.Units.Quantity( f'{baseY+2}*{yCount}/2 mm' )

verts = [
  App.Vector(-vertX,  vertY, 0),
  App.Vector( vertX,  vertY, 0),
  App.Vector( vertX, -vertY, 0),
  App.Vector(-vertX, -vertY, 0)
]

geoList = []

# wire up all the pairs
for a, b in pairs(verts):
  geoList.append( Part.LineSegment(a,b) )

structure_sketch.addGeometry(geoList,False)

conList = []

# make sure the points are all connected
for a, b in pairs(ints(len(verts))):
  conList.append( Sketcher.Constraint('Coincident', a, 2, b, 1))

conList.append(Sketcher.Constraint('Horizontal',2))
conList.append(Sketcher.Constraint('Vertical',3))

conList.append(Sketcher.Constraint( 'DistanceX', 0, 1, 0, 2, 2*vertX ))
conList.append(Sketcher.Constraint( 'DistanceY', 1, 1, 1, 2, 2*vertY ))

conList.append(Sketcher.Constraint( 'Symmetric', 0, 1, 0, 2, -2 ))
conList.append(Sketcher.Constraint( 'Symmetric', 1, 1, 1, 2, -1 ))

structure_sketch.addConstraint(conList)
del geoList, conList

# pocket!
structure_pad = body.newObject('PartDesign::Pad','MainStructure')
structure_pad.Profile = structure_sketch
structure_pad.Length = baseZ
structure_pad.ReferenceAxis = (structure_sketch, ['N_Axis'])
structure_sketch.Visibility = False

### dataum plane ###

box_plane = body.newObject('PartDesign::Plane', 'DatumPlane')
box_plane.Support = structure_pad
box_plane.MapMode = 'ObjectXY'
box_plane.Visibility = False

### make the individual zones

zone_sketch = body.newObject('Sketcher::SketchObject','ZoneSketch')
zone_sketch.Support = box_plane
zone_sketch.MapMode = 'FlatFace'

vertX = App.Units.Quantity( f'{baseX}/2 mm' )
vertXshort = App.Units.Quantity( f'{baseX}/2 - 10 mm' )
vertXinset = App.Units.Quantity( f'{baseX}/2 - 3 mm' )

vertY = App.Units.Quantity( f'{baseY}/2 mm' )
vertYshort = App.Units.Quantity( f'{baseY}/2 - 10 mm' )
vertYinset = App.Units.Quantity( f'{baseY}/2 - 3 mm' )

############## general shape
#    .____
#   /      \
#  |        |
#  |        |
#   \______/
# dot is first vertext in list

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

geoList = []
# wire up all the pairs
for a, b in pairs(verts):
  geoList.append( Part.LineSegment(a,b) )

zone_sketch.addGeometry(geoList,False)

conList = []

# make sure all the points are connected
for a, b in pairs(ints(len(verts))):
  conList.append( Sketcher.Constraint('Coincident', a, 2, b, 1))

# conList.append(Sketcher.Constraint('Horizontal',0))
conList.append(Sketcher.Constraint('Horizontal',4))
# conList.append(Sketcher.Constraint('Vertical',2))
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
del geoList, conList

# # but wait, there's more! (circles in the corners)
zone_sketch.addGeometry( Part.Circle( App.Vector( -vertXinset,  vertYinset, 0), App.Vector(0,0,1), 2.5 ), False)
zone_sketch.addGeometry( Part.Circle( App.Vector(  vertXinset,  vertYinset, 0), App.Vector(0,0,1), 2.5 ), False)
zone_sketch.addGeometry( Part.Circle( App.Vector(  vertXinset, -vertYinset, 0), App.Vector(0,0,1), 2.5 ), False)
zone_sketch.addGeometry( Part.Circle( App.Vector( -vertXinset, -vertYinset, 0), App.Vector(0,0,1), 2.5 ), False)

zone_sketch.addConstraint(Sketcher.Constraint('Radius', 8, 2.5))
zone_sketch.addConstraint(Sketcher.Constraint('Radius', 9, 2.5))
zone_sketch.addConstraint(Sketcher.Constraint('Radius',10, 2.5))
zone_sketch.addConstraint(Sketcher.Constraint('Radius',11, 2.5))

# pocket!
zone_sketch.AttachmentOffset = corner_offset_placement

center_pocket = body.newObject('PartDesign::Pocket','CenterPocket')
center_pocket.Profile = zone_sketch
center_pocket.Length = baseZ
center_pocket.Reversed = 1
center_pocket.ReferenceAxis = (zone_sketch, ['N_Axis'])
zone_sketch.Visibility = False

# making copies
makeCopies( center_pocket, zone_sketch, 'CenterPocketTransform' )

# remaining cavity

zone_fill_sketch = body.newObject('Sketcher::SketchObject','ZoneFillSketch')
zone_fill_sketch.Support = box_plane
zone_fill_sketch.MapMode = 'FlatFace'

vertX = App.Units.Quantity( f'{baseX}/2 mm' )
vertY = App.Units.Quantity( f'{baseY}/2 mm' )

verts = [
  App.Vector( -vertX,  vertY, 0 ),
  App.Vector(  vertX,  vertY, 0 ),
  App.Vector(  vertX, -vertY, 0 ),
  App.Vector( -vertX, -vertY, 0 )
]

geoList = []
# wire up all the pairs
for a, b in pairs(verts):
  geoList.append( Part.LineSegment(a,b) )

zone_fill_sketch.addGeometry(geoList,False)

conList = []

# make sure all the points are connected
for a, b in pairs(ints(len(verts))):
  conList.append( Sketcher.Constraint('Coincident', a, 2, b, 1))

conList.append(Sketcher.Constraint( 'DistanceX', 0, 1, 0, 2, 2*vertX ))
conList.append(Sketcher.Constraint( 'DistanceY', 1, 2, 1, 1, 2*vertY ))

conList.append(Sketcher.Constraint( 'Symmetric', 0, 1, 0, 2, -2 ))
conList.append(Sketcher.Constraint( 'Symmetric', 1, 1, 1, 2, -1 ))

conList.append(Sketcher.Constraint('Equal', 0, 2))
conList.append(Sketcher.Constraint('Equal', 1, 3))

zone_fill_sketch.addConstraint(conList)
del geoList, conList

# pocket!
zone_fill_sketch.AttachmentOffset = corner_offset_placement

fill_pocket = body.newObject('PartDesign::Pocket','CenterFillPocket')
fill_pocket.Profile = zone_fill_sketch
fill_pocket.Length = baseZ - 2
fill_pocket.Reversed = 1
fill_pocket.ReferenceAxis = (zone_fill_sketch, ['N_Axis'])
zone_fill_sketch.Visibility = False

makeCopies( fill_pocket, zone_fill_sketch, 'CenterFillTransform' )

doc.recompute()
