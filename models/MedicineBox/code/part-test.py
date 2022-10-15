Python 3.9.13 | packaged by conda-forge | (main, May 27 2022, 17:07:35)
[Clang 13.0.1 ] on darwin
Type 'help', 'copyright', 'credits' or 'license' for more information.
>>> Gui.runCommand('Std_Workbench',19)
>>> Gui.runCommand('Std_ViewStatusBar',1)
>>> ### Begin command Std_Open
>>> FreeCAD.openDocument('/Users/ebaur/Library/Mobile Documents/com~apple~CloudDocs/Crafts/designs/models/MedicineBox/MedicineBox.FCStd')
>>> # App.setActiveDocument("MedicineBox")
>>> # App.ActiveDocument=App.getDocument("MedicineBox")
>>> # Gui.ActiveDocument=Gui.getDocument("MedicineBox")
>>> ### End command Std_Open
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Pocket006.')
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.')
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch015.')
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Pocket006.')
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.DatumPlane005.')
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch013.')
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.DatumPlane005.')
>>> Gui.runCommand('Std_ToggleVisibility',0)
>>> Gui.runCommand('Std_ToggleVisibility',0)
>>> Gui.runCommand('Std_ToggleVisibility',0)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch013.')
>>> # Gui.Selection.clearSelection()
>>> import Show
>>> ActiveSketch = App.getDocument('MedicineBox').getObject('Sketch013')
>>> tv = Show.TempoVis(App.ActiveDocument, tag= ActiveSketch.ViewObject.TypeId)
>>> ActiveSketch.ViewObject.TempoVis = tv
>>> if ActiveSketch.ViewObject.EditingWorkbench:
>>>   tv.activateWorkbench(ActiveSketch.ViewObject.EditingWorkbench)
>>> if ActiveSketch.ViewObject.HideDependent:
>>>   tv.hide(tv.get_all_dependent(App.getDocument('MedicineBox').getObject('Part001'), 'Body003.Sketch013.'))
>>> if ActiveSketch.ViewObject.ShowSupport:
>>>   tv.show([ref[0] for ref in ActiveSketch.Support if not ref[0].isDerivedFrom("PartDesign::Plane")])
>>> if ActiveSketch.ViewObject.ShowLinks:
>>>   tv.show([ref[0] for ref in ActiveSketch.ExternalGeometry])
>>> tv.sketchClipPlane(ActiveSketch, ActiveSketch.ViewObject.SectionView)
>>> tv.hide(ActiveSketch)
>>> del(tv)
>>> del(ActiveSketch)
>>>
>>> ActiveSketch = App.getDocument('MedicineBox').getObject('Sketch013')
>>> if ActiveSketch.ViewObject.RestoreCamera:
>>>   ActiveSketch.ViewObject.TempoVis.saveCamera()
>>>   if ActiveSketch.ViewObject.ForceOrtho:
>>>     ActiveSketch.ViewObject.Document.ActiveView.setCameraType('Orthographic')
>>>
>>> Gui.getDocument('MedicineBox').resetEdit()
>>> App.ActiveDocument.recompute()
>>> ActiveSketch = App.getDocument('MedicineBox').getObject('Sketch013')
>>> tv = ActiveSketch.ViewObject.TempoVis
>>> if tv:
>>>   tv.restore()
>>> ActiveSketch.ViewObject.TempoVis = None
>>> del(tv)
>>> del(ActiveSketch)
>>>
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch013.')
>>> App.getDocument('MedicineBox').recompute()
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Pocket006.')
>>> ### Begin command Std_Workbench
>>> Gui.activateWorkbench("PartDesignWorkbench")
>>> ### End command Std_Workbench
>>> Gui.runCommand('PartDesign_MultiTransform',0)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.')
>>> Gui.ActiveDocument.ActiveView.setActiveObject('part',App.getDocument('MedicineBox').getObject('Part001'))
>>> Gui.ActiveDocument.ActiveView.setActiveObject('pdbody',App.getDocument('MedicineBox').getObject('Body003'))
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Pocket006.')
>>> ### Begin command PartDesign_MultiTransform
>>> App.getDocument('MedicineBox').getObject('Body003').newObject('PartDesign::MultiTransform','MultiTransform002')
>>> App.ActiveDocument.recompute()
>>> App.getDocument('MedicineBox').getObject('MultiTransform002').Originals = [App.getDocument('MedicineBox').getObject('Pocket006'),]
>>> App.getDocument('MedicineBox').getObject('MultiTransform002').Shape = App.getDocument('MedicineBox').getObject('Pocket006').Shape
>>> App.ActiveDocument.recompute()
>>> App.getDocument('MedicineBox').getObject('MultiTransform002').ViewObject.ShapeColor=getattr(App.getDocument('MedicineBox').getObject('Pocket006').getLinkedObject(True).ViewObject,'ShapeColor',App.getDocument('MedicineBox').getObject('MultiTransform002').ViewObject.ShapeColor)
>>> App.getDocument('MedicineBox').getObject('MultiTransform002').ViewObject.LineColor=getattr(App.getDocument('MedicineBox').getObject('Pocket006').getLinkedObject(True).ViewObject,'LineColor',App.getDocument('MedicineBox').getObject('MultiTransform002').ViewObject.LineColor)
>>> App.getDocument('MedicineBox').getObject('MultiTransform002').ViewObject.PointColor=getattr(App.getDocument('MedicineBox').getObject('Pocket006').getLinkedObject(True).ViewObject,'PointColor',App.getDocument('MedicineBox').getObject('MultiTransform002').ViewObject.PointColor)
>>> App.getDocument('MedicineBox').getObject('MultiTransform002').ViewObject.Transparency=getattr(App.getDocument('MedicineBox').getObject('Pocket006').getLinkedObject(True).ViewObject,'Transparency',App.getDocument('MedicineBox').getObject('MultiTransform002').ViewObject.Transparency)
>>> App.getDocument('MedicineBox').getObject('MultiTransform002').ViewObject.DisplayMode=getattr(App.getDocument('MedicineBox').getObject('Pocket006').getLinkedObject(True).ViewObject,'DisplayMode',App.getDocument('MedicineBox').getObject('MultiTransform002').ViewObject.DisplayMode)
>>> Gui.getDocument('MedicineBox').setEdit(App.getDocument('MedicineBox').getObject('Part001'), 0, 'Body003.MultiTransform002.')
>>> Gui.Selection.clearSelection()
>>> App.getDocument('MedicineBox').getObject('Body003').Tip = App.getDocument('MedicineBox').getObject('MultiTransform002')
>>> App.ActiveDocument.recompute()
>>> ### End command PartDesign_MultiTransform
>>> # Gui.Selection.clearSelection()
>>> App.getDocument('MedicineBox').getObject('Body003').newObject('PartDesign::Mirrored','Mirrored004')
>>> App.getDocument('MedicineBox').getObject('Mirrored004').MirrorPlane = (App.getDocument('MedicineBox').getObject('Sketch012'),['V_Axis'])
>>> App.getDocument('MedicineBox').getObject('Pocket006').Visibility = False
>>> App.getDocument('MedicineBox').getObject('Mirrored004').Visibility = False
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Origin005.YZ_Plane005.',0,-78,19.5884)
>>> App.getDocument('MedicineBox').getObject('MultiTransform002').Visibility = True
>>> App.getDocument('MedicineBox').getObject('MultiTransform002').Transformations = [App.getDocument('MedicineBox').getObject('Mirrored004'),]
>>> App.getDocument('MedicineBox').recompute()
>>> App.getDocument('MedicineBox').getObject('Pocket006').Visibility = False
>>> Gui.getDocument('MedicineBox').resetEdit()
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Pocket006.Sketch012.')
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.MultiTransform002.')
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch013.')
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.DatumPlane005.')
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch014.')
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch015.')
>>> ### Begin command Std_Delete
>>> App.getDocument('MedicineBox').removeObject('Sketch013')
>>> App.getDocument('MedicineBox').removeObject('DatumPlane005')
>>> App.getDocument('MedicineBox').removeObject('Sketch014')
>>> App.getDocument('MedicineBox').removeObject('Sketch015')
>>> App.getDocument('MedicineBox').recompute()
>>> ### End command Std_Delete
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.MultiTransform002.')
>>> ### Begin command Std_Delete
>>> App.getDocument('MedicineBox').removeObject("Mirrored004")
>>> App.getDocument('MedicineBox').getObject('Body003').removeObject(App.getDocument('MedicineBox').getObject('MultiTransform002'))
>>> App.getDocument('MedicineBox').removeObject('MultiTransform002')
>>> App.getDocument('MedicineBox').recompute()
>>> ### End command Std_Delete
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Pocket006.')
>>> ### Begin command PartDesign_MultiTransform
>>> App.getDocument('MedicineBox').getObject('Body003').newObject('PartDesign::MultiTransform','MultiTransform002')
>>> App.ActiveDocument.recompute()
>>> App.getDocument('MedicineBox').getObject('MultiTransform002').Originals = [App.getDocument('MedicineBox').getObject('Pocket006'),]
>>> App.getDocument('MedicineBox').getObject('MultiTransform002').Shape = App.getDocument('MedicineBox').getObject('Pocket006').Shape
>>> App.ActiveDocument.recompute()
>>> App.getDocument('MedicineBox').getObject('MultiTransform002').ViewObject.ShapeColor=getattr(App.getDocument('MedicineBox').getObject('Pocket006').getLinkedObject(True).ViewObject,'ShapeColor',App.getDocument('MedicineBox').getObject('MultiTransform002').ViewObject.ShapeColor)
>>> App.getDocument('MedicineBox').getObject('MultiTransform002').ViewObject.LineColor=getattr(App.getDocument('MedicineBox').getObject('Pocket006').getLinkedObject(True).ViewObject,'LineColor',App.getDocument('MedicineBox').getObject('MultiTransform002').ViewObject.LineColor)
>>> App.getDocument('MedicineBox').getObject('MultiTransform002').ViewObject.PointColor=getattr(App.getDocument('MedicineBox').getObject('Pocket006').getLinkedObject(True).ViewObject,'PointColor',App.getDocument('MedicineBox').getObject('MultiTransform002').ViewObject.PointColor)
>>> App.getDocument('MedicineBox').getObject('MultiTransform002').ViewObject.Transparency=getattr(App.getDocument('MedicineBox').getObject('Pocket006').getLinkedObject(True).ViewObject,'Transparency',App.getDocument('MedicineBox').getObject('MultiTransform002').ViewObject.Transparency)
>>> App.getDocument('MedicineBox').getObject('MultiTransform002').ViewObject.DisplayMode=getattr(App.getDocument('MedicineBox').getObject('Pocket006').getLinkedObject(True).ViewObject,'DisplayMode',App.getDocument('MedicineBox').getObject('MultiTransform002').ViewObject.DisplayMode)
>>> Gui.getDocument('MedicineBox').setEdit(App.getDocument('MedicineBox').getObject('Part001'), 0, 'Body003.MultiTransform002.')
>>> Gui.Selection.clearSelection()
>>> App.getDocument('MedicineBox').getObject('Body003').Tip = App.getDocument('MedicineBox').getObject('MultiTransform002')
>>> App.ActiveDocument.recompute()
>>> ### End command PartDesign_MultiTransform
>>> # Gui.Selection.clearSelection()
>>> App.getDocument('MedicineBox').getObject('Body003').newObject('PartDesign::Mirrored','Mirrored004')
>>> App.getDocument('MedicineBox').getObject('Mirrored004').MirrorPlane = (App.getDocument('MedicineBox').getObject('Sketch012'),['V_Axis'])
>>> App.getDocument('MedicineBox').getObject('Pocket006').Visibility = False
>>> App.getDocument('MedicineBox').getObject('Mirrored004').Visibility = False
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Origin005.XZ_Plane005.',34.944,7.7486e-06,-65)
>>> App.getDocument('MedicineBox').getObject('MultiTransform002').Visibility = True
>>> App.getDocument('MedicineBox').getObject('Body003').newObject('PartDesign::Mirrored','Mirrored005')
>>> App.getDocument('MedicineBox').getObject('Mirrored005').MirrorPlane = (App.getDocument('MedicineBox').getObject('Sketch012'),['V_Axis'])
>>> App.getDocument('MedicineBox').getObject('Mirrored005').Visibility = False
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Origin005.YZ_Plane005.',0,-78,23.9468)
>>> App.getDocument('MedicineBox').getObject('MultiTransform002').Visibility = True
>>> App.getDocument('MedicineBox').getObject('MultiTransform002').Transformations = [App.getDocument('MedicineBox').getObject('Mirrored004'),App.getDocument('MedicineBox').getObject('Mirrored005'),]
>>> App.getDocument('MedicineBox').recompute()
>>> App.getDocument('MedicineBox').getObject('Pocket006').Visibility = False
>>> Gui.getDocument('MedicineBox').resetEdit()
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.MultiTransform002.')
>>> ### Begin command Std_Delete
>>> App.getDocument('MedicineBox').removeObject("Mirrored004")
>>> App.getDocument('MedicineBox').removeObject("Mirrored005")
>>> App.getDocument('MedicineBox').getObject('Body003').removeObject(App.getDocument('MedicineBox').getObject('MultiTransform002'))
>>> App.getDocument('MedicineBox').removeObject('MultiTransform002')
>>> App.getDocument('MedicineBox').recompute()
>>> ### End command Std_Delete
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Pocket006.')
>>> ### Begin command Std_Delete
>>> App.getDocument('MedicineBox').getObject('Body003').removeObject(App.getDocument('MedicineBox').getObject('Pocket006'))
>>> App.getDocument('MedicineBox').removeObject('Pocket006')
>>> App.getDocument('MedicineBox').recompute()
>>> ### End command Std_Delete
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch012.')
>>> # Gui.Selection.clearSelection()
>>> ActiveSketch = App.getDocument('MedicineBox').getObject('Sketch012')
>>> tv = Show.TempoVis(App.ActiveDocument, tag= ActiveSketch.ViewObject.TypeId)
>>> ActiveSketch.ViewObject.TempoVis = tv
>>> if ActiveSketch.ViewObject.EditingWorkbench:
>>>   tv.activateWorkbench(ActiveSketch.ViewObject.EditingWorkbench)
>>> if ActiveSketch.ViewObject.HideDependent:
>>>   tv.hide(tv.get_all_dependent(App.getDocument('MedicineBox').getObject('Part001'), 'Body003.Sketch012.'))
>>> if ActiveSketch.ViewObject.ShowSupport:
>>>   tv.show([ref[0] for ref in ActiveSketch.Support if not ref[0].isDerivedFrom("PartDesign::Plane")])
>>> if ActiveSketch.ViewObject.ShowLinks:
>>>   tv.show([ref[0] for ref in ActiveSketch.ExternalGeometry])
>>> tv.sketchClipPlane(ActiveSketch, ActiveSketch.ViewObject.SectionView)
>>> tv.hide(ActiveSketch)
>>> del(tv)
>>> del(ActiveSketch)
>>>
>>> import PartDesignGui
>>> ActiveSketch = App.getDocument('MedicineBox').getObject('Sketch012')
>>> if ActiveSketch.ViewObject.RestoreCamera:
>>>   ActiveSketch.ViewObject.TempoVis.saveCamera()
>>>   if ActiveSketch.ViewObject.ForceOrtho:
>>>     ActiveSketch.ViewObject.Document.ActiveView.setCameraType('Orthographic')
>>>
>>> Gui.getDocument('MedicineBox').resetEdit()
>>> App.ActiveDocument.recompute()
>>> ActiveSketch = App.getDocument('MedicineBox').getObject('Sketch012')
>>> tv = ActiveSketch.ViewObject.TempoVis
>>> if tv:
>>>   tv.restore()
>>> ActiveSketch.ViewObject.TempoVis = None
>>> del(tv)
>>> del(ActiveSketch)
>>>
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch012.')
>>> App.getDocument('MedicineBox').recompute()
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Origin005.')
>>> Gui.runCommand('Std_ToggleVisibility',0)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch012.')
>>> ### Begin command PartDesign_Pocket
>>> App.getDocument('MedicineBox').getObject('Body003').newObject('PartDesign::Pocket','Pocket006')
>>> App.getDocument('MedicineBox').getObject('Pocket006').Profile = App.getDocument('MedicineBox').getObject('Sketch012')
>>> App.getDocument('MedicineBox').getObject('Pocket006').Length = 5
>>> App.ActiveDocument.recompute()
>>> App.getDocument('MedicineBox').getObject('Pocket006').ReferenceAxis = (App.getDocument('MedicineBox').getObject('Sketch012'),['N_Axis'])
>>> App.getDocument('MedicineBox').getObject('Sketch012').Visibility = False
>>> App.ActiveDocument.recompute()
>>> App.getDocument('MedicineBox').getObject('Pocket006').ViewObject.ShapeColor=getattr(App.getDocument('MedicineBox').getObject('Pad005').getLinkedObject(True).ViewObject,'ShapeColor',App.getDocument('MedicineBox').getObject('Pocket006').ViewObject.ShapeColor)
>>> App.getDocument('MedicineBox').getObject('Pocket006').ViewObject.LineColor=getattr(App.getDocument('MedicineBox').getObject('Pad005').getLinkedObject(True).ViewObject,'LineColor',App.getDocument('MedicineBox').getObject('Pocket006').ViewObject.LineColor)
>>> App.getDocument('MedicineBox').getObject('Pocket006').ViewObject.PointColor=getattr(App.getDocument('MedicineBox').getObject('Pad005').getLinkedObject(True).ViewObject,'PointColor',App.getDocument('MedicineBox').getObject('Pocket006').ViewObject.PointColor)
>>> App.getDocument('MedicineBox').getObject('Pocket006').ViewObject.Transparency=getattr(App.getDocument('MedicineBox').getObject('Pad005').getLinkedObject(True).ViewObject,'Transparency',App.getDocument('MedicineBox').getObject('Pocket006').ViewObject.Transparency)
>>> App.getDocument('MedicineBox').getObject('Pocket006').ViewObject.DisplayMode=getattr(App.getDocument('MedicineBox').getObject('Pad005').getLinkedObject(True).ViewObject,'DisplayMode',App.getDocument('MedicineBox').getObject('Pocket006').ViewObject.DisplayMode)
>>> Gui.getDocument('MedicineBox').setEdit(App.getDocument('MedicineBox').getObject('Part001'), 0, 'Body003.Pocket006.')
>>> Gui.Selection.clearSelection()
>>> ### End command PartDesign_Pocket
>>> # Gui.Selection.clearSelection()
>>> App.getDocument('MedicineBox').getObject('Pocket006').Length = 5.000000
>>> App.getDocument('MedicineBox').getObject('Pocket006').Length2 = 5.000000
>>> App.getDocument('MedicineBox').getObject('Pocket006').TaperAngle = 0.000000
>>> App.getDocument('MedicineBox').getObject('Pocket006').TaperAngle2 = 0.000000
>>> App.getDocument('MedicineBox').getObject('Pocket006').UseCustomVector = 0
>>> App.getDocument('MedicineBox').getObject('Pocket006').Direction = (0, 0, -1)
>>> App.getDocument('MedicineBox').getObject('Pocket006').ReferenceAxis = (App.getDocument('MedicineBox').getObject('Sketch012'), ['N_Axis'])
>>> App.getDocument('MedicineBox').getObject('Pocket006').AlongSketchNormal = 1
>>> App.getDocument('MedicineBox').getObject('Pocket006').Type = 0
>>> App.getDocument('MedicineBox').getObject('Pocket006').UpToFace = None
>>> App.getDocument('MedicineBox').getObject('Pocket006').Reversed = 0
>>> App.getDocument('MedicineBox').getObject('Pocket006').Midplane = 0
>>> App.getDocument('MedicineBox').getObject('Pocket006').Offset = 0
>>> App.getDocument('MedicineBox').recompute()
>>> App.getDocument('MedicineBox').getObject('Pad005').Visibility = False
>>> Gui.getDocument('MedicineBox').resetEdit()
>>> App.getDocument('MedicineBox').getObject('Sketch012').Visibility = False
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Pocket006.')
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Pocket006.')
>>> ### Begin command PartDesign_MultiTransform
>>> App.getDocument('MedicineBox').getObject('Body003').newObject('PartDesign::MultiTransform','MultiTransform002')
>>> App.ActiveDocument.recompute()
>>> App.getDocument('MedicineBox').getObject('MultiTransform002').Originals = [App.getDocument('MedicineBox').getObject('Pocket006'),]
>>> App.getDocument('MedicineBox').getObject('MultiTransform002').Shape = App.getDocument('MedicineBox').getObject('Pocket006').Shape
>>> App.ActiveDocument.recompute()
>>> App.getDocument('MedicineBox').getObject('MultiTransform002').ViewObject.ShapeColor=getattr(App.getDocument('MedicineBox').getObject('Pocket006').getLinkedObject(True).ViewObject,'ShapeColor',App.getDocument('MedicineBox').getObject('MultiTransform002').ViewObject.ShapeColor)
>>> App.getDocument('MedicineBox').getObject('MultiTransform002').ViewObject.LineColor=getattr(App.getDocument('MedicineBox').getObject('Pocket006').getLinkedObject(True).ViewObject,'LineColor',App.getDocument('MedicineBox').getObject('MultiTransform002').ViewObject.LineColor)
>>> App.getDocument('MedicineBox').getObject('MultiTransform002').ViewObject.PointColor=getattr(App.getDocument('MedicineBox').getObject('Pocket006').getLinkedObject(True).ViewObject,'PointColor',App.getDocument('MedicineBox').getObject('MultiTransform002').ViewObject.PointColor)
>>> App.getDocument('MedicineBox').getObject('MultiTransform002').ViewObject.Transparency=getattr(App.getDocument('MedicineBox').getObject('Pocket006').getLinkedObject(True).ViewObject,'Transparency',App.getDocument('MedicineBox').getObject('MultiTransform002').ViewObject.Transparency)
>>> App.getDocument('MedicineBox').getObject('MultiTransform002').ViewObject.DisplayMode=getattr(App.getDocument('MedicineBox').getObject('Pocket006').getLinkedObject(True).ViewObject,'DisplayMode',App.getDocument('MedicineBox').getObject('MultiTransform002').ViewObject.DisplayMode)
>>> Gui.getDocument('MedicineBox').setEdit(App.getDocument('MedicineBox').getObject('Part001'), 0, 'Body003.MultiTransform002.')
>>> Gui.Selection.clearSelection()
>>> App.getDocument('MedicineBox').getObject('Body003').Tip = App.getDocument('MedicineBox').getObject('MultiTransform002')
>>> App.ActiveDocument.recompute()
>>> ### End command PartDesign_MultiTransform
>>> # Gui.Selection.clearSelection()
>>> App.getDocument('MedicineBox').getObject('Body003').newObject('PartDesign::Mirrored','Mirrored004')
>>> App.getDocument('MedicineBox').getObject('Mirrored004').MirrorPlane = (App.getDocument('MedicineBox').getObject('Sketch012'),['V_Axis'])
>>> App.getDocument('MedicineBox').getObject('Pocket006').Visibility = False
>>> App.getDocument('MedicineBox').getObject('Mirrored004').Visibility = False
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Origin005.XZ_Plane005.',-58.7135,-6.97476e-06,58.5085)
>>> App.getDocument('MedicineBox').getObject('MultiTransform002').Visibility = True
>>> App.getDocument('MedicineBox').getObject('Body003').newObject('PartDesign::Mirrored','Mirrored005')
>>> App.getDocument('MedicineBox').getObject('Mirrored005').MirrorPlane = (App.getDocument('MedicineBox').getObject('Sketch012'),['V_Axis'])
>>> App.getDocument('MedicineBox').getObject('Mirrored005').Visibility = False
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Origin005.YZ_Plane005.',0,-66.7909,73.2237)
>>> App.getDocument('MedicineBox').getObject('MultiTransform002').Visibility = True
>>> App.getDocument('MedicineBox').getObject('MultiTransform002').Transformations = [App.getDocument('MedicineBox').getObject('Mirrored004'),App.getDocument('MedicineBox').getObject('Mirrored005'),]
>>> App.getDocument('MedicineBox').recompute()
>>> App.getDocument('MedicineBox').getObject('Pocket006').Visibility = False
>>> Gui.getDocument('MedicineBox').resetEdit()
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.MultiTransform002.')
>>> ### Begin command Std_Delete
>>> App.getDocument('MedicineBox').removeObject("Mirrored004")
>>> App.getDocument('MedicineBox').removeObject("Mirrored005")
>>> App.getDocument('MedicineBox').getObject('Body003').removeObject(App.getDocument('MedicineBox').getObject('MultiTransform002'))
>>> App.getDocument('MedicineBox').removeObject('MultiTransform002')
>>> App.getDocument('MedicineBox').recompute()
>>> ### End command Std_Delete
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Pad005.Sketch011.')
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Pocket006.')
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Pocket006.Sketch012.')
>>> FreeCAD.getDocument('MedicineBox').getObject('Sketch012').AttachmentOffset = App.Placement(App.Vector(0.00,-30.00,0.00),App.Rotation(App.Vector(0.00,0.00,1.00),0.00))
>>>
>>> FreeCAD.getDocument('MedicineBox').getObject('Sketch012').AttachmentOffset = App.Placement(App.Vector(0.00,0.00,0.00),App.Rotation(App.Vector(0.00,0.00,1.00),0.00))
>>>
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Pocket006.')
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Pocket006.')
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Pocket006.Sketch012.')
>>> Gui.runCommand('Std_Undo',0)
>>> Gui.runCommand('Std_Undo',0)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Pocket006.Sketch012.')
>>> Gui.runCommand('PartDesign_MultiTransform',0)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Pocket006.')
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Pad005.Sketch011.')
>>> # Gui.Selection.clearSelection()
>>> ActiveSketch = App.getDocument('MedicineBox').getObject('Sketch011')
>>> tv = Show.TempoVis(App.ActiveDocument, tag= ActiveSketch.ViewObject.TypeId)
>>> ActiveSketch.ViewObject.TempoVis = tv
>>> if ActiveSketch.ViewObject.EditingWorkbench:
>>>   tv.activateWorkbench(ActiveSketch.ViewObject.EditingWorkbench)
>>> if ActiveSketch.ViewObject.HideDependent:
>>>   tv.hide(tv.get_all_dependent(App.getDocument('MedicineBox').getObject('Part001'), 'Body003.Pad005.Sketch011.'))
>>> if ActiveSketch.ViewObject.ShowSupport:
>>>   tv.show([ref[0] for ref in ActiveSketch.Support if not ref[0].isDerivedFrom("PartDesign::Plane")])
>>> if ActiveSketch.ViewObject.ShowLinks:
>>>   tv.show([ref[0] for ref in ActiveSketch.ExternalGeometry])
>>> tv.sketchClipPlane(ActiveSketch, ActiveSketch.ViewObject.SectionView)
>>> tv.hide(ActiveSketch)
>>> del(tv)
>>> del(ActiveSketch)
>>>
>>> import PartDesignGui
>>> ActiveSketch = App.getDocument('MedicineBox').getObject('Sketch011')
>>> if ActiveSketch.ViewObject.RestoreCamera:
>>>   ActiveSketch.ViewObject.TempoVis.saveCamera()
>>>   if ActiveSketch.ViewObject.ForceOrtho:
>>>     ActiveSketch.ViewObject.Document.ActiveView.setCameraType('Orthographic')
>>>
>>> Gui.getDocument('MedicineBox').resetEdit()
>>> App.ActiveDocument.recompute()
>>> ActiveSketch = App.getDocument('MedicineBox').getObject('Sketch011')
>>> tv = ActiveSketch.ViewObject.TempoVis
>>> if tv:
>>>   tv.restore()
>>> ActiveSketch.ViewObject.TempoVis = None
>>> del(tv)
>>> del(ActiveSketch)
>>>
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Pad005.Sketch011.')
>>> App.getDocument('MedicineBox').recompute()
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.DatumPlane004.')
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Pocket006.Sketch012.')
>>> # Gui.Selection.clearSelection()
>>> ActiveSketch = App.getDocument('MedicineBox').getObject('Sketch012')
>>> tv = Show.TempoVis(App.ActiveDocument, tag= ActiveSketch.ViewObject.TypeId)
>>> ActiveSketch.ViewObject.TempoVis = tv
>>> if ActiveSketch.ViewObject.EditingWorkbench:
>>>   tv.activateWorkbench(ActiveSketch.ViewObject.EditingWorkbench)
>>> if ActiveSketch.ViewObject.HideDependent:
>>>   tv.hide(tv.get_all_dependent(App.getDocument('MedicineBox').getObject('Part001'), 'Body003.Pocket006.Sketch012.'))
>>> if ActiveSketch.ViewObject.ShowSupport:
>>>   tv.show([ref[0] for ref in ActiveSketch.Support if not ref[0].isDerivedFrom("PartDesign::Plane")])
>>> if ActiveSketch.ViewObject.ShowLinks:
>>>   tv.show([ref[0] for ref in ActiveSketch.ExternalGeometry])
>>> tv.sketchClipPlane(ActiveSketch, ActiveSketch.ViewObject.SectionView)
>>> tv.hide(ActiveSketch)
>>> del(tv)
>>> del(ActiveSketch)
>>>
>>> import PartDesignGui
>>> ActiveSketch = App.getDocument('MedicineBox').getObject('Sketch012')
>>> if ActiveSketch.ViewObject.RestoreCamera:
>>>   ActiveSketch.ViewObject.TempoVis.saveCamera()
>>>   if ActiveSketch.ViewObject.ForceOrtho:
>>>     ActiveSketch.ViewObject.Document.ActiveView.setCameraType('Orthographic')
>>>
>>> Gui.getDocument('MedicineBox').resetEdit()
>>> App.ActiveDocument.recompute()
>>> ActiveSketch = App.getDocument('MedicineBox').getObject('Sketch012')
>>> tv = ActiveSketch.ViewObject.TempoVis
>>> if tv:
>>>   tv.restore()
>>> ActiveSketch.ViewObject.TempoVis = None
>>> del(tv)
>>> del(ActiveSketch)
>>>
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Pocket006.Sketch012.')
>>> App.getDocument('MedicineBox').recompute()
>>> Gui.runCommand('Std_Undo',0)
>>> Gui.runCommand('Std_Undo',0)
>>> Gui.runCommand('Std_Redo',0)
>>> Gui.runCommand('Std_Redo',0)
>>> FreeCAD.getDocument('MedicineBox').getObject('Sketch012').AttachmentOffset = App.Placement(App.Vector(0.00,-30.00,0.00),App.Rotation(App.Vector(0.00,0.00,1.00),0.00))
>>>
>>> FreeCAD.getDocument('MedicineBox').getObject('Sketch012').AttachmentOffset = App.Placement(App.Vector(0.00,0.00,0.00),App.Rotation(App.Vector(0.00,0.00,1.00),0.00))
>>>
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Pocket006.Sketch012.')
>>> # Gui.Selection.clearSelection()
>>> ActiveSketch = App.getDocument('MedicineBox').getObject('Sketch012')
>>> tv = Show.TempoVis(App.ActiveDocument, tag= ActiveSketch.ViewObject.TypeId)
>>> ActiveSketch.ViewObject.TempoVis = tv
>>> if ActiveSketch.ViewObject.EditingWorkbench:
>>>   tv.activateWorkbench(ActiveSketch.ViewObject.EditingWorkbench)
>>> if ActiveSketch.ViewObject.HideDependent:
>>>   tv.hide(tv.get_all_dependent(App.getDocument('MedicineBox').getObject('Part001'), 'Body003.Pocket006.Sketch012.'))
>>> if ActiveSketch.ViewObject.ShowSupport:
>>>   tv.show([ref[0] for ref in ActiveSketch.Support if not ref[0].isDerivedFrom("PartDesign::Plane")])
>>> if ActiveSketch.ViewObject.ShowLinks:
>>>   tv.show([ref[0] for ref in ActiveSketch.ExternalGeometry])
>>> tv.sketchClipPlane(ActiveSketch, ActiveSketch.ViewObject.SectionView)
>>> tv.hide(ActiveSketch)
>>> del(tv)
>>> del(ActiveSketch)
>>>
>>> import PartDesignGui
>>> ActiveSketch = App.getDocument('MedicineBox').getObject('Sketch012')
>>> if ActiveSketch.ViewObject.RestoreCamera:
>>>   ActiveSketch.ViewObject.TempoVis.saveCamera()
>>>   if ActiveSketch.ViewObject.ForceOrtho:
>>>     ActiveSketch.ViewObject.Document.ActiveView.setCameraType('Orthographic')
>>>
>>> Gui.getDocument('MedicineBox').resetEdit()
>>> App.ActiveDocument.recompute()
>>> ActiveSketch = App.getDocument('MedicineBox').getObject('Sketch012')
>>> tv = ActiveSketch.ViewObject.TempoVis
>>> if tv:
>>>   tv.restore()
>>> ActiveSketch.ViewObject.TempoVis = None
>>> del(tv)
>>> del(ActiveSketch)
>>>
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Pocket006.Sketch012.')
>>> App.getDocument('MedicineBox').recompute()
>>> Gui.runCommand('Std_Undo',0)
>>> Gui.runCommand('Std_Undo',0)
>>> Gui.runCommand('Std_Undo',0)
>>> Gui.runCommand('PartDesign_LinearPattern',0)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Pocket006.')
>>> ### Begin command PartDesign_LinearPattern
>>> App.getDocument('MedicineBox').getObject('Body003').newObject('PartDesign::LinearPattern','LinearPattern')
>>> App.ActiveDocument.recompute()
>>> App.getDocument('MedicineBox').getObject('LinearPattern').Originals = [App.getDocument('MedicineBox').getObject('Pocket006'),]
>>> App.getDocument('MedicineBox').getObject('LinearPattern').Direction = (App.getDocument('MedicineBox').getObject('Sketch012'), ['H_Axis'])
>>> App.getDocument('MedicineBox').getObject('LinearPattern').Length = 100
>>> App.getDocument('MedicineBox').getObject('LinearPattern').Occurrences = 2
>>> App.ActiveDocument.recompute()
>>> App.getDocument('MedicineBox').getObject('LinearPattern').ViewObject.ShapeColor=getattr(App.getDocument('MedicineBox').getObject('Pocket006').getLinkedObject(True).ViewObject,'ShapeColor',App.getDocument('MedicineBox').getObject('LinearPattern').ViewObject.ShapeColor)
>>> App.getDocument('MedicineBox').getObject('LinearPattern').ViewObject.LineColor=getattr(App.getDocument('MedicineBox').getObject('Pocket006').getLinkedObject(True).ViewObject,'LineColor',App.getDocument('MedicineBox').getObject('LinearPattern').ViewObject.LineColor)
>>> App.getDocument('MedicineBox').getObject('LinearPattern').ViewObject.PointColor=getattr(App.getDocument('MedicineBox').getObject('Pocket006').getLinkedObject(True).ViewObject,'PointColor',App.getDocument('MedicineBox').getObject('LinearPattern').ViewObject.PointColor)
>>> App.getDocument('MedicineBox').getObject('LinearPattern').ViewObject.Transparency=getattr(App.getDocument('MedicineBox').getObject('Pocket006').getLinkedObject(True).ViewObject,'Transparency',App.getDocument('MedicineBox').getObject('LinearPattern').ViewObject.Transparency)
>>> App.getDocument('MedicineBox').getObject('LinearPattern').ViewObject.DisplayMode=getattr(App.getDocument('MedicineBox').getObject('Pocket006').getLinkedObject(True).ViewObject,'DisplayMode',App.getDocument('MedicineBox').getObject('LinearPattern').ViewObject.DisplayMode)
>>> Gui.getDocument('MedicineBox').setEdit(App.getDocument('MedicineBox').getObject('Part001'), 0, 'Body003.LinearPattern.')
>>> Gui.Selection.clearSelection()
>>> App.getDocument('MedicineBox').getObject('Body003').Tip = App.getDocument('MedicineBox').getObject('LinearPattern')
>>> App.ActiveDocument.recompute()
>>> ### End command PartDesign_LinearPattern
>>> # Gui.Selection.clearSelection()
>>> App.getDocument('MedicineBox').getObject('LinearPattern').Visibility = True
>>> App.getDocument('MedicineBox').getObject('LinearPattern').Visibility = True
>>> App.getDocument('MedicineBox').getObject('LinearPattern').Visibility = True
>>> App.getDocument('MedicineBox').recompute()
>>> Gui.getDocument('MedicineBox').resetEdit()
>>> Gui.runCommand('PartDesign_Mirrored',0)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Pocket006.')
>>> ### Begin command PartDesign_Mirrored
>>> App.getDocument('MedicineBox').getObject('Body003').newObject('PartDesign::Mirrored','Mirrored004')
>>> App.ActiveDocument.recompute()
>>> App.getDocument('MedicineBox').getObject('Mirrored004').Originals = [App.getDocument('MedicineBox').getObject('Pocket006'),]
>>> App.getDocument('MedicineBox').getObject('Mirrored004').MirrorPlane = (App.getDocument('MedicineBox').getObject('Sketch012'), ['V_Axis'])
>>> App.ActiveDocument.recompute()
>>> App.getDocument('MedicineBox').getObject('Mirrored004').ViewObject.ShapeColor=getattr(App.getDocument('MedicineBox').getObject('Pocket006').getLinkedObject(True).ViewObject,'ShapeColor',App.getDocument('MedicineBox').getObject('Mirrored004').ViewObject.ShapeColor)
>>> App.getDocument('MedicineBox').getObject('Mirrored004').ViewObject.LineColor=getattr(App.getDocument('MedicineBox').getObject('Pocket006').getLinkedObject(True).ViewObject,'LineColor',App.getDocument('MedicineBox').getObject('Mirrored004').ViewObject.LineColor)
>>> App.getDocument('MedicineBox').getObject('Mirrored004').ViewObject.PointColor=getattr(App.getDocument('MedicineBox').getObject('Pocket006').getLinkedObject(True).ViewObject,'PointColor',App.getDocument('MedicineBox').getObject('Mirrored004').ViewObject.PointColor)
>>> App.getDocument('MedicineBox').getObject('Mirrored004').ViewObject.Transparency=getattr(App.getDocument('MedicineBox').getObject('Pocket006').getLinkedObject(True).ViewObject,'Transparency',App.getDocument('MedicineBox').getObject('Mirrored004').ViewObject.Transparency)
>>> App.getDocument('MedicineBox').getObject('Mirrored004').ViewObject.DisplayMode=getattr(App.getDocument('MedicineBox').getObject('Pocket006').getLinkedObject(True).ViewObject,'DisplayMode',App.getDocument('MedicineBox').getObject('Mirrored004').ViewObject.DisplayMode)
>>> Gui.getDocument('MedicineBox').setEdit(App.getDocument('MedicineBox').getObject('Part001'), 0, 'Body003.Mirrored004.')
>>> Gui.Selection.clearSelection()
>>> App.getDocument('MedicineBox').getObject('Body003').Tip = App.getDocument('MedicineBox').getObject('Mirrored004')
>>> App.ActiveDocument.recompute()
>>> ### End command PartDesign_Mirrored
>>> # Gui.Selection.clearSelection()
>>> App.getDocument('MedicineBox').getObject('Mirrored004').Visibility = True
>>> App.getDocument('MedicineBox').getObject('Mirrored004').Visibility = True
>>> App.getDocument('MedicineBox').getObject('Mirrored004').Visibility = True
>>> App.getDocument('MedicineBox').getObject('Mirrored004').Visibility = True
>>> App.getDocument('MedicineBox').getObject('Mirrored004').Visibility = True
>>> App.getDocument('MedicineBox').recompute()
>>> Gui.getDocument('MedicineBox').resetEdit()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Pocket006.')
>>> ### Begin command PartDesign_MultiTransform
>>> App.getDocument('MedicineBox').getObject('Body003').newObject('PartDesign::MultiTransform','MultiTransform002')
>>> App.ActiveDocument.recompute()
>>> App.getDocument('MedicineBox').getObject('MultiTransform002').Originals = [App.getDocument('MedicineBox').getObject('Pocket006'),]
>>> App.getDocument('MedicineBox').getObject('MultiTransform002').Shape = App.getDocument('MedicineBox').getObject('Pocket006').Shape
>>> App.ActiveDocument.recompute()
>>> App.getDocument('MedicineBox').getObject('MultiTransform002').ViewObject.ShapeColor=getattr(App.getDocument('MedicineBox').getObject('Pocket006').getLinkedObject(True).ViewObject,'ShapeColor',App.getDocument('MedicineBox').getObject('MultiTransform002').ViewObject.ShapeColor)
>>> App.getDocument('MedicineBox').getObject('MultiTransform002').ViewObject.LineColor=getattr(App.getDocument('MedicineBox').getObject('Pocket006').getLinkedObject(True).ViewObject,'LineColor',App.getDocument('MedicineBox').getObject('MultiTransform002').ViewObject.LineColor)
>>> App.getDocument('MedicineBox').getObject('MultiTransform002').ViewObject.PointColor=getattr(App.getDocument('MedicineBox').getObject('Pocket006').getLinkedObject(True).ViewObject,'PointColor',App.getDocument('MedicineBox').getObject('MultiTransform002').ViewObject.PointColor)
>>> App.getDocument('MedicineBox').getObject('MultiTransform002').ViewObject.Transparency=getattr(App.getDocument('MedicineBox').getObject('Pocket006').getLinkedObject(True).ViewObject,'Transparency',App.getDocument('MedicineBox').getObject('MultiTransform002').ViewObject.Transparency)
>>> App.getDocument('MedicineBox').getObject('MultiTransform002').ViewObject.DisplayMode=getattr(App.getDocument('MedicineBox').getObject('Pocket006').getLinkedObject(True).ViewObject,'DisplayMode',App.getDocument('MedicineBox').getObject('MultiTransform002').ViewObject.DisplayMode)
>>> Gui.getDocument('MedicineBox').setEdit(App.getDocument('MedicineBox').getObject('Part001'), 0, 'Body003.MultiTransform002.')
>>> Gui.Selection.clearSelection()
>>> App.getDocument('MedicineBox').getObject('Body003').Tip = App.getDocument('MedicineBox').getObject('MultiTransform002')
>>> App.ActiveDocument.recompute()
>>> ### End command PartDesign_MultiTransform
>>> # Gui.Selection.clearSelection()
>>> App.getDocument('MedicineBox').getObject('Body003').newObject('PartDesign::Mirrored','Mirrored004')
>>> App.getDocument('MedicineBox').getObject('Mirrored004').MirrorPlane = (App.getDocument('MedicineBox').getObject('Sketch012'),['V_Axis'])
>>> App.getDocument('MedicineBox').getObject('Pocket006').Visibility = False
>>> App.getDocument('MedicineBox').getObject('Mirrored004').Visibility = False
>>> App.getDocument('MedicineBox').getObject('MultiTransform002').Visibility = True
>>> App.getDocument('MedicineBox').getObject('MultiTransform002').Visibility = True
>>> App.getDocument('MedicineBox').getObject('Body003').newObject('PartDesign::Mirrored','Mirrored005')
>>> App.getDocument('MedicineBox').getObject('Mirrored005').MirrorPlane = (App.getDocument('MedicineBox').getObject('Sketch012'),['V_Axis'])
>>> App.getDocument('MedicineBox').getObject('Mirrored005').Visibility = False
>>> App.getDocument('MedicineBox').getObject('MultiTransform002').Visibility = True
>>> App.getDocument('MedicineBox').getObject('MultiTransform002').Transformations = [App.getDocument('MedicineBox').getObject('Mirrored004'),App.getDocument('MedicineBox').getObject('Mirrored005'),]
>>> App.getDocument('MedicineBox').recompute()
>>> App.getDocument('MedicineBox').getObject('Pocket006').Visibility = False
>>> Gui.getDocument('MedicineBox').resetEdit()
>>> App.getDocument('MedicineBox').getObject('MultiTransform002').Visibility = True
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Pocket006.')
>>> Gui.ActiveDocument.setEdit(App.getDocument('MedicineBox').getObject('Pocket006'), 0)
>>> # Gui.Selection.clearSelection()
>>> App.getDocument('MedicineBox').getObject('Pocket006').Length = 5.000000
>>> App.getDocument('MedicineBox').getObject('Pocket006').Length2 = 5.000000
>>> App.getDocument('MedicineBox').getObject('Pocket006').TaperAngle = 0.000000
>>> App.getDocument('MedicineBox').getObject('Pocket006').TaperAngle2 = 0.000000
>>> App.getDocument('MedicineBox').getObject('Pocket006').UseCustomVector = 0
>>> App.getDocument('MedicineBox').getObject('Pocket006').Direction = (0, 0, -1)
>>> App.getDocument('MedicineBox').getObject('Pocket006').ReferenceAxis = (App.getDocument('MedicineBox').getObject('Sketch012'), ['N_Axis'])
>>> App.getDocument('MedicineBox').getObject('Pocket006').AlongSketchNormal = 1
>>> App.getDocument('MedicineBox').getObject('Pocket006').Type = 1
>>> App.getDocument('MedicineBox').getObject('Pocket006').UpToFace = None
>>> App.getDocument('MedicineBox').getObject('Pocket006').Reversed = 0
>>> App.getDocument('MedicineBox').getObject('Pocket006').Midplane = 0
>>> App.getDocument('MedicineBox').getObject('Pocket006').Offset = 0
>>> App.getDocument('MedicineBox').recompute()
>>> App.getDocument('MedicineBox').getObject('Pad005').Visibility = False
>>> Gui.getDocument('MedicineBox').resetEdit()
>>> App.getDocument('MedicineBox').getObject('Sketch012').Visibility = False
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.MultiTransform002.')
>>> Gui.runCommand('Std_ToggleVisibility',0)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Origin005.')
>>> Gui.runCommand('Std_ToggleVisibility',0)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.MultiTransform002.Face4',1.7415,-51.3678,-3.55271e-15)
>>> ### Begin command PartDesign_Plane
>>> App.getDocument('MedicineBox').getObject('Body003').newObject('PartDesign::Plane','DatumPlane005')
>>> App.getDocument('MedicineBox').getObject('DatumPlane005').Support = [(App.getDocument('MedicineBox').getObject('MultiTransform002'),'Face4')]
>>> App.getDocument('MedicineBox').getObject('DatumPlane005').MapMode = 'FlatFace'
>>> App.activeDocument().recompute()
>>> Gui.getDocument('MedicineBox').setEdit(App.getDocument('MedicineBox').getObject('Part001'), 0, 'Body003.DatumPlane005.')
>>> import Show
>>> from Show.Containers import isAContainer
>>> _tv_DatumPlane005 = Show.TempoVis(App.ActiveDocument, tag= 'PartGui::TaskAttacher')
>>> tvObj = App.getDocument('MedicineBox').getObject('DatumPlane005')
>>> dep_features = _tv_DatumPlane005.get_all_dependent(App.getDocument('MedicineBox').getObject('Part001'), 'Body003.DatumPlane005.')
>>> dep_features = [o for o in dep_features if not isAContainer(o)]
>>> if tvObj.isDerivedFrom('PartDesign::CoordinateSystem'):
>>> 	visible_features = [feat for feat in tvObj.InList if feat.isDerivedFrom('PartDesign::FeaturePrimitive')]
>>> 	dep_features = [feat for feat in dep_features if feat not in visible_features]
>>> 	del(visible_features)
>>> _tv_DatumPlane005.hide(dep_features)
>>> del(dep_features)
>>> if not tvObj.isDerivedFrom('PartDesign::CoordinateSystem'):
>>> 		if len(tvObj.Support) > 0:
>>> 			_tv_DatumPlane005.show([lnk[0] for lnk in tvObj.Support])
>>> del(tvObj)
>>> ### End command PartDesign_Plane
>>> # Gui.Selection.clearSelection()
>>> App.getDocument('MedicineBox').getObject('DatumPlane005').AttachmentOffset = App.Placement(App.Vector(0.0000000000, 0.0000000000, 0.0000000000),  App.Rotation(0.0000000000, 0.0000000000, 0.0000000000))
>>> App.getDocument('MedicineBox').getObject('DatumPlane005').MapReversed = False
>>> App.getDocument('MedicineBox').getObject('DatumPlane005').Support = [(App.getDocument('MedicineBox').getObject('MultiTransform002'),'Face4')]
>>> App.getDocument('MedicineBox').getObject('DatumPlane005').MapPathParameter = 0.000000
>>> App.getDocument('MedicineBox').getObject('DatumPlane005').MapMode = 'FlatFace'
>>> App.getDocument('MedicineBox').getObject('DatumPlane005').recompute()
>>> Gui.getDocument('MedicineBox').resetEdit()
>>> _tv_DatumPlane005.restore()
>>> del(_tv_DatumPlane005)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.DatumPlane005.Plane',-45.4343,-67.4905,0)
>>> ### Begin command PartDesign_NewSketch
>>> App.getDocument('MedicineBox').getObject('Body003').newObject('Sketcher::SketchObject','Sketch013')
>>> App.getDocument('MedicineBox').getObject('Sketch013').Support = (App.getDocument('MedicineBox').getObject('DatumPlane005'),'')
>>> App.getDocument('MedicineBox').getObject('Sketch013').MapMode = 'FlatFace'
>>> App.ActiveDocument.recompute()
>>> Gui.getDocument('MedicineBox').setEdit(App.getDocument('MedicineBox').getObject('Part001'), 0, 'Body003.Sketch013.')
>>> ActiveSketch = App.getDocument('MedicineBox').getObject('Sketch013')
>>> tv = Show.TempoVis(App.ActiveDocument, tag= ActiveSketch.ViewObject.TypeId)
>>> ActiveSketch.ViewObject.TempoVis = tv
>>> if ActiveSketch.ViewObject.EditingWorkbench:
>>>   tv.activateWorkbench(ActiveSketch.ViewObject.EditingWorkbench)
>>> if ActiveSketch.ViewObject.HideDependent:
>>>   tv.hide(tv.get_all_dependent(App.getDocument('MedicineBox').getObject('Part001'), 'Body003.Sketch013.'))
>>> if ActiveSketch.ViewObject.ShowSupport:
>>>   tv.show([ref[0] for ref in ActiveSketch.Support if not ref[0].isDerivedFrom("PartDesign::Plane")])
>>> if ActiveSketch.ViewObject.ShowLinks:
>>>   tv.show([ref[0] for ref in ActiveSketch.ExternalGeometry])
>>> tv.sketchClipPlane(ActiveSketch, ActiveSketch.ViewObject.SectionView)
>>> tv.hide(ActiveSketch)
>>> del(tv)
>>> del(ActiveSketch)
>>>
>>> import PartDesignGui
>>> ActiveSketch = App.getDocument('MedicineBox').getObject('Sketch013')
>>> if ActiveSketch.ViewObject.RestoreCamera:
>>>   ActiveSketch.ViewObject.TempoVis.saveCamera()
>>>   if ActiveSketch.ViewObject.ForceOrtho:
>>>     ActiveSketch.ViewObject.Document.ActiveView.setCameraType('Orthographic')
>>>
>>> ### End command PartDesign_NewSketch
>>> # Gui.Selection.clearSelection()
>>> Gui.runCommand('Sketcher_CompCreateRectangles',0)
>>> Gui.runCommand('Sketcher_CompCreateRectangles',0)
>>> geoList = []
>>> geoList.append(Part.LineSegment(App.Vector(-15.006631,21.620058,0),App.Vector(19.409401,21.620058,0)))
>>> geoList.append(Part.LineSegment(App.Vector(19.409401,21.620058,0),App.Vector(19.409401,-27.909100,0)))
>>> geoList.append(Part.LineSegment(App.Vector(19.409401,-27.909100,0),App.Vector(-15.006631,-27.909100,0)))
>>> geoList.append(Part.LineSegment(App.Vector(-15.006631,-27.909100,0),App.Vector(-15.006631,21.620058,0)))
>>> App.getDocument('MedicineBox').getObject('Sketch013').addGeometry(geoList,False)
>>> conList = []
>>> conList.append(Sketcher.Constraint('Coincident',0,2,1,1))
>>> conList.append(Sketcher.Constraint('Coincident',1,2,2,1))
>>> conList.append(Sketcher.Constraint('Coincident',2,2,3,1))
>>> conList.append(Sketcher.Constraint('Coincident',3,2,0,1))
>>> conList.append(Sketcher.Constraint('Horizontal',0))
>>> conList.append(Sketcher.Constraint('Horizontal',2))
>>> conList.append(Sketcher.Constraint('Vertical',1))
>>> conList.append(Sketcher.Constraint('Vertical',3))
>>> App.getDocument('MedicineBox').getObject('Sketch013').addConstraint(conList)
>>> del geoList, conList
>>>
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch013.Edge1',-2.8862,-21.6201,-0.008,False)
>>> ### Begin command Sketcher_ConstrainDistanceX
>>> App.getDocument('MedicineBox').getObject('Sketch013').addConstraint(Sketcher.Constraint('DistanceX',0,1,0,2,34.416032))
>>> App.getDocument('MedicineBox').getObject('Sketch013').setDatum(8,App.Units.Quantity('52.000000 mm'))
>>> ### End command Sketcher_ConstrainDistanceX
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch013.Edge1',0,0,0,False)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch013.Edge4',-24.0346,-10.0982,-0.008,False)
>>> Gui.runCommand('Sketcher_ConstrainDistanceY',0)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch013.Edge4',-24.0346,-9.64927,-0.008,False)
>>> ### Begin command Sketcher_ConstrainDistanceY
>>> App.getDocument('MedicineBox').getObject('Sketch013').addConstraint(Sketcher.Constraint('DistanceY',3,1,3,2,49.529158))
>>> App.getDocument('MedicineBox').getObject('Sketch013').setDatum(9,App.Units.Quantity('90.000000 mm'))
>>> ### End command Sketcher_ConstrainDistanceY
>>> # Gui.Selection.clearSelection()
>>> App.getDocument('MedicineBox').getObject('Sketch013').movePoint(0,0,App.Vector(-24.989033,4.638691,0),1)
>>> App.getDocument('MedicineBox').getObject('Sketch013').movePoint(0,0,App.Vector(1.382851,1.075550,0),1)
>>> Gui.getDocument('MedicineBox').resetEdit()
>>> App.ActiveDocument.recompute()
>>> ActiveSketch = App.getDocument('MedicineBox').getObject('Sketch013')
>>> tv = ActiveSketch.ViewObject.TempoVis
>>> if tv:
>>>   tv.restore()
>>> ActiveSketch.ViewObject.TempoVis = None
>>> del(tv)
>>> del(ActiveSketch)
>>>
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch013.')
>>> App.getDocument('MedicineBox').recompute()
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Pocket006.Sketch012.')
>>> # Gui.Selection.clearSelection()
>>> ActiveSketch = App.getDocument('MedicineBox').getObject('Sketch012')
>>> tv = Show.TempoVis(App.ActiveDocument, tag= ActiveSketch.ViewObject.TypeId)
>>> ActiveSketch.ViewObject.TempoVis = tv
>>> if ActiveSketch.ViewObject.EditingWorkbench:
>>>   tv.activateWorkbench(ActiveSketch.ViewObject.EditingWorkbench)
>>> if ActiveSketch.ViewObject.HideDependent:
>>>   tv.hide(tv.get_all_dependent(App.getDocument('MedicineBox').getObject('Part001'), 'Body003.Pocket006.Sketch012.'))
>>> if ActiveSketch.ViewObject.ShowSupport:
>>>   tv.show([ref[0] for ref in ActiveSketch.Support if not ref[0].isDerivedFrom("PartDesign::Plane")])
>>> if ActiveSketch.ViewObject.ShowLinks:
>>>   tv.show([ref[0] for ref in ActiveSketch.ExternalGeometry])
>>> tv.sketchClipPlane(ActiveSketch, ActiveSketch.ViewObject.SectionView)
>>> tv.hide(ActiveSketch)
>>> del(tv)
>>> del(ActiveSketch)
>>>
>>> import PartDesignGui
>>> ActiveSketch = App.getDocument('MedicineBox').getObject('Sketch012')
>>> if ActiveSketch.ViewObject.RestoreCamera:
>>>   ActiveSketch.ViewObject.TempoVis.saveCamera()
>>>   if ActiveSketch.ViewObject.ForceOrtho:
>>>     ActiveSketch.ViewObject.Document.ActiveView.setCameraType('Orthographic')
>>>
>>> Gui.getDocument('MedicineBox').resetEdit()
>>> App.ActiveDocument.recompute()
>>> ActiveSketch = App.getDocument('MedicineBox').getObject('Sketch012')
>>> tv = ActiveSketch.ViewObject.TempoVis
>>> if tv:
>>>   tv.restore()
>>> ActiveSketch.ViewObject.TempoVis = None
>>> del(tv)
>>> del(ActiveSketch)
>>>
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Pocket006.Sketch012.')
>>> App.getDocument('MedicineBox').recompute()
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch013.')
>>> # Gui.Selection.clearSelection()
>>> ActiveSketch = App.getDocument('MedicineBox').getObject('Sketch013')
>>> tv = Show.TempoVis(App.ActiveDocument, tag= ActiveSketch.ViewObject.TypeId)
>>> ActiveSketch.ViewObject.TempoVis = tv
>>> if ActiveSketch.ViewObject.EditingWorkbench:
>>>   tv.activateWorkbench(ActiveSketch.ViewObject.EditingWorkbench)
>>> if ActiveSketch.ViewObject.HideDependent:
>>>   tv.hide(tv.get_all_dependent(App.getDocument('MedicineBox').getObject('Part001'), 'Body003.Sketch013.'))
>>> if ActiveSketch.ViewObject.ShowSupport:
>>>   tv.show([ref[0] for ref in ActiveSketch.Support if not ref[0].isDerivedFrom("PartDesign::Plane")])
>>> if ActiveSketch.ViewObject.ShowLinks:
>>>   tv.show([ref[0] for ref in ActiveSketch.ExternalGeometry])
>>> tv.sketchClipPlane(ActiveSketch, ActiveSketch.ViewObject.SectionView)
>>> tv.hide(ActiveSketch)
>>> del(tv)
>>> del(ActiveSketch)
>>>
>>> import PartDesignGui
>>> ActiveSketch = App.getDocument('MedicineBox').getObject('Sketch013')
>>> if ActiveSketch.ViewObject.RestoreCamera:
>>>   ActiveSketch.ViewObject.TempoVis.saveCamera()
>>>   if ActiveSketch.ViewObject.ForceOrtho:
>>>     ActiveSketch.ViewObject.Document.ActiveView.setCameraType('Orthographic')
>>>
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch013.Constraint10',-56.6104,-11.171,-0.009,False)
>>> App.getDocument('MedicineBox').getObject('Sketch013').setDatum(9,App.Units.Quantity('55.000000 mm'))
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch013.Constraint9',-24.1396,-58.9045,-0.009,False)
>>> App.getDocument('MedicineBox').getObject('Sketch013').setDatum(8,App.Units.Quantity('45.000000 mm'))
>>> # Gui.Selection.clearSelection()
>>> App.getDocument('MedicineBox').getObject('Sketch013').movePoint(0,0,App.Vector(22.744512,-21.846699,0),1)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch013.Edge1',-20.296,-28.8465,-0.008,False)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch013.Vertex2',24.2753,-28.8465,-0.012,False)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch013.Vertex1',-20.7247,-28.8465,-0.012,False)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch013.V_Axis',0,-62.007,-0.001,False)
>>> ### Begin command Sketcher_ConstrainSymmetric
>>> App.getDocument('MedicineBox').getObject('Sketch013').addConstraint(Sketcher.Constraint('Symmetric',0,2,0,1,-2))
>>> ### End command Sketcher_ConstrainSymmetric
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch013.Vertex1',-22.5,-28.8465,-0.012,False)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch013.Vertex6',-22.5,26.1535,-0.012,False)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch013.H_Axis',-60.8532,0,-0.001,False)
>>> ### Begin command Sketcher_ConstrainSymmetric
>>> App.getDocument('MedicineBox').getObject('Sketch013').addConstraint(Sketcher.Constraint('Symmetric',0,1,2,2,-1))
>>> ### End command Sketcher_ConstrainSymmetric
>>> # Gui.Selection.clearSelection()
>>> Gui.getDocument('MedicineBox').resetEdit()
>>> App.ActiveDocument.recompute()
>>> ActiveSketch = App.getDocument('MedicineBox').getObject('Sketch013')
>>> tv = ActiveSketch.ViewObject.TempoVis
>>> if tv:
>>>   tv.restore()
>>> ActiveSketch.ViewObject.TempoVis = None
>>> del(tv)
>>> del(ActiveSketch)
>>>
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch013.')
>>> App.getDocument('MedicineBox').recompute()
>>> FreeCAD.getDocument('MedicineBox').getObject('Sketch013').AttachmentOffset = App.Placement(App.Vector(-2.00,0.00,0.00),App.Rotation(App.Vector(0.00,0.00,1.00),0.00))
>>>
>>> FreeCAD.getDocument('MedicineBox').getObject('Sketch013').AttachmentOffset = App.Placement(App.Vector(-25.00,0.00,0.00),App.Rotation(App.Vector(0.00,0.00,1.00),0.00))
>>>
>>> FreeCAD.getDocument('MedicineBox').getObject('Sketch013').AttachmentOffset = App.Placement(App.Vector(-25.00,-3.00,0.00),App.Rotation(App.Vector(0.00,0.00,1.00),0.00))
>>>
>>> FreeCAD.getDocument('MedicineBox').getObject('Sketch013').AttachmentOffset = App.Placement(App.Vector(-25.00,-35.00,0.00),App.Rotation(App.Vector(0.00,0.00,1.00),0.00))
>>>
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Pocket006.Sketch012.')
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch013.')
>>> FreeCAD.getDocument('MedicineBox').getObject('Sketch013').AttachmentOffset = App.Placement(App.Vector(-25.00,-3.00,0.00),App.Rotation(App.Vector(0.00,0.00,1.00),0.00))
>>>
>>> FreeCAD.getDocument('MedicineBox').getObject('Sketch013').AttachmentOffset = App.Placement(App.Vector(-25.00,-30.00,0.00),App.Rotation(App.Vector(0.00,0.00,1.00),0.00))
>>>
>>> ### Begin command PartDesign_Pocket
>>> App.getDocument('MedicineBox').getObject('Body003').newObject('PartDesign::Pocket','Pocket007')
>>> App.getDocument('MedicineBox').getObject('Pocket007').Profile = App.getDocument('MedicineBox').getObject('Sketch013')
>>> App.getDocument('MedicineBox').getObject('Pocket007').Length = 5
>>> App.ActiveDocument.recompute()
>>> App.getDocument('MedicineBox').getObject('Pocket007').ReferenceAxis = (App.getDocument('MedicineBox').getObject('Sketch013'),['N_Axis'])
>>> App.getDocument('MedicineBox').getObject('Sketch013').Visibility = False
>>> App.ActiveDocument.recompute()
>>> App.getDocument('MedicineBox').getObject('Pocket007').ViewObject.ShapeColor=getattr(App.getDocument('MedicineBox').getObject('MultiTransform002').getLinkedObject(True).ViewObject,'ShapeColor',App.getDocument('MedicineBox').getObject('Pocket007').ViewObject.ShapeColor)
>>> App.getDocument('MedicineBox').getObject('Pocket007').ViewObject.LineColor=getattr(App.getDocument('MedicineBox').getObject('MultiTransform002').getLinkedObject(True).ViewObject,'LineColor',App.getDocument('MedicineBox').getObject('Pocket007').ViewObject.LineColor)
>>> App.getDocument('MedicineBox').getObject('Pocket007').ViewObject.PointColor=getattr(App.getDocument('MedicineBox').getObject('MultiTransform002').getLinkedObject(True).ViewObject,'PointColor',App.getDocument('MedicineBox').getObject('Pocket007').ViewObject.PointColor)
>>> App.getDocument('MedicineBox').getObject('Pocket007').ViewObject.Transparency=getattr(App.getDocument('MedicineBox').getObject('MultiTransform002').getLinkedObject(True).ViewObject,'Transparency',App.getDocument('MedicineBox').getObject('Pocket007').ViewObject.Transparency)
>>> App.getDocument('MedicineBox').getObject('Pocket007').ViewObject.DisplayMode=getattr(App.getDocument('MedicineBox').getObject('MultiTransform002').getLinkedObject(True).ViewObject,'DisplayMode',App.getDocument('MedicineBox').getObject('Pocket007').ViewObject.DisplayMode)
>>> Gui.getDocument('MedicineBox').setEdit(App.getDocument('MedicineBox').getObject('Part001'), 0, 'Body003.Pocket007.')
>>> Gui.Selection.clearSelection()
>>> ### End command PartDesign_Pocket
>>> # Gui.Selection.clearSelection()
>>> App.getDocument('MedicineBox').getObject('Pocket007').Length = 48.000000
>>> App.getDocument('MedicineBox').getObject('Pocket007').Length2 = 5.000000
>>> App.getDocument('MedicineBox').getObject('Pocket007').TaperAngle = 0.000000
>>> App.getDocument('MedicineBox').getObject('Pocket007').TaperAngle2 = 0.000000
>>> App.getDocument('MedicineBox').getObject('Pocket007').UseCustomVector = 0
>>> App.getDocument('MedicineBox').getObject('Pocket007').Direction = (0, 0, 1)
>>> App.getDocument('MedicineBox').getObject('Pocket007').ReferenceAxis = (App.getDocument('MedicineBox').getObject('Sketch013'), ['N_Axis'])
>>> App.getDocument('MedicineBox').getObject('Pocket007').AlongSketchNormal = 1
>>> App.getDocument('MedicineBox').getObject('Pocket007').Type = 0
>>> App.getDocument('MedicineBox').getObject('Pocket007').UpToFace = None
>>> App.getDocument('MedicineBox').getObject('Pocket007').Reversed = 0
>>> App.getDocument('MedicineBox').getObject('Pocket007').Midplane = 0
>>> App.getDocument('MedicineBox').getObject('Pocket007').Offset = 0
>>> App.getDocument('MedicineBox').recompute()
>>> App.getDocument('MedicineBox').getObject('MultiTransform002').Visibility = False
>>> Gui.getDocument('MedicineBox').resetEdit()
>>> App.getDocument('MedicineBox').getObject('Sketch013').Visibility = False
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body002.Pocket004.Sketch009.')
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body002.Pocket004.')
>>> Gui.runCommand('Std_ToggleVisibility',0)
>>> Gui.runCommand('Std_ToggleVisibility',0)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body002.')
>>> Gui.runCommand('Std_ToggleVisibility',0)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.')
>>> Gui.runCommand('Std_ToggleVisibility',0)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body002.Fillet006.')
>>> Gui.runCommand('Std_ToggleVisibility',0)
>>> Gui.runCommand('Std_ToggleVisibility',0)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body002.Pocket004.')
>>> Gui.runCommand('Std_ToggleVisibility',0)
>>> Gui.runCommand('Std_ToggleVisibility',0)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body002.MultiTransform001.')
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body002.Pocket003.')
>>> Gui.runCommand('Std_ToggleVisibility',0)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body002.Pocket004.')
>>> Gui.runCommand('Std_ToggleVisibility',0)
>>> Gui.runCommand('Std_ToggleVisibility',0)
>>> Gui.runCommand('Std_ToggleVisibility',0)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body002.Pocket005.')
>>> Gui.runCommand('Std_ToggleVisibility',0)
>>> Gui.runCommand('Std_ToggleVisibility',0)
>>> Gui.runCommand('Std_ToggleVisibility',0)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body002.')
>>> Gui.runCommand('Std_ToggleVisibility',0)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.')
>>> Gui.runCommand('Std_ToggleVisibility',0)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Pocket007.')
>>> Gui.ActiveDocument.setEdit(App.getDocument('MedicineBox').getObject('Pocket007'), 0)
>>> # Gui.Selection.clearSelection()
>>> App.getDocument('MedicineBox').getObject('Pocket007').Length = 45.000000
>>> App.getDocument('MedicineBox').getObject('Pocket007').Length2 = 5.000000
>>> App.getDocument('MedicineBox').getObject('Pocket007').TaperAngle = 0.000000
>>> App.getDocument('MedicineBox').getObject('Pocket007').TaperAngle2 = 0.000000
>>> App.getDocument('MedicineBox').getObject('Pocket007').UseCustomVector = 0
>>> App.getDocument('MedicineBox').getObject('Pocket007').Direction = (0, 0, 1)
>>> App.getDocument('MedicineBox').getObject('Pocket007').ReferenceAxis = (App.getDocument('MedicineBox').getObject('Sketch013'), ['N_Axis'])
>>> App.getDocument('MedicineBox').getObject('Pocket007').AlongSketchNormal = 1
>>> App.getDocument('MedicineBox').getObject('Pocket007').Type = 0
>>> App.getDocument('MedicineBox').getObject('Pocket007').UpToFace = None
>>> App.getDocument('MedicineBox').getObject('Pocket007').Reversed = 0
>>> App.getDocument('MedicineBox').getObject('Pocket007').Midplane = 0
>>> App.getDocument('MedicineBox').getObject('Pocket007').Offset = 0
>>> App.getDocument('MedicineBox').recompute()
>>> App.getDocument('MedicineBox').getObject('MultiTransform002').Visibility = False
>>> Gui.getDocument('MedicineBox').resetEdit()
>>> App.getDocument('MedicineBox').getObject('Sketch013').Visibility = False
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Pocket007.')
>>> ### Begin command PartDesign_MultiTransform
>>> App.getDocument('MedicineBox').getObject('Body003').newObject('PartDesign::MultiTransform','MultiTransform003')
>>> App.ActiveDocument.recompute()
>>> App.getDocument('MedicineBox').getObject('MultiTransform003').Originals = [App.getDocument('MedicineBox').getObject('Pocket007'),]
>>> App.getDocument('MedicineBox').getObject('MultiTransform003').Shape = App.getDocument('MedicineBox').getObject('Pocket007').Shape
>>> App.ActiveDocument.recompute()
>>> App.getDocument('MedicineBox').getObject('MultiTransform003').ViewObject.ShapeColor=getattr(App.getDocument('MedicineBox').getObject('Pocket007').getLinkedObject(True).ViewObject,'ShapeColor',App.getDocument('MedicineBox').getObject('MultiTransform003').ViewObject.ShapeColor)
>>> App.getDocument('MedicineBox').getObject('MultiTransform003').ViewObject.LineColor=getattr(App.getDocument('MedicineBox').getObject('Pocket007').getLinkedObject(True).ViewObject,'LineColor',App.getDocument('MedicineBox').getObject('MultiTransform003').ViewObject.LineColor)
>>> App.getDocument('MedicineBox').getObject('MultiTransform003').ViewObject.PointColor=getattr(App.getDocument('MedicineBox').getObject('Pocket007').getLinkedObject(True).ViewObject,'PointColor',App.getDocument('MedicineBox').getObject('MultiTransform003').ViewObject.PointColor)
>>> App.getDocument('MedicineBox').getObject('MultiTransform003').ViewObject.Transparency=getattr(App.getDocument('MedicineBox').getObject('Pocket007').getLinkedObject(True).ViewObject,'Transparency',App.getDocument('MedicineBox').getObject('MultiTransform003').ViewObject.Transparency)
>>> App.getDocument('MedicineBox').getObject('MultiTransform003').ViewObject.DisplayMode=getattr(App.getDocument('MedicineBox').getObject('Pocket007').getLinkedObject(True).ViewObject,'DisplayMode',App.getDocument('MedicineBox').getObject('MultiTransform003').ViewObject.DisplayMode)
>>> Gui.getDocument('MedicineBox').setEdit(App.getDocument('MedicineBox').getObject('Part001'), 0, 'Body003.MultiTransform003.')
>>> Gui.Selection.clearSelection()
>>> App.getDocument('MedicineBox').getObject('Body003').Tip = App.getDocument('MedicineBox').getObject('MultiTransform003')
>>> App.ActiveDocument.recompute()
>>> ### End command PartDesign_MultiTransform
>>> # Gui.Selection.clearSelection()
>>> App.getDocument('MedicineBox').getObject('Body003').newObject('PartDesign::Mirrored','Mirrored006')
>>> App.getDocument('MedicineBox').getObject('Mirrored006').MirrorPlane = (App.getDocument('MedicineBox').getObject('Sketch013'),['V_Axis'])
>>> App.getDocument('MedicineBox').getObject('Pocket007').Visibility = False
>>> App.getDocument('MedicineBox').getObject('Mirrored006').Visibility = False
>>> App.getDocument('MedicineBox').getObject('MultiTransform003').Visibility = True
>>> App.getDocument('MedicineBox').getObject('MultiTransform003').Visibility = True
>>> App.getDocument('MedicineBox').getObject('MultiTransform003').Visibility = True
>>> App.getDocument('MedicineBox').getObject('Body003').newObject('PartDesign::Mirrored','Mirrored007')
>>> App.getDocument('MedicineBox').getObject('Mirrored007').MirrorPlane = (App.getDocument('MedicineBox').getObject('Sketch013'),['V_Axis'])
>>> App.getDocument('MedicineBox').getObject('Mirrored007').Visibility = False
>>> App.getDocument('MedicineBox').getObject('MultiTransform003').Visibility = True
>>> App.getDocument('MedicineBox').getObject('MultiTransform003').Visibility = True
>>> App.getDocument('MedicineBox').getObject('MultiTransform003').Transformations = [App.getDocument('MedicineBox').getObject('Mirrored006'),App.getDocument('MedicineBox').getObject('Mirrored007'),]
>>> App.getDocument('MedicineBox').recompute()
>>> App.getDocument('MedicineBox').getObject('Pocket007').Visibility = False
>>> Gui.getDocument('MedicineBox').resetEdit()
>>> App.getDocument('MedicineBox').getObject('MultiTransform003').Visibility = True
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.DatumPlane005.')
>>> Gui.runCommand('Std_ToggleVisibility',0)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body002.')
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body002.Pocket005.Sketch010.')
>>> # Gui.Selection.clearSelection()
>>> ActiveSketch = App.getDocument('MedicineBox').getObject('Sketch010')
>>> tv = Show.TempoVis(App.ActiveDocument, tag= ActiveSketch.ViewObject.TypeId)
>>> ActiveSketch.ViewObject.TempoVis = tv
>>> if ActiveSketch.ViewObject.EditingWorkbench:
>>>   tv.activateWorkbench(ActiveSketch.ViewObject.EditingWorkbench)
>>> if ActiveSketch.ViewObject.HideDependent:
>>>   tv.hide(tv.get_all_dependent(App.getDocument('MedicineBox').getObject('Part001'), 'Body002.Pocket005.Sketch010.'))
>>> if ActiveSketch.ViewObject.ShowSupport:
>>>   tv.show([ref[0] for ref in ActiveSketch.Support if not ref[0].isDerivedFrom("PartDesign::Plane")])
>>> if ActiveSketch.ViewObject.ShowLinks:
>>>   tv.show([ref[0] for ref in ActiveSketch.ExternalGeometry])
>>> tv.sketchClipPlane(ActiveSketch, ActiveSketch.ViewObject.SectionView)
>>> tv.hide(ActiveSketch)
>>> del(tv)
>>> del(ActiveSketch)
>>>
>>> import PartDesignGui
>>> ActiveSketch = App.getDocument('MedicineBox').getObject('Sketch010')
>>> if ActiveSketch.ViewObject.RestoreCamera:
>>>   ActiveSketch.ViewObject.TempoVis.saveCamera()
>>>   if ActiveSketch.ViewObject.ForceOrtho:
>>>     ActiveSketch.ViewObject.Document.ActiveView.setCameraType('Orthographic')
>>>
>>> Gui.getDocument('MedicineBox').resetEdit()
>>> App.ActiveDocument.recompute()
>>> ActiveSketch = App.getDocument('MedicineBox').getObject('Sketch010')
>>> tv = ActiveSketch.ViewObject.TempoVis
>>> if tv:
>>>   tv.restore()
>>> ActiveSketch.ViewObject.TempoVis = None
>>> del(tv)
>>> del(ActiveSketch)
>>>
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body002.Pocket005.Sketch010.')
>>> App.getDocument('MedicineBox').recompute()
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body002.Fillet006.')
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body002.Pocket004.Sketch009.')
>>> # Gui.Selection.clearSelection()
>>> ActiveSketch = App.getDocument('MedicineBox').getObject('Sketch009')
>>> tv = Show.TempoVis(App.ActiveDocument, tag= ActiveSketch.ViewObject.TypeId)
>>> ActiveSketch.ViewObject.TempoVis = tv
>>> if ActiveSketch.ViewObject.EditingWorkbench:
>>>   tv.activateWorkbench(ActiveSketch.ViewObject.EditingWorkbench)
>>> if ActiveSketch.ViewObject.HideDependent:
>>>   tv.hide(tv.get_all_dependent(App.getDocument('MedicineBox').getObject('Part001'), 'Body002.Pocket004.Sketch009.'))
>>> if ActiveSketch.ViewObject.ShowSupport:
>>>   tv.show([ref[0] for ref in ActiveSketch.Support if not ref[0].isDerivedFrom("PartDesign::Plane")])
>>> if ActiveSketch.ViewObject.ShowLinks:
>>>   tv.show([ref[0] for ref in ActiveSketch.ExternalGeometry])
>>> tv.sketchClipPlane(ActiveSketch, ActiveSketch.ViewObject.SectionView)
>>> tv.hide(ActiveSketch)
>>> del(tv)
>>> del(ActiveSketch)
>>>
>>> import PartDesignGui
>>> ActiveSketch = App.getDocument('MedicineBox').getObject('Sketch009')
>>> if ActiveSketch.ViewObject.RestoreCamera:
>>>   ActiveSketch.ViewObject.TempoVis.saveCamera()
>>>   if ActiveSketch.ViewObject.ForceOrtho:
>>>     ActiveSketch.ViewObject.Document.ActiveView.setCameraType('Orthographic')
>>>
>>> Gui.getDocument('MedicineBox').resetEdit()
>>> App.ActiveDocument.recompute()
>>> ActiveSketch = App.getDocument('MedicineBox').getObject('Sketch009')
>>> tv = ActiveSketch.ViewObject.TempoVis
>>> if tv:
>>>   tv.restore()
>>> ActiveSketch.ViewObject.TempoVis = None
>>> del(tv)
>>> del(ActiveSketch)
>>>
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body002.Pocket004.Sketch009.')
>>> App.getDocument('MedicineBox').recompute()
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body002.MultiTransform001.')
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body002.Pocket003.Sketch008.')
>>> # Gui.Selection.clearSelection()
>>> ActiveSketch = App.getDocument('MedicineBox').getObject('Sketch008')
>>> tv = Show.TempoVis(App.ActiveDocument, tag= ActiveSketch.ViewObject.TypeId)
>>> ActiveSketch.ViewObject.TempoVis = tv
>>> if ActiveSketch.ViewObject.EditingWorkbench:
>>>   tv.activateWorkbench(ActiveSketch.ViewObject.EditingWorkbench)
>>> if ActiveSketch.ViewObject.HideDependent:
>>>   tv.hide(tv.get_all_dependent(App.getDocument('MedicineBox').getObject('Part001'), 'Body002.Pocket003.Sketch008.'))
>>> if ActiveSketch.ViewObject.ShowSupport:
>>>   tv.show([ref[0] for ref in ActiveSketch.Support if not ref[0].isDerivedFrom("PartDesign::Plane")])
>>> if ActiveSketch.ViewObject.ShowLinks:
>>>   tv.show([ref[0] for ref in ActiveSketch.ExternalGeometry])
>>> tv.sketchClipPlane(ActiveSketch, ActiveSketch.ViewObject.SectionView)
>>> tv.hide(ActiveSketch)
>>> del(tv)
>>> del(ActiveSketch)
>>>
>>> import PartDesignGui
>>> ActiveSketch = App.getDocument('MedicineBox').getObject('Sketch008')
>>> if ActiveSketch.ViewObject.RestoreCamera:
>>>   ActiveSketch.ViewObject.TempoVis.saveCamera()
>>>   if ActiveSketch.ViewObject.ForceOrtho:
>>>     ActiveSketch.ViewObject.Document.ActiveView.setCameraType('Orthographic')
>>>
>>> Gui.getDocument('MedicineBox').resetEdit()
>>> App.ActiveDocument.recompute()
>>> ActiveSketch = App.getDocument('MedicineBox').getObject('Sketch008')
>>> tv = ActiveSketch.ViewObject.TempoVis
>>> if tv:
>>>   tv.restore()
>>> ActiveSketch.ViewObject.TempoVis = None
>>> del(tv)
>>> del(ActiveSketch)
>>>
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body002.Pocket003.Sketch008.')
>>> App.getDocument('MedicineBox').recompute()
>>> Gui.runCommand('Std_Copy',0)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.MultiTransform003.')
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.MultiTransform003.Face5',-47.2108,51.0881,50)
>>> ### Begin command PartDesign_Plane
>>> App.getDocument('MedicineBox').getObject('Body003').newObject('PartDesign::Plane','DatumPlane006')
>>> App.getDocument('MedicineBox').getObject('DatumPlane006').Support = [(App.getDocument('MedicineBox').getObject('MultiTransform003'),'Face5')]
>>> App.getDocument('MedicineBox').getObject('DatumPlane006').MapMode = 'FlatFace'
>>> App.activeDocument().recompute()
>>> Gui.getDocument('MedicineBox').setEdit(App.getDocument('MedicineBox').getObject('Part001'), 0, 'Body003.DatumPlane006.')
>>> import Show
>>> from Show.Containers import isAContainer
>>> _tv_DatumPlane006 = Show.TempoVis(App.ActiveDocument, tag= 'PartGui::TaskAttacher')
>>> tvObj = App.getDocument('MedicineBox').getObject('DatumPlane006')
>>> dep_features = _tv_DatumPlane006.get_all_dependent(App.getDocument('MedicineBox').getObject('Part001'), 'Body003.DatumPlane006.')
>>> dep_features = [o for o in dep_features if not isAContainer(o)]
>>> if tvObj.isDerivedFrom('PartDesign::CoordinateSystem'):
>>> 	visible_features = [feat for feat in tvObj.InList if feat.isDerivedFrom('PartDesign::FeaturePrimitive')]
>>> 	dep_features = [feat for feat in dep_features if feat not in visible_features]
>>> 	del(visible_features)
>>> _tv_DatumPlane006.hide(dep_features)
>>> del(dep_features)
>>> if not tvObj.isDerivedFrom('PartDesign::CoordinateSystem'):
>>> 		if len(tvObj.Support) > 0:
>>> 			_tv_DatumPlane006.show([lnk[0] for lnk in tvObj.Support])
>>> del(tvObj)
>>> ### End command PartDesign_Plane
>>> # Gui.Selection.clearSelection()
>>> App.getDocument('MedicineBox').getObject('DatumPlane006').AttachmentOffset = App.Placement(App.Vector(0.0000000000, 0.0000000000, 0.0000000000),  App.Rotation(0.0000000000, 0.0000000000, 0.0000000000))
>>> App.getDocument('MedicineBox').getObject('DatumPlane006').MapReversed = False
>>> App.getDocument('MedicineBox').getObject('DatumPlane006').Support = [(App.getDocument('MedicineBox').getObject('MultiTransform003'),'Face5')]
>>> App.getDocument('MedicineBox').getObject('DatumPlane006').MapPathParameter = 0.000000
>>> App.getDocument('MedicineBox').getObject('DatumPlane006').MapMode = 'FlatFace'
>>> App.getDocument('MedicineBox').getObject('DatumPlane006').recompute()
>>> Gui.getDocument('MedicineBox').resetEdit()
>>> _tv_DatumPlane006.restore()
>>> del(_tv_DatumPlane006)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.DatumPlane006.Plane',-9.07526,66.8397,50)
>>> ### Begin command PartDesign_NewSketch
>>> App.getDocument('MedicineBox').getObject('Body003').newObject('Sketcher::SketchObject','Sketch014')
>>> App.getDocument('MedicineBox').getObject('Sketch014').Support = (App.getDocument('MedicineBox').getObject('DatumPlane006'),'')
>>> App.getDocument('MedicineBox').getObject('Sketch014').MapMode = 'FlatFace'
>>> App.ActiveDocument.recompute()
>>> Gui.getDocument('MedicineBox').setEdit(App.getDocument('MedicineBox').getObject('Part001'), 0, 'Body003.Sketch014.')
>>> ActiveSketch = App.getDocument('MedicineBox').getObject('Sketch014')
>>> tv = Show.TempoVis(App.ActiveDocument, tag= ActiveSketch.ViewObject.TypeId)
>>> ActiveSketch.ViewObject.TempoVis = tv
>>> if ActiveSketch.ViewObject.EditingWorkbench:
>>>   tv.activateWorkbench(ActiveSketch.ViewObject.EditingWorkbench)
>>> if ActiveSketch.ViewObject.HideDependent:
>>>   tv.hide(tv.get_all_dependent(App.getDocument('MedicineBox').getObject('Part001'), 'Body003.Sketch014.'))
>>> if ActiveSketch.ViewObject.ShowSupport:
>>>   tv.show([ref[0] for ref in ActiveSketch.Support if not ref[0].isDerivedFrom("PartDesign::Plane")])
>>> if ActiveSketch.ViewObject.ShowLinks:
>>>   tv.show([ref[0] for ref in ActiveSketch.ExternalGeometry])
>>> tv.sketchClipPlane(ActiveSketch, ActiveSketch.ViewObject.SectionView)
>>> tv.hide(ActiveSketch)
>>> del(tv)
>>> del(ActiveSketch)
>>>
>>> import PartDesignGui
>>> ActiveSketch = App.getDocument('MedicineBox').getObject('Sketch014')
>>> if ActiveSketch.ViewObject.RestoreCamera:
>>>   ActiveSketch.ViewObject.TempoVis.saveCamera()
>>>   if ActiveSketch.ViewObject.ForceOrtho:
>>>     ActiveSketch.ViewObject.Document.ActiveView.setCameraType('Orthographic')
>>>
>>> ### End command PartDesign_NewSketch
>>> # Gui.Selection.clearSelection()
>>> Gui.runCommand('Sketcher_CompCreateCircle',0)
>>> App.getDocument('MedicineBox').getObject('Sketch014').addGeometry(Part.Circle(App.Vector(-20.893137,28.509693,0),App.Vector(0,0,1),4.448968),False)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch014.Vertex1',-20.8931,28.5097,50.012,False)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch014.V_Axis',0,78.1885,50.001,False)
>>> ### Begin command Sketcher_ConstrainDistanceX
>>> App.getDocument('MedicineBox').getObject('Sketch014').addConstraint(Sketcher.Constraint('DistanceX',0,3,-1,1,20.893137))
>>> App.getDocument('MedicineBox').getObject('Sketch014').setDatum(0,App.Units.Quantity('19.000000 mm'))
>>> ### End command Sketcher_ConstrainDistanceX
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch014.Vertex1',-19,28.5097,50.012,False)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch014.H_Axis',-69.6741,0,50.001,False)
>>> ### Begin command Sketcher_ConstrainDistanceY
>>> App.getDocument('MedicineBox').getObject('Sketch014').addConstraint(Sketcher.Constraint('DistanceY',-1,1,0,3,28.509693))
>>> App.getDocument('MedicineBox').getObject('Sketch014').setDatum(1,App.Units.Quantity('24.000000 mm'))
>>> ### End command Sketcher_ConstrainDistanceY
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch014.Edge1',-14.6861,25.0818,50.008,False)
>>> ### Begin command Sketcher_CompConstrainRadDia
>>> App.getDocument('MedicineBox').getObject('Sketch014').addConstraint(Sketcher.Constraint('Radius',0,4.448968))
>>> App.getDocument('MedicineBox').getObject('Sketch014').setDatum(2,App.Units.Quantity('2.500000 mm'))
>>> ### End command Sketcher_CompConstrainRadDia
>>> # Gui.Selection.clearSelection()
>>> Gui.getDocument('MedicineBox').resetEdit()
>>> App.ActiveDocument.recompute()
>>> ActiveSketch = App.getDocument('MedicineBox').getObject('Sketch014')
>>> tv = ActiveSketch.ViewObject.TempoVis
>>> if tv:
>>>   tv.restore()
>>> ActiveSketch.ViewObject.TempoVis = None
>>> del(tv)
>>> del(ActiveSketch)
>>>
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch014.')
>>> App.getDocument('MedicineBox').recompute()
>>> FreeCAD.getDocument('MedicineBox').getObject('Sketch014').AttachmentOffset = App.Placement(App.Vector(-2.00,0.00,0.00),App.Rotation(App.Vector(0.00,0.00,1.00),0.00))
>>>
>>> FreeCAD.getDocument('MedicineBox').getObject('Sketch014').AttachmentOffset = App.Placement(App.Vector(-25.00,0.00,0.00),App.Rotation(App.Vector(0.00,0.00,1.00),0.00))
>>>
>>> FreeCAD.getDocument('MedicineBox').getObject('Sketch014').AttachmentOffset = App.Placement(App.Vector(-25.00,-3.00,0.00),App.Rotation(App.Vector(0.00,0.00,1.00),0.00))
>>>
>>> FreeCAD.getDocument('MedicineBox').getObject('Sketch014').AttachmentOffset = App.Placement(App.Vector(-25.00,-30.00,0.00),App.Rotation(App.Vector(0.00,0.00,1.00),0.00))
>>>
>>> ### Begin command PartDesign_Hole
>>> App.getDocument('MedicineBox').getObject('Body003').newObject('PartDesign::Hole','Hole')
>>> App.getDocument('MedicineBox').getObject('Hole').Profile = App.getDocument('MedicineBox').getObject('Sketch014')
>>> App.getDocument('MedicineBox').getObject('Sketch014').Visibility = False
>>> App.ActiveDocument.recompute()
>>> App.getDocument('MedicineBox').getObject('Hole').ViewObject.ShapeColor=getattr(App.getDocument('MedicineBox').getObject('MultiTransform003').getLinkedObject(True).ViewObject,'ShapeColor',App.getDocument('MedicineBox').getObject('Hole').ViewObject.ShapeColor)
>>> App.getDocument('MedicineBox').getObject('Hole').ViewObject.LineColor=getattr(App.getDocument('MedicineBox').getObject('MultiTransform003').getLinkedObject(True).ViewObject,'LineColor',App.getDocument('MedicineBox').getObject('Hole').ViewObject.LineColor)
>>> App.getDocument('MedicineBox').getObject('Hole').ViewObject.PointColor=getattr(App.getDocument('MedicineBox').getObject('MultiTransform003').getLinkedObject(True).ViewObject,'PointColor',App.getDocument('MedicineBox').getObject('Hole').ViewObject.PointColor)
>>> App.getDocument('MedicineBox').getObject('Hole').ViewObject.Transparency=getattr(App.getDocument('MedicineBox').getObject('MultiTransform003').getLinkedObject(True).ViewObject,'Transparency',App.getDocument('MedicineBox').getObject('Hole').ViewObject.Transparency)
>>> App.getDocument('MedicineBox').getObject('Hole').ViewObject.DisplayMode=getattr(App.getDocument('MedicineBox').getObject('MultiTransform003').getLinkedObject(True).ViewObject,'DisplayMode',App.getDocument('MedicineBox').getObject('Hole').ViewObject.DisplayMode)
>>> Gui.getDocument('MedicineBox').setEdit(App.getDocument('MedicineBox').getObject('Part001'), 0, 'Body003.Hole.')
>>> Gui.Selection.clearSelection()
>>> ### End command PartDesign_Hole
>>> # Gui.Selection.clearSelection()
>>> App.getDocument('MedicineBox').recompute()
>>> Gui.getDocument('MedicineBox').resetEdit()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch014.')
>>> ### Begin command PartDesign_Pocket
>>> App.getDocument('MedicineBox').getObject('Body003').newObject('PartDesign::Pocket','Pocket008')
>>> App.getDocument('MedicineBox').getObject('Pocket008').Profile = App.getDocument('MedicineBox').getObject('Sketch014')
>>> App.getDocument('MedicineBox').getObject('Pocket008').Length = 5
>>> App.ActiveDocument.recompute()
>>> App.getDocument('MedicineBox').getObject('Pocket008').ReferenceAxis = (App.getDocument('MedicineBox').getObject('Sketch014'),['N_Axis'])
>>> App.getDocument('MedicineBox').getObject('Sketch014').Visibility = False
>>> App.ActiveDocument.recompute()
>>> App.getDocument('MedicineBox').getObject('Pocket008').ViewObject.ShapeColor=getattr(App.getDocument('MedicineBox').getObject('MultiTransform003').getLinkedObject(True).ViewObject,'ShapeColor',App.getDocument('MedicineBox').getObject('Pocket008').ViewObject.ShapeColor)
>>> App.getDocument('MedicineBox').getObject('Pocket008').ViewObject.LineColor=getattr(App.getDocument('MedicineBox').getObject('MultiTransform003').getLinkedObject(True).ViewObject,'LineColor',App.getDocument('MedicineBox').getObject('Pocket008').ViewObject.LineColor)
>>> App.getDocument('MedicineBox').getObject('Pocket008').ViewObject.PointColor=getattr(App.getDocument('MedicineBox').getObject('MultiTransform003').getLinkedObject(True).ViewObject,'PointColor',App.getDocument('MedicineBox').getObject('Pocket008').ViewObject.PointColor)
>>> App.getDocument('MedicineBox').getObject('Pocket008').ViewObject.Transparency=getattr(App.getDocument('MedicineBox').getObject('MultiTransform003').getLinkedObject(True).ViewObject,'Transparency',App.getDocument('MedicineBox').getObject('Pocket008').ViewObject.Transparency)
>>> App.getDocument('MedicineBox').getObject('Pocket008').ViewObject.DisplayMode=getattr(App.getDocument('MedicineBox').getObject('MultiTransform003').getLinkedObject(True).ViewObject,'DisplayMode',App.getDocument('MedicineBox').getObject('Pocket008').ViewObject.DisplayMode)
>>> Gui.getDocument('MedicineBox').setEdit(App.getDocument('MedicineBox').getObject('Part001'), 0, 'Body003.Pocket008.')
>>> Gui.Selection.clearSelection()
>>> ### End command PartDesign_Pocket
>>> # Gui.Selection.clearSelection()
>>> App.getDocument('MedicineBox').getObject('Pocket008').Length = 5.000000
>>> App.getDocument('MedicineBox').getObject('Pocket008').Length2 = 5.000000
>>> App.getDocument('MedicineBox').getObject('Pocket008').TaperAngle = 0.000000
>>> App.getDocument('MedicineBox').getObject('Pocket008').TaperAngle2 = 0.000000
>>> App.getDocument('MedicineBox').getObject('Pocket008').UseCustomVector = 0
>>> App.getDocument('MedicineBox').getObject('Pocket008').Direction = (0, 0, -1)
>>> App.getDocument('MedicineBox').getObject('Pocket008').ReferenceAxis = (App.getDocument('MedicineBox').getObject('Sketch014'), ['N_Axis'])
>>> App.getDocument('MedicineBox').getObject('Pocket008').AlongSketchNormal = 1
>>> App.getDocument('MedicineBox').getObject('Pocket008').Type = 1
>>> App.getDocument('MedicineBox').getObject('Pocket008').UpToFace = None
>>> App.getDocument('MedicineBox').getObject('Pocket008').Reversed = 0
>>> App.getDocument('MedicineBox').getObject('Pocket008').Midplane = 0
>>> App.getDocument('MedicineBox').getObject('Pocket008').Offset = 0
>>> App.getDocument('MedicineBox').recompute()
>>> App.getDocument('MedicineBox').getObject('MultiTransform003').Visibility = False
>>> Gui.getDocument('MedicineBox').resetEdit()
>>> App.getDocument('MedicineBox').getObject('Sketch014').Visibility = False
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Pocket008.')
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Pocket008.Sketch014.')
>>> Gui.runCommand('PartDesign_MultiTransform',0)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Pocket008.')
>>> ### Begin command PartDesign_MultiTransform
>>> App.getDocument('MedicineBox').getObject('Body003').newObject('PartDesign::MultiTransform','MultiTransform004')
>>> App.ActiveDocument.recompute()
>>> App.getDocument('MedicineBox').getObject('MultiTransform004').Originals = [App.getDocument('MedicineBox').getObject('Pocket008'),]
>>> App.getDocument('MedicineBox').getObject('MultiTransform004').Shape = App.getDocument('MedicineBox').getObject('Pocket008').Shape
>>> App.ActiveDocument.recompute()
>>> App.getDocument('MedicineBox').getObject('MultiTransform004').ViewObject.ShapeColor=getattr(App.getDocument('MedicineBox').getObject('Pocket008').getLinkedObject(True).ViewObject,'ShapeColor',App.getDocument('MedicineBox').getObject('MultiTransform004').ViewObject.ShapeColor)
>>> App.getDocument('MedicineBox').getObject('MultiTransform004').ViewObject.LineColor=getattr(App.getDocument('MedicineBox').getObject('Pocket008').getLinkedObject(True).ViewObject,'LineColor',App.getDocument('MedicineBox').getObject('MultiTransform004').ViewObject.LineColor)
>>> App.getDocument('MedicineBox').getObject('MultiTransform004').ViewObject.PointColor=getattr(App.getDocument('MedicineBox').getObject('Pocket008').getLinkedObject(True).ViewObject,'PointColor',App.getDocument('MedicineBox').getObject('MultiTransform004').ViewObject.PointColor)
>>> App.getDocument('MedicineBox').getObject('MultiTransform004').ViewObject.Transparency=getattr(App.getDocument('MedicineBox').getObject('Pocket008').getLinkedObject(True).ViewObject,'Transparency',App.getDocument('MedicineBox').getObject('MultiTransform004').ViewObject.Transparency)
>>> App.getDocument('MedicineBox').getObject('MultiTransform004').ViewObject.DisplayMode=getattr(App.getDocument('MedicineBox').getObject('Pocket008').getLinkedObject(True).ViewObject,'DisplayMode',App.getDocument('MedicineBox').getObject('MultiTransform004').ViewObject.DisplayMode)
>>> Gui.getDocument('MedicineBox').setEdit(App.getDocument('MedicineBox').getObject('Part001'), 0, 'Body003.MultiTransform004.')
>>> Gui.Selection.clearSelection()
>>> App.getDocument('MedicineBox').getObject('Body003').Tip = App.getDocument('MedicineBox').getObject('MultiTransform004')
>>> App.ActiveDocument.recompute()
>>> ### End command PartDesign_MultiTransform
>>> # Gui.Selection.clearSelection()
>>> App.getDocument('MedicineBox').getObject('Body003').newObject('PartDesign::Mirrored','Mirrored008')
>>> App.getDocument('MedicineBox').getObject('Mirrored008').MirrorPlane = (App.getDocument('MedicineBox').getObject('Sketch014'),['V_Axis'])
>>> App.getDocument('MedicineBox').getObject('Pocket008').Visibility = False
>>> App.getDocument('MedicineBox').getObject('Mirrored008').Visibility = False
>>> App.getDocument('MedicineBox').getObject('MultiTransform004').Visibility = True
>>> App.getDocument('MedicineBox').getObject('Body003').newObject('PartDesign::Mirrored','Mirrored009')
>>> App.getDocument('MedicineBox').getObject('Mirrored009').MirrorPlane = (App.getDocument('MedicineBox').getObject('Sketch014'),['V_Axis'])
>>> App.getDocument('MedicineBox').getObject('Mirrored009').Visibility = False
>>> App.getDocument('MedicineBox').getObject('MultiTransform004').Visibility = True
>>> App.getDocument('MedicineBox').getObject('MultiTransform004').Transformations = [App.getDocument('MedicineBox').getObject('Mirrored008'),App.getDocument('MedicineBox').getObject('Mirrored009'),]
>>> App.getDocument('MedicineBox').recompute()
>>> App.getDocument('MedicineBox').getObject('Pocket008').Visibility = False
>>> Gui.getDocument('MedicineBox').resetEdit()
>>> App.getDocument('MedicineBox').getObject('MultiTransform004').Visibility = True
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.MultiTransform004.')
>>> Gui.runCommand('PartDesign_MultiTransform',0)
>>> Gui.runCommand('PartDesign_MultiTransform',0)
>>> Gui.ActiveDocument.setEdit(App.getDocument('MedicineBox').getObject('MultiTransform004'), 0)
>>> # Gui.Selection.clearSelection()
>>> App.getDocument('MedicineBox').getObject('Body003').newObject('PartDesign::Mirrored','Mirrored010')
>>> App.getDocument('MedicineBox').getObject('Mirrored010').MirrorPlane = (App.getDocument('MedicineBox').getObject('Sketch014'),['V_Axis'])
>>> App.getDocument('MedicineBox').getObject('Mirrored010').Visibility = False
>>> App.getDocument('MedicineBox').getObject('MultiTransform004').Visibility = True
>>> App.getDocument('MedicineBox').getObject('MultiTransform004').Visibility = True
>>> App.getDocument('MedicineBox').getObject('MultiTransform004').Visibility = True
>>> App.getDocument('MedicineBox').getObject('Body003').newObject('PartDesign::Mirrored','Mirrored011')
>>> App.getDocument('MedicineBox').getObject('Mirrored011').MirrorPlane = (App.getDocument('MedicineBox').getObject('Sketch014'),['V_Axis'])
>>> App.getDocument('MedicineBox').getObject('Mirrored011').Visibility = False
>>> App.getDocument('MedicineBox').getObject('MultiTransform004').Visibility = True
>>> App.getDocument('MedicineBox').getObject('MultiTransform004').Transformations = [App.getDocument('MedicineBox').getObject('Mirrored008'),App.getDocument('MedicineBox').getObject('Mirrored009'),App.getDocument('MedicineBox').getObject('Mirrored010'),App.getDocument('MedicineBox').getObject('Mirrored011'),]
>>> App.getDocument('MedicineBox').recompute()
>>> App.getDocument('MedicineBox').getObject('Pocket008').Visibility = False
>>> Gui.getDocument('MedicineBox').resetEdit()
>>> App.getDocument('MedicineBox').getObject('MultiTransform004').Visibility = True
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.MultiTransform003.')
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.DatumPlane006.')
>>> Gui.runCommand('Std_ToggleVisibility',0)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.MultiTransform004.Face89',-42.9203,56.2361,48.2212)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.MultiTransform004.Face90',-4.63117,56.0844,47.3494)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.MultiTransform004.Face93',8.17995,55.2106,48.0956)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.MultiTransform004.Face102',45.4448,56.0356,47.2253)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.MultiTransform004.Face92',46.436,6.5267,47.4993)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.MultiTransform004.Face78',46.3475,-5.19115,48.408)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.MultiTransform004.Face68',46.4271,-53.4009,47.9434)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.MultiTransform004.Face91',8.16761,7.22849,46.9514)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.MultiTransform004.Face80',-4.13001,7.65895,47.3743)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.MultiTransform004.Face79',-41.8212,7.21231,47.7008)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.MultiTransform004.Face65',-41.9622,-4.58342,47.9929)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.MultiTransform004.Face66',-4.66085,-3.90002,47.1283)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.MultiTransform004.Face77',7.90832,-4.39586,47.8069)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.MultiTransform004.Face67',8.11116,-52.6897,47.2153)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.MultiTransform004.Face64',-4.28622,-52.2027,47.0323)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.MultiTransform004.Face55',-41.9949,-52.536,47.5768)
>>> ### Begin command PartDesign_Fillet
>>> App.getDocument('MedicineBox').getObject('Body003').newObject('PartDesign::Fillet','Fillet008')
>>> App.getDocument('MedicineBox').getObject('Fillet008').Base = (App.getDocument('MedicineBox').getObject('MultiTransform004'),['Face89','Face90','Face93','Face102','Face92','Face78','Face68','Face91','Face80','Face79','Face65','Face66','Face77','Face67','Face64','Face55',])
>>> Gui.Selection.clearSelection()
>>> App.getDocument('MedicineBox').getObject('MultiTransform004').Visibility = False
>>> App.ActiveDocument.recompute()
>>> App.getDocument('MedicineBox').getObject('Fillet008').ViewObject.ShapeColor=getattr(App.getDocument('MedicineBox').getObject('MultiTransform004').getLinkedObject(True).ViewObject,'ShapeColor',App.getDocument('MedicineBox').getObject('Fillet008').ViewObject.ShapeColor)
>>> App.getDocument('MedicineBox').getObject('Fillet008').ViewObject.LineColor=getattr(App.getDocument('MedicineBox').getObject('MultiTransform004').getLinkedObject(True).ViewObject,'LineColor',App.getDocument('MedicineBox').getObject('Fillet008').ViewObject.LineColor)
>>> App.getDocument('MedicineBox').getObject('Fillet008').ViewObject.PointColor=getattr(App.getDocument('MedicineBox').getObject('MultiTransform004').getLinkedObject(True).ViewObject,'PointColor',App.getDocument('MedicineBox').getObject('Fillet008').ViewObject.PointColor)
>>> App.getDocument('MedicineBox').getObject('Fillet008').ViewObject.Transparency=getattr(App.getDocument('MedicineBox').getObject('MultiTransform004').getLinkedObject(True).ViewObject,'Transparency',App.getDocument('MedicineBox').getObject('Fillet008').ViewObject.Transparency)
>>> App.getDocument('MedicineBox').getObject('Fillet008').ViewObject.DisplayMode=getattr(App.getDocument('MedicineBox').getObject('MultiTransform004').getLinkedObject(True).ViewObject,'DisplayMode',App.getDocument('MedicineBox').getObject('Fillet008').ViewObject.DisplayMode)
>>> Gui.getDocument('MedicineBox').setEdit(App.getDocument('MedicineBox').getObject('Part001'), 0, 'Body003.Fillet008.')
>>> Gui.Selection.clearSelection()
>>> ### End command PartDesign_Fillet
>>> # Gui.Selection.clearSelection()
>>> App.getDocument('MedicineBox').getObject('Fillet008').Radius = 1.000000
>>> App.getDocument('MedicineBox').getObject('Fillet008').Base = (App.getDocument('MedicineBox').getObject('MultiTransform004'),["Face89","Face90","Face93","Face102","Face92","Face78","Face68","Face91","Face80","Face79","Face65","Face66","Face77","Face67","Face64","Face55",])
>>> App.getDocument('MedicineBox').recompute()
>>> App.getDocument('MedicineBox').getObject('Fillet008').Radius = 1.000000
>>> App.getDocument('MedicineBox').getObject('Fillet008').Base = (App.getDocument('MedicineBox').getObject('MultiTransform004'),["Face89","Face90","Face93","Face102","Face92","Face78","Face68","Face91","Face80","Face79","Face65","Face66","Face77","Face67","Face64","Face55",])
>>> App.getDocument('MedicineBox').recompute()
>>> App.getDocument('MedicineBox').recompute()
>>> Gui.getDocument('MedicineBox').resetEdit()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.MultiTransform004.Face89',-41.6748,54.8677,48.3191)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.MultiTransform004.Face90',-5.48725,56.4297,48.7958)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.MultiTransform004.Face93',7.83749,55.6877,48.1203)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.MultiTransform004.Face89',-41.9047,55.3333,46.7774)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.MultiTransform004.Face90',-4.11733,55.6413,48.5181)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.MultiTransform004.Face93',8.02291,55.4381,48.2127)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.MultiTransform004.Face102',46.0469,55.4034,48.8263)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.MultiTransform004.Face79',-42.1159,7.63925,48.1581)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.MultiTransform004.Face80',-3.89411,7.31791,47.1982)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.MultiTransform004.Face91',8.34669,6.81099,48.0651)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.MultiTransform004.Face92',45.852,7.67491,48.5352)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.MultiTransform004.Face78',45.7668,-4.24963,48.8035)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.MultiTransform004.Face77',8.3315,-5.14897,48.732)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.MultiTransform004.Face66',-4.13456,-4.33702,47.328)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.MultiTransform004.Face65',-42.1422,-4.33023,47.8922)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.MultiTransform004.Face55',-42.4287,-52.0764,48.4383)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.MultiTransform004.Face64',-4.20837,-52.2716,48.6217)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.MultiTransform004.Face67',7.95412,-52.4622,47.3324)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.MultiTransform004.Face68',45.7236,-52.2113,47.4536)
>>> ### Begin command PartDesign_Fillet
>>> App.getDocument('MedicineBox').getObject('Body003').newObject('PartDesign::Fillet','Fillet008')
>>> App.getDocument('MedicineBox').getObject('Fillet008').Base = (App.getDocument('MedicineBox').getObject('MultiTransform004'),['Face89','Face90','Face93','Face102','Face79','Face80','Face91','Face92','Face78','Face77','Face66','Face65','Face55','Face64','Face67','Face68',])
>>> Gui.Selection.clearSelection()
>>> App.getDocument('MedicineBox').getObject('MultiTransform004').Visibility = False
>>> App.ActiveDocument.recompute()
>>> App.getDocument('MedicineBox').getObject('Fillet008').ViewObject.ShapeColor=getattr(App.getDocument('MedicineBox').getObject('MultiTransform004').getLinkedObject(True).ViewObject,'ShapeColor',App.getDocument('MedicineBox').getObject('Fillet008').ViewObject.ShapeColor)
>>> App.getDocument('MedicineBox').getObject('Fillet008').ViewObject.LineColor=getattr(App.getDocument('MedicineBox').getObject('MultiTransform004').getLinkedObject(True).ViewObject,'LineColor',App.getDocument('MedicineBox').getObject('Fillet008').ViewObject.LineColor)
>>> App.getDocument('MedicineBox').getObject('Fillet008').ViewObject.PointColor=getattr(App.getDocument('MedicineBox').getObject('MultiTransform004').getLinkedObject(True).ViewObject,'PointColor',App.getDocument('MedicineBox').getObject('Fillet008').ViewObject.PointColor)
>>> App.getDocument('MedicineBox').getObject('Fillet008').ViewObject.Transparency=getattr(App.getDocument('MedicineBox').getObject('MultiTransform004').getLinkedObject(True).ViewObject,'Transparency',App.getDocument('MedicineBox').getObject('Fillet008').ViewObject.Transparency)
>>> App.getDocument('MedicineBox').getObject('Fillet008').ViewObject.DisplayMode=getattr(App.getDocument('MedicineBox').getObject('MultiTransform004').getLinkedObject(True).ViewObject,'DisplayMode',App.getDocument('MedicineBox').getObject('Fillet008').ViewObject.DisplayMode)
>>> Gui.getDocument('MedicineBox').setEdit(App.getDocument('MedicineBox').getObject('Part001'), 0, 'Body003.Fillet008.')
>>> Gui.Selection.clearSelection()
>>> ### End command PartDesign_Fillet
>>> # Gui.Selection.clearSelection()
>>> App.getDocument('MedicineBox').getObject('Fillet008').Radius = 1.000000
>>> App.getDocument('MedicineBox').getObject('Fillet008').Base = (App.getDocument('MedicineBox').getObject('MultiTransform004'),["Face89","Face90","Face93","Face102","Face79","Face80","Face91","Face92","Face78","Face77","Face66","Face65","Face55","Face64","Face67","Face68",])
>>> App.getDocument('MedicineBox').recompute()
>>> App.getDocument('MedicineBox').getObject('MultiTransform004').Visibility = False
>>> Gui.getDocument('MedicineBox').resetEdit()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Fillet008.Face78',-2.5,34.0251,32.1427)
>>> ### Begin command PartDesign_Plane
>>> App.getDocument('MedicineBox').getObject('Body003').newObject('PartDesign::Plane','DatumPlane007')
>>> App.getDocument('MedicineBox').getObject('DatumPlane007').Support = [(App.getDocument('MedicineBox').getObject('Fillet008'),'Face78')]
>>> App.getDocument('MedicineBox').getObject('DatumPlane007').MapMode = 'FlatFace'
>>> App.activeDocument().recompute()
>>> Gui.getDocument('MedicineBox').setEdit(App.getDocument('MedicineBox').getObject('Part001'), 0, 'Body003.DatumPlane007.')
>>> import Show
>>> from Show.Containers import isAContainer
>>> _tv_DatumPlane007 = Show.TempoVis(App.ActiveDocument, tag= 'PartGui::TaskAttacher')
>>> tvObj = App.getDocument('MedicineBox').getObject('DatumPlane007')
>>> dep_features = _tv_DatumPlane007.get_all_dependent(App.getDocument('MedicineBox').getObject('Part001'), 'Body003.DatumPlane007.')
>>> dep_features = [o for o in dep_features if not isAContainer(o)]
>>> if tvObj.isDerivedFrom('PartDesign::CoordinateSystem'):
>>> 	visible_features = [feat for feat in tvObj.InList if feat.isDerivedFrom('PartDesign::FeaturePrimitive')]
>>> 	dep_features = [feat for feat in dep_features if feat not in visible_features]
>>> 	del(visible_features)
>>> _tv_DatumPlane007.hide(dep_features)
>>> del(dep_features)
>>> if not tvObj.isDerivedFrom('PartDesign::CoordinateSystem'):
>>> 		if len(tvObj.Support) > 0:
>>> 			_tv_DatumPlane007.show([lnk[0] for lnk in tvObj.Support])
>>> del(tvObj)
>>> ### End command PartDesign_Plane
>>> # Gui.Selection.clearSelection()
>>> App.getDocument('MedicineBox').getObject('DatumPlane007').AttachmentOffset = App.Placement(App.Vector(0.0000000000, 0.0000000000, 0.0000000000),  App.Rotation(0.0000000000, 0.0000000000, 0.0000000000))
>>> App.getDocument('MedicineBox').getObject('DatumPlane007').MapReversed = False
>>> App.getDocument('MedicineBox').getObject('DatumPlane007').Support = [(App.getDocument('MedicineBox').getObject('Fillet008'),'Face78')]
>>> App.getDocument('MedicineBox').getObject('DatumPlane007').MapPathParameter = 0.000000
>>> App.getDocument('MedicineBox').getObject('DatumPlane007').MapMode = 'FlatFace'
>>> App.getDocument('MedicineBox').getObject('DatumPlane007').recompute()
>>> Gui.getDocument('MedicineBox').resetEdit()
>>> _tv_DatumPlane007.restore()
>>> del(_tv_DatumPlane007)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.DatumPlane007.Plane',-2.5,64.6537,51.8814)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.DatumPlane007.',-2.5,63.0684,48.1931)
>>> ### Begin command PartDesign_NewSketch
>>> App.getDocument('MedicineBox').getObject('Body003').newObject('Sketcher::SketchObject','Sketch015')
>>> App.getDocument('MedicineBox').getObject('Sketch015').Support = (App.getDocument('MedicineBox').getObject('DatumPlane007'),'')
>>> App.getDocument('MedicineBox').getObject('Sketch015').MapMode = 'FlatFace'
>>> App.ActiveDocument.recompute()
>>> Gui.getDocument('MedicineBox').setEdit(App.getDocument('MedicineBox').getObject('Part001'), 0, 'Body003.Sketch015.')
>>> ActiveSketch = App.getDocument('MedicineBox').getObject('Sketch015')
>>> tv = Show.TempoVis(App.ActiveDocument, tag= ActiveSketch.ViewObject.TypeId)
>>> ActiveSketch.ViewObject.TempoVis = tv
>>> if ActiveSketch.ViewObject.EditingWorkbench:
>>>   tv.activateWorkbench(ActiveSketch.ViewObject.EditingWorkbench)
>>> if ActiveSketch.ViewObject.HideDependent:
>>>   tv.hide(tv.get_all_dependent(App.getDocument('MedicineBox').getObject('Part001'), 'Body003.Sketch015.'))
>>> if ActiveSketch.ViewObject.ShowSupport:
>>>   tv.show([ref[0] for ref in ActiveSketch.Support if not ref[0].isDerivedFrom("PartDesign::Plane")])
>>> if ActiveSketch.ViewObject.ShowLinks:
>>>   tv.show([ref[0] for ref in ActiveSketch.ExternalGeometry])
>>> tv.sketchClipPlane(ActiveSketch, ActiveSketch.ViewObject.SectionView)
>>> tv.hide(ActiveSketch)
>>> del(tv)
>>> del(ActiveSketch)
>>>
>>> import PartDesignGui
>>> ActiveSketch = App.getDocument('MedicineBox').getObject('Sketch015')
>>> if ActiveSketch.ViewObject.RestoreCamera:
>>>   ActiveSketch.ViewObject.TempoVis.saveCamera()
>>>   if ActiveSketch.ViewObject.ForceOrtho:
>>>     ActiveSketch.ViewObject.Document.ActiveView.setCameraType('Orthographic')
>>>
>>> ### End command PartDesign_NewSketch
>>> # Gui.Selection.clearSelection()
>>> ### Begin command Sketcher_ViewSection
>>> ActiveSketch.ViewObject.TempoVis.sketchClipPlane(ActiveSketch)
>>> ### End command Sketcher_ViewSection
>>> Gui.runCommand('Sketcher_CreatePolyline',0)
>>> App.getDocument('MedicineBox').getObject('Sketch015').addGeometry(Part.LineSegment(App.Vector(-57.200665,0.247629,0),App.Vector(-44.930607,44.539566,0)),False)
>>> App.getDocument('MedicineBox').getObject('Sketch015').addConstraint(Sketcher.Constraint('PointOnObject',0,1,-1))
>>> App.getDocument('MedicineBox').getObject('Sketch015').addGeometry(Part.LineSegment(App.Vector(-44.930607,44.539566,0),App.Vector(-15.302893,44.539566,0)),False)
>>> App.getDocument('MedicineBox').getObject('Sketch015').addConstraint(Sketcher.Constraint('Coincident',0,2,1,1))
>>> App.getDocument('MedicineBox').getObject('Sketch015').addConstraint(Sketcher.Constraint('Horizontal',1))
>>> App.getDocument('MedicineBox').getObject('Sketch015').addGeometry(Part.LineSegment(App.Vector(-15.302893,44.539566,0),App.Vector(-2.583921,-0.051640,0)),False)
>>> App.getDocument('MedicineBox').getObject('Sketch015').addConstraint(Sketcher.Constraint('Coincident',1,2,2,1))
>>> App.getDocument('MedicineBox').getObject('Sketch015').addConstraint(Sketcher.Constraint('PointOnObject',2,2,-1))
>>> App.getDocument('MedicineBox').getObject('Sketch015').addGeometry(Part.LineSegment(App.Vector(-2.583921,0.000000,0),App.Vector(-57.051033,-0.201276,0)),False)
>>> App.getDocument('MedicineBox').getObject('Sketch015').addConstraint(Sketcher.Constraint('Coincident',2,2,3,1))
>>> App.getDocument('MedicineBox').getObject('Sketch015').addConstraint(Sketcher.Constraint('Coincident',3,2,0,1))
>>> App.getDocument('MedicineBox').getObject('Sketch015').addConstraint(Sketcher.Constraint('Horizontal',3))
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch015.Edge2',-2.508,33.4087,44.5396,False)
>>> ### Begin command Sketcher_ConstrainDistanceX
>>> App.getDocument('MedicineBox').getObject('Sketch015').addConstraint(Sketcher.Constraint('DistanceX',1,1,1,2,29.627714))
>>> App.getDocument('MedicineBox').getObject('Sketch015').setDatum(7,App.Units.Quantity('30.000000 mm'))
>>> ### End command Sketcher_ConstrainDistanceX
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch015.Edge4',-2.508,47.624,0,False)
>>> ### Begin command Sketcher_ConstrainDistanceX
>>> App.getDocument('MedicineBox').getObject('Sketch015').addConstraint(Sketcher.Constraint('DistanceX',3,2,3,1,54.467112))
>>> App.getDocument('MedicineBox').getObject('Sketch015').setDatum(8,App.Units.Quantity('55.000000 mm'))
>>> ### End command Sketcher_ConstrainDistanceX
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch015.Vertex2',-2.512,45.0013,44.5396,False)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch015.Edge2',-2.508,21.5876,44.5396,False)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch015.Edge4',-2.508,30.416,0,False)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch015.Edge2',-2.508,33.708,44.5396,False)
>>> Gui.runCommand('Sketcher_ConstrainDistanceY',0)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch015.Edge2',-2.508,37.8978,44.5396,False)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch015.Edge4',-2.508,41.0401,0,False)
>>> Gui.runCommand('Sketcher_ConstrainDistanceY',0)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch015.Vertex1',-2.512,57.3993,0,False)
>>> ### Begin command Sketcher_ConstrainDistanceY
>>> App.getDocument('MedicineBox').getObject('Sketch015').addConstraint(Sketcher.Constraint('DistanceY',0,1,0.000000))
>>> ### End command Sketcher_ConstrainDistanceY
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch015.Vertex2',-2.512,45.0013,44.5396,False)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch015.Vertex1',-2.512,57.3993,0,False)
>>> ### Begin command Sketcher_ConstrainDistanceY
>>> App.getDocument('MedicineBox').getObject('Sketch015').addConstraint(Sketcher.Constraint('DistanceY',0,1,0,2,44.539566))
>>> App.getDocument('MedicineBox').getObject('Sketch015').setDatum(9,App.Units.Quantity('45.000000 mm'))
>>> ### End command Sketcher_ConstrainDistanceY
>>> # Gui.Selection.clearSelection()
>>> App.getDocument('MedicineBox').getObject('Sketch015').movePoint(1,0,App.Vector(29.029177,5.985394,0),1)
>>> App.getDocument('MedicineBox').getObject('Sketch015').movePoint(3,0,App.Vector(27.532823,0.748175,0),1)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch015.Vertex2',-2.512,15.9721,45,False)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch015.Vertex4',-2.512,-14.0279,45,False)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch015.V_Axis',-2.501,0,64.6676,False)
>>> ### Begin command Sketcher_ConstrainSymmetric
>>> App.getDocument('MedicineBox').getObject('Sketch015').addConstraint(Sketcher.Constraint('Symmetric',0,2,1,2,-2))
>>> ### End command Sketcher_ConstrainSymmetric
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch015.Vertex1',-2.512,29.8664,0,False)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch015.Vertex6',-2.512,-25.1336,0,False)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch015.V_Axis',-2.501,0,-12.0425,False)
>>> ### Begin command Sketcher_ConstrainSymmetric
>>> App.getDocument('MedicineBox').getObject('Sketch015').addConstraint(Sketcher.Constraint('Symmetric',0,1,2,2,-2))
>>> ### End command Sketcher_ConstrainSymmetric
>>> # Gui.Selection.clearSelection()
>>> Gui.getDocument('MedicineBox').resetEdit()
>>> App.ActiveDocument.recompute()
>>> ActiveSketch = App.getDocument('MedicineBox').getObject('Sketch015')
>>> tv = ActiveSketch.ViewObject.TempoVis
>>> if tv:
>>>   tv.restore()
>>> ActiveSketch.ViewObject.TempoVis = None
>>> del(tv)
>>> del(ActiveSketch)
>>>
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch015.')
>>> App.getDocument('MedicineBox').recompute()
>>> FreeCAD.getDocument('MedicineBox').getObject('Sketch015').AttachmentOffset = App.Placement(App.Vector(0.00,1.00,0.00),App.Rotation(App.Vector(0.00,0.00,1.00),0.00))
>>>
>>> FreeCAD.getDocument('MedicineBox').getObject('Sketch015').AttachmentOffset = App.Placement(App.Vector(0.00,10.00,0.00),App.Rotation(App.Vector(0.00,0.00,1.00),0.00))
>>>
>>> FreeCAD.getDocument('MedicineBox').getObject('Sketch015').AttachmentOffset = App.Placement(App.Vector(0.00,0.00,0.00),App.Rotation(App.Vector(0.00,0.00,1.00),0.00))
>>>
>>> FreeCAD.getDocument('MedicineBox').getObject('Sketch015').AttachmentOffset = App.Placement(App.Vector(0.00,0.00,1.00),App.Rotation(App.Vector(0.00,0.00,1.00),0.00))
>>>
>>> FreeCAD.getDocument('MedicineBox').getObject('Sketch015').AttachmentOffset = App.Placement(App.Vector(0.00,0.00,10.00),App.Rotation(App.Vector(0.00,0.00,1.00),0.00))
>>>
>>> FreeCAD.getDocument('MedicineBox').getObject('Sketch015').AttachmentOffset = App.Placement(App.Vector(0.00,0.00,0.00),App.Rotation(App.Vector(0.00,0.00,1.00),0.00))
>>>
>>> FreeCAD.getDocument('MedicineBox').getObject('Sketch015').AttachmentOffset = App.Placement(App.Vector(3.00,0.00,0.00),App.Rotation(App.Vector(0.00,0.00,1.00),0.00))
>>>
>>> FreeCAD.getDocument('MedicineBox').getObject('Sketch015').AttachmentOffset = App.Placement(App.Vector(30.00,0.00,0.00),App.Rotation(App.Vector(0.00,0.00,1.00),0.00))
>>>
>>> FreeCAD.getDocument('MedicineBox').getObject('Sketch015').AttachmentOffset = App.Placement(App.Vector(3.00,0.00,0.00),App.Rotation(App.Vector(0.00,0.00,1.00),0.00))
>>>
>>> FreeCAD.getDocument('MedicineBox').getObject('Sketch015').AttachmentOffset = App.Placement(App.Vector(1.00,0.00,0.00),App.Rotation(App.Vector(0.00,0.00,1.00),0.00))
>>>
>>> FreeCAD.getDocument('MedicineBox').getObject('Sketch015').AttachmentOffset = App.Placement(App.Vector(-3.00,0.00,0.00),App.Rotation(App.Vector(0.00,0.00,1.00),0.00))
>>>
>>> FreeCAD.getDocument('MedicineBox').getObject('Sketch015').AttachmentOffset = App.Placement(App.Vector(-30.00,0.00,0.00),App.Rotation(App.Vector(0.00,0.00,1.00),0.00))
>>>
>>> ### Begin command PartDesign_Pocket
>>> App.getDocument('MedicineBox').getObject('Body003').newObject('PartDesign::Pocket','Pocket009')
>>> App.getDocument('MedicineBox').getObject('Pocket009').Profile = App.getDocument('MedicineBox').getObject('Sketch015')
>>> App.getDocument('MedicineBox').getObject('Pocket009').Length = 5
>>> App.ActiveDocument.recompute()
>>> App.getDocument('MedicineBox').getObject('Pocket009').ReferenceAxis = (App.getDocument('MedicineBox').getObject('Sketch015'),['N_Axis'])
>>> App.getDocument('MedicineBox').getObject('Sketch015').Visibility = False
>>> App.ActiveDocument.recompute()
>>> App.getDocument('MedicineBox').getObject('Pocket009').ViewObject.ShapeColor=getattr(App.getDocument('MedicineBox').getObject('Fillet008').getLinkedObject(True).ViewObject,'ShapeColor',App.getDocument('MedicineBox').getObject('Pocket009').ViewObject.ShapeColor)
>>> App.getDocument('MedicineBox').getObject('Pocket009').ViewObject.LineColor=getattr(App.getDocument('MedicineBox').getObject('Fillet008').getLinkedObject(True).ViewObject,'LineColor',App.getDocument('MedicineBox').getObject('Pocket009').ViewObject.LineColor)
>>> App.getDocument('MedicineBox').getObject('Pocket009').ViewObject.PointColor=getattr(App.getDocument('MedicineBox').getObject('Fillet008').getLinkedObject(True).ViewObject,'PointColor',App.getDocument('MedicineBox').getObject('Pocket009').ViewObject.PointColor)
>>> App.getDocument('MedicineBox').getObject('Pocket009').ViewObject.Transparency=getattr(App.getDocument('MedicineBox').getObject('Fillet008').getLinkedObject(True).ViewObject,'Transparency',App.getDocument('MedicineBox').getObject('Pocket009').ViewObject.Transparency)
>>> App.getDocument('MedicineBox').getObject('Pocket009').ViewObject.DisplayMode=getattr(App.getDocument('MedicineBox').getObject('Fillet008').getLinkedObject(True).ViewObject,'DisplayMode',App.getDocument('MedicineBox').getObject('Pocket009').ViewObject.DisplayMode)
>>> Gui.getDocument('MedicineBox').setEdit(App.getDocument('MedicineBox').getObject('Part001'), 0, 'Body003.Pocket009.')
>>> Gui.Selection.clearSelection()
>>> ### End command PartDesign_Pocket
>>> # Gui.Selection.clearSelection()
>>> Gui.runCommand('Std_Undo',0)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch015.')
>>> ### Begin command PartDesign_Pocket
>>> App.getDocument('MedicineBox').getObject('Body003').newObject('PartDesign::Pocket','Pocket009')
>>> App.getDocument('MedicineBox').getObject('Pocket009').Profile = App.getDocument('MedicineBox').getObject('Sketch015')
>>> App.getDocument('MedicineBox').getObject('Pocket009').Length = 5
>>> App.ActiveDocument.recompute()
>>> App.getDocument('MedicineBox').getObject('Pocket009').ReferenceAxis = (App.getDocument('MedicineBox').getObject('Sketch015'),['N_Axis'])
>>> App.getDocument('MedicineBox').getObject('Sketch015').Visibility = False
>>> App.ActiveDocument.recompute()
>>> App.getDocument('MedicineBox').getObject('Pocket009').ViewObject.ShapeColor=getattr(App.getDocument('MedicineBox').getObject('Fillet008').getLinkedObject(True).ViewObject,'ShapeColor',App.getDocument('MedicineBox').getObject('Pocket009').ViewObject.ShapeColor)
>>> App.getDocument('MedicineBox').getObject('Pocket009').ViewObject.LineColor=getattr(App.getDocument('MedicineBox').getObject('Fillet008').getLinkedObject(True).ViewObject,'LineColor',App.getDocument('MedicineBox').getObject('Pocket009').ViewObject.LineColor)
>>> App.getDocument('MedicineBox').getObject('Pocket009').ViewObject.PointColor=getattr(App.getDocument('MedicineBox').getObject('Fillet008').getLinkedObject(True).ViewObject,'PointColor',App.getDocument('MedicineBox').getObject('Pocket009').ViewObject.PointColor)
>>> App.getDocument('MedicineBox').getObject('Pocket009').ViewObject.Transparency=getattr(App.getDocument('MedicineBox').getObject('Fillet008').getLinkedObject(True).ViewObject,'Transparency',App.getDocument('MedicineBox').getObject('Pocket009').ViewObject.Transparency)
>>> App.getDocument('MedicineBox').getObject('Pocket009').ViewObject.DisplayMode=getattr(App.getDocument('MedicineBox').getObject('Fillet008').getLinkedObject(True).ViewObject,'DisplayMode',App.getDocument('MedicineBox').getObject('Pocket009').ViewObject.DisplayMode)
>>> Gui.getDocument('MedicineBox').setEdit(App.getDocument('MedicineBox').getObject('Part001'), 0, 'Body003.Pocket009.')
>>> Gui.Selection.clearSelection()
>>> ### End command PartDesign_Pocket
>>> # Gui.Selection.clearSelection()
>>> App.getDocument('MedicineBox').getObject('Pocket009').Length = 5.000000
>>> App.getDocument('MedicineBox').getObject('Pocket009').Length2 = 5.000000
>>> App.getDocument('MedicineBox').getObject('Pocket009').TaperAngle = 0.000000
>>> App.getDocument('MedicineBox').getObject('Pocket009').TaperAngle2 = 0.000000
>>> App.getDocument('MedicineBox').getObject('Pocket009').UseCustomVector = 0
>>> App.getDocument('MedicineBox').getObject('Pocket009').Direction = (1, 0, 0)
>>> App.getDocument('MedicineBox').getObject('Pocket009').ReferenceAxis = (App.getDocument('MedicineBox').getObject('Sketch015'), ['N_Axis'])
>>> App.getDocument('MedicineBox').getObject('Pocket009').AlongSketchNormal = 1
>>> App.getDocument('MedicineBox').getObject('Pocket009').Type = 0
>>> App.getDocument('MedicineBox').getObject('Pocket009').UpToFace = None
>>> App.getDocument('MedicineBox').getObject('Pocket009').Reversed = 0
>>> App.getDocument('MedicineBox').getObject('Pocket009').Midplane = 0
>>> App.getDocument('MedicineBox').getObject('Pocket009').Offset = 0
>>> App.getDocument('MedicineBox').recompute()
>>> App.getDocument('MedicineBox').getObject('Fillet008').Visibility = False
>>> Gui.getDocument('MedicineBox').resetEdit()
>>> App.getDocument('MedicineBox').getObject('Sketch015').Visibility = False
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.DatumPlane007.',-2.5,-10.4786,-13.3664)
>>> Gui.runCommand('Std_ToggleVisibility',0)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Pocket009.')
>>> ### Begin command PartDesign_Mirrored
>>> App.getDocument('MedicineBox').getObject('Body003').newObject('PartDesign::Mirrored','Mirrored012')
>>> App.ActiveDocument.recompute()
>>> App.getDocument('MedicineBox').getObject('Mirrored012').Originals = [App.getDocument('MedicineBox').getObject('Pocket009'),]
>>> App.getDocument('MedicineBox').getObject('Mirrored012').MirrorPlane = (App.getDocument('MedicineBox').getObject('Sketch015'), ['V_Axis'])
>>> App.ActiveDocument.recompute()
>>> App.getDocument('MedicineBox').getObject('Mirrored012').ViewObject.ShapeColor=getattr(App.getDocument('MedicineBox').getObject('Pocket009').getLinkedObject(True).ViewObject,'ShapeColor',App.getDocument('MedicineBox').getObject('Mirrored012').ViewObject.ShapeColor)
>>> App.getDocument('MedicineBox').getObject('Mirrored012').ViewObject.LineColor=getattr(App.getDocument('MedicineBox').getObject('Pocket009').getLinkedObject(True).ViewObject,'LineColor',App.getDocument('MedicineBox').getObject('Mirrored012').ViewObject.LineColor)
>>> App.getDocument('MedicineBox').getObject('Mirrored012').ViewObject.PointColor=getattr(App.getDocument('MedicineBox').getObject('Pocket009').getLinkedObject(True).ViewObject,'PointColor',App.getDocument('MedicineBox').getObject('Mirrored012').ViewObject.PointColor)
>>> App.getDocument('MedicineBox').getObject('Mirrored012').ViewObject.Transparency=getattr(App.getDocument('MedicineBox').getObject('Pocket009').getLinkedObject(True).ViewObject,'Transparency',App.getDocument('MedicineBox').getObject('Mirrored012').ViewObject.Transparency)
>>> App.getDocument('MedicineBox').getObject('Mirrored012').ViewObject.DisplayMode=getattr(App.getDocument('MedicineBox').getObject('Pocket009').getLinkedObject(True).ViewObject,'DisplayMode',App.getDocument('MedicineBox').getObject('Mirrored012').ViewObject.DisplayMode)
>>> Gui.getDocument('MedicineBox').setEdit(App.getDocument('MedicineBox').getObject('Part001'), 0, 'Body003.Mirrored012.')
>>> Gui.Selection.clearSelection()
>>> App.getDocument('MedicineBox').getObject('Body003').Tip = App.getDocument('MedicineBox').getObject('Mirrored012')
>>> App.ActiveDocument.recompute()
>>> ### End command PartDesign_Mirrored
>>> # Gui.Selection.clearSelection()
>>> App.getDocument('MedicineBox').getObject('Mirrored012').Visibility = True
>>> App.getDocument('MedicineBox').getObject('Mirrored012').Visibility = True
>>> App.getDocument('MedicineBox').getObject('Mirrored012').Visibility = True
>>> App.getDocument('MedicineBox').getObject('Mirrored012').MirrorPlane = (App.getDocument('MedicineBox').getObject('XZ_Plane005'), [''])
>>> App.getDocument('MedicineBox').getObject('Mirrored012').Visibility = True
>>> App.getDocument('MedicineBox').recompute()
>>> App.getDocument('MedicineBox').getObject('Pocket009').Visibility = False
>>> Gui.getDocument('MedicineBox').resetEdit()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Mirrored012.Face58',-24.4228,-2.5,26.2255)
>>> ### Begin command PartDesign_Plane
>>> App.getDocument('MedicineBox').getObject('Body003').newObject('PartDesign::Plane','DatumPlane008')
>>> App.getDocument('MedicineBox').getObject('DatumPlane008').Support = [(App.getDocument('MedicineBox').getObject('Mirrored012'),'Face58')]
>>> App.getDocument('MedicineBox').getObject('DatumPlane008').MapMode = 'FlatFace'
>>> App.activeDocument().recompute()
>>> Gui.getDocument('MedicineBox').setEdit(App.getDocument('MedicineBox').getObject('Part001'), 0, 'Body003.DatumPlane008.')
>>> import Show
>>> from Show.Containers import isAContainer
>>> _tv_DatumPlane008 = Show.TempoVis(App.ActiveDocument, tag= 'PartGui::TaskAttacher')
>>> tvObj = App.getDocument('MedicineBox').getObject('DatumPlane008')
>>> dep_features = _tv_DatumPlane008.get_all_dependent(App.getDocument('MedicineBox').getObject('Part001'), 'Body003.DatumPlane008.')
>>> dep_features = [o for o in dep_features if not isAContainer(o)]
>>> if tvObj.isDerivedFrom('PartDesign::CoordinateSystem'):
>>> 	visible_features = [feat for feat in tvObj.InList if feat.isDerivedFrom('PartDesign::FeaturePrimitive')]
>>> 	dep_features = [feat for feat in dep_features if feat not in visible_features]
>>> 	del(visible_features)
>>> _tv_DatumPlane008.hide(dep_features)
>>> del(dep_features)
>>> if not tvObj.isDerivedFrom('PartDesign::CoordinateSystem'):
>>> 		if len(tvObj.Support) > 0:
>>> 			_tv_DatumPlane008.show([lnk[0] for lnk in tvObj.Support])
>>> del(tvObj)
>>> ### End command PartDesign_Plane
>>> # Gui.Selection.clearSelection()
>>> App.getDocument('MedicineBox').getObject('DatumPlane008').AttachmentOffset = App.Placement(App.Vector(0.0000000000, 0.0000000000, 0.0000000000),  App.Rotation(0.0000000000, 0.0000000000, 0.0000000000))
>>> App.getDocument('MedicineBox').getObject('DatumPlane008').MapReversed = False
>>> App.getDocument('MedicineBox').getObject('DatumPlane008').Support = [(App.getDocument('MedicineBox').getObject('Mirrored012'),'Face58')]
>>> App.getDocument('MedicineBox').getObject('DatumPlane008').MapPathParameter = 0.000000
>>> App.getDocument('MedicineBox').getObject('DatumPlane008').MapMode = 'FlatFace'
>>> App.getDocument('MedicineBox').getObject('DatumPlane008').recompute()
>>> Gui.getDocument('MedicineBox').resetEdit()
>>> _tv_DatumPlane008.restore()
>>> del(_tv_DatumPlane008)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.DatumPlane008.Plane',-56.4063,-2.50001,46.5404)
>>> ### Begin command PartDesign_NewSketch
>>> App.getDocument('MedicineBox').getObject('Body003').newObject('Sketcher::SketchObject','Sketch016')
>>> App.getDocument('MedicineBox').getObject('Sketch016').Support = (App.getDocument('MedicineBox').getObject('DatumPlane008'),'')
>>> App.getDocument('MedicineBox').getObject('Sketch016').MapMode = 'FlatFace'
>>> App.ActiveDocument.recompute()
>>> Gui.getDocument('MedicineBox').setEdit(App.getDocument('MedicineBox').getObject('Part001'), 0, 'Body003.Sketch016.')
>>> ActiveSketch = App.getDocument('MedicineBox').getObject('Sketch016')
>>> tv = Show.TempoVis(App.ActiveDocument, tag= ActiveSketch.ViewObject.TypeId)
>>> ActiveSketch.ViewObject.TempoVis = tv
>>> if ActiveSketch.ViewObject.EditingWorkbench:
>>>   tv.activateWorkbench(ActiveSketch.ViewObject.EditingWorkbench)
>>> if ActiveSketch.ViewObject.HideDependent:
>>>   tv.hide(tv.get_all_dependent(App.getDocument('MedicineBox').getObject('Part001'), 'Body003.Sketch016.'))
>>> if ActiveSketch.ViewObject.ShowSupport:
>>>   tv.show([ref[0] for ref in ActiveSketch.Support if not ref[0].isDerivedFrom("PartDesign::Plane")])
>>> if ActiveSketch.ViewObject.ShowLinks:
>>>   tv.show([ref[0] for ref in ActiveSketch.ExternalGeometry])
>>> tv.sketchClipPlane(ActiveSketch, ActiveSketch.ViewObject.SectionView)
>>> tv.hide(ActiveSketch)
>>> del(tv)
>>> del(ActiveSketch)
>>>
>>> import PartDesignGui
>>> ActiveSketch = App.getDocument('MedicineBox').getObject('Sketch016')
>>> if ActiveSketch.ViewObject.RestoreCamera:
>>>   ActiveSketch.ViewObject.TempoVis.saveCamera()
>>>   if ActiveSketch.ViewObject.ForceOrtho:
>>>     ActiveSketch.ViewObject.Document.ActiveView.setCameraType('Orthographic')
>>>
>>> ### End command PartDesign_NewSketch
>>> # Gui.Selection.clearSelection()
>>> ### Begin command Sketcher_ViewSection
>>> ActiveSketch.ViewObject.TempoVis.sketchClipPlane(ActiveSketch)
>>> ### End command Sketcher_ViewSection
>>> ### Begin command Sketcher_ViewSection
>>> ActiveSketch.ViewObject.TempoVis.sketchClipPlane(ActiveSketch)
>>> ### End command Sketcher_ViewSection
>>> ### Begin command Sketcher_ViewSection
>>> ActiveSketch.ViewObject.TempoVis.sketchClipPlane(ActiveSketch)
>>> ### End command Sketcher_ViewSection
>>> Gui.runCommand('Sketcher_CreatePolyline',0)
>>> App.getDocument('MedicineBox').getObject('Sketch016').addGeometry(Part.LineSegment(App.Vector(-47.279236,-0.091632,0),App.Vector(-34.975372,44.836105,0)),False)
>>> App.getDocument('MedicineBox').getObject('Sketch016').addConstraint(Sketcher.Constraint('PointOnObject',0,1,-1))
>>> App.getDocument('MedicineBox').getObject('Sketch016').addGeometry(Part.LineSegment(App.Vector(-34.975372,44.836105,0),App.Vector(-15.121410,44.836105,0)),False)
>>> App.getDocument('MedicineBox').getObject('Sketch016').addConstraint(Sketcher.Constraint('Coincident',0,2,1,1))
>>> App.getDocument('MedicineBox').getObject('Sketch016').addConstraint(Sketcher.Constraint('Horizontal',1))
>>> App.getDocument('MedicineBox').getObject('Sketch016').addGeometry(Part.LineSegment(App.Vector(-15.121410,44.836105,0),App.Vector(-2.537919,0.094789,0)),False)
>>> App.getDocument('MedicineBox').getObject('Sketch016').addConstraint(Sketcher.Constraint('Coincident',1,2,2,1))
>>> App.getDocument('MedicineBox').getObject('Sketch016').addGeometry(Part.LineSegment(App.Vector(-2.537919,0.094789,0),App.Vector(-47.279236,-0.091632,0)),False)
>>> App.getDocument('MedicineBox').getObject('Sketch016').addConstraint(Sketcher.Constraint('Coincident',2,2,3,1))
>>> App.getDocument('MedicineBox').getObject('Sketch016').addConstraint(Sketcher.Constraint('Coincident',3,2,0,1))
>>> App.getDocument('MedicineBox').getObject('Sketch016').addConstraint(Sketcher.Constraint('Horizontal',3))
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch016.Edge2',-28.4506,-2.50801,44.8361,False)
>>> ### Begin command Sketcher_ConstrainDistanceX
>>> App.getDocument('MedicineBox').getObject('Sketch016').addConstraint(Sketcher.Constraint('DistanceX',1,1,1,2,19.853962))
>>> App.getDocument('MedicineBox').getObject('Sketch016').setDatum(7,App.Units.Quantity('20.000000 mm'))
>>> ### End command Sketcher_ConstrainDistanceX
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch016.Edge4',-36.6532,-2.508,-9.53674e-10,False)
>>> ### Begin command Sketcher_ConstrainDistanceX
>>> App.getDocument('MedicineBox').getObject('Sketch016').addConstraint(Sketcher.Constraint('DistanceX',3,2,3,1,44.741317))
>>> App.getDocument('MedicineBox').getObject('Sketch016').setDatum(8,App.Units.Quantity('45.000000 mm'))
>>> ### End command Sketcher_ConstrainDistanceX
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch016.Vertex2',-35.0507,-2.51201,44.8361,False)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch016.Vertex1',-47.4672,-2.512,-1.43051e-09,False)
>>> ### Begin command Sketcher_ConstrainDistanceY
>>> App.getDocument('MedicineBox').getObject('Sketch016').addConstraint(Sketcher.Constraint('DistanceY',0,1,0,2,44.836105))
>>> App.getDocument('MedicineBox').getObject('Sketch016').setDatum(9,App.Units.Quantity('45.000000 mm'))
>>> ### End command Sketcher_ConstrainDistanceY
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch016.Vertex2',-35.0507,-2.51201,45,False)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch016.V_Axis',0,-2.50101,52.8523,False)
>>> Gui.runCommand('Sketcher_ConstrainSymmetric',0)
>>> # Gui.Selection.clearSelection()
>>> App.getDocument('MedicineBox').getObject('Sketch016').movePoint(1,0,App.Vector(24.794144,1.677795,0),1)
>>> App.getDocument('MedicineBox').getObject('Sketch016').movePoint(3,0,App.Vector(24.700938,1.957432,0),1)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch016.Vertex2',-10.2566,-2.51201,45,False)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch016.Vertex4',9.74344,-2.51201,45,False)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch016.V_Axis',0,-2.50101,54.8097,False)
>>> ### Begin command Sketcher_ConstrainSymmetric
>>> App.getDocument('MedicineBox').getObject('Sketch016').addConstraint(Sketcher.Constraint('Symmetric',0,2,1,2,-2))
>>> ### End command Sketcher_ConstrainSymmetric
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch016.Vertex1',-22.7663,-2.512,-1.43051e-09,False)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch016.Vertex6',22.2337,-2.512,-1.43051e-09,False)
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch016.V_Axis',0,-2.501,-13.3276,False)
>>> ### Begin command Sketcher_ConstrainSymmetric
>>> App.getDocument('MedicineBox').getObject('Sketch016').addConstraint(Sketcher.Constraint('Symmetric',0,1,2,2,-2))
>>> ### End command Sketcher_ConstrainSymmetric
>>> # Gui.Selection.clearSelection()
>>> Gui.getDocument('MedicineBox').resetEdit()
>>> App.ActiveDocument.recompute()
>>> ActiveSketch = App.getDocument('MedicineBox').getObject('Sketch016')
>>> tv = ActiveSketch.ViewObject.TempoVis
>>> if tv:
>>>   tv.restore()
>>> ActiveSketch.ViewObject.TempoVis = None
>>> del(tv)
>>> del(ActiveSketch)
>>>
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Sketch016.')
>>> App.getDocument('MedicineBox').recompute()
>>> FreeCAD.getDocument('MedicineBox').getObject('Sketch016').AttachmentOffset = App.Placement(App.Vector(0.00,0.00,-3.00),App.Rotation(App.Vector(0.00,0.00,1.00),0.00))
>>>
>>> FreeCAD.getDocument('MedicineBox').getObject('Sketch016').AttachmentOffset = App.Placement(App.Vector(0.00,0.00,-30.00),App.Rotation(App.Vector(0.00,0.00,1.00),0.00))
>>>
>>> Gui.runCommand('Std_Undo',0)
>>> FreeCAD.getDocument('MedicineBox').getObject('Sketch016').AttachmentOffset = App.Placement(App.Vector(0.00,3.00,0.00),App.Rotation(App.Vector(0.00,0.00,1.00),0.00))
>>>
>>> FreeCAD.getDocument('MedicineBox').getObject('Sketch016').AttachmentOffset = App.Placement(App.Vector(0.00,30.00,0.00),App.Rotation(App.Vector(0.00,0.00,1.00),0.00))
>>>
>>> FreeCAD.getDocument('MedicineBox').getObject('Sketch016').AttachmentOffset = App.Placement(App.Vector(0.00,0.00,0.00),App.Rotation(App.Vector(0.00,0.00,1.00),0.00))
>>>
>>> FreeCAD.getDocument('MedicineBox').getObject('Sketch016').AttachmentOffset = App.Placement(App.Vector(3.00,0.00,0.00),App.Rotation(App.Vector(0.00,0.00,1.00),0.00))
>>>
>>> FreeCAD.getDocument('MedicineBox').getObject('Sketch016').AttachmentOffset = App.Placement(App.Vector(30.00,0.00,0.00),App.Rotation(App.Vector(0.00,0.00,1.00),0.00))
>>>
>>> FreeCAD.getDocument('MedicineBox').getObject('Sketch016').AttachmentOffset = App.Placement(App.Vector(-2.00,0.00,0.00),App.Rotation(App.Vector(0.00,0.00,1.00),0.00))
>>>
>>> FreeCAD.getDocument('MedicineBox').getObject('Sketch016').AttachmentOffset = App.Placement(App.Vector(-25.00,0.00,0.00),App.Rotation(App.Vector(0.00,0.00,1.00),0.00))
>>>
>>> ### Begin command PartDesign_Pocket
>>> App.getDocument('MedicineBox').getObject('Body003').newObject('PartDesign::Pocket','Pocket010')
>>> App.getDocument('MedicineBox').getObject('Pocket010').Profile = App.getDocument('MedicineBox').getObject('Sketch016')
>>> App.getDocument('MedicineBox').getObject('Pocket010').Length = 5
>>> App.ActiveDocument.recompute()
>>> App.getDocument('MedicineBox').getObject('Pocket010').ReferenceAxis = (App.getDocument('MedicineBox').getObject('Sketch016'),['N_Axis'])
>>> App.getDocument('MedicineBox').getObject('Sketch016').Visibility = False
>>> App.ActiveDocument.recompute()
>>> App.getDocument('MedicineBox').getObject('Pocket010').ViewObject.ShapeColor=getattr(App.getDocument('MedicineBox').getObject('Mirrored012').getLinkedObject(True).ViewObject,'ShapeColor',App.getDocument('MedicineBox').getObject('Pocket010').ViewObject.ShapeColor)
>>> App.getDocument('MedicineBox').getObject('Pocket010').ViewObject.LineColor=getattr(App.getDocument('MedicineBox').getObject('Mirrored012').getLinkedObject(True).ViewObject,'LineColor',App.getDocument('MedicineBox').getObject('Pocket010').ViewObject.LineColor)
>>> App.getDocument('MedicineBox').getObject('Pocket010').ViewObject.PointColor=getattr(App.getDocument('MedicineBox').getObject('Mirrored012').getLinkedObject(True).ViewObject,'PointColor',App.getDocument('MedicineBox').getObject('Pocket010').ViewObject.PointColor)
>>> App.getDocument('MedicineBox').getObject('Pocket010').ViewObject.Transparency=getattr(App.getDocument('MedicineBox').getObject('Mirrored012').getLinkedObject(True).ViewObject,'Transparency',App.getDocument('MedicineBox').getObject('Pocket010').ViewObject.Transparency)
>>> App.getDocument('MedicineBox').getObject('Pocket010').ViewObject.DisplayMode=getattr(App.getDocument('MedicineBox').getObject('Mirrored012').getLinkedObject(True).ViewObject,'DisplayMode',App.getDocument('MedicineBox').getObject('Pocket010').ViewObject.DisplayMode)
>>> Gui.getDocument('MedicineBox').setEdit(App.getDocument('MedicineBox').getObject('Part001'), 0, 'Body003.Pocket010.')
>>> Gui.Selection.clearSelection()
>>> ### End command PartDesign_Pocket
>>> # Gui.Selection.clearSelection()
>>> App.getDocument('MedicineBox').getObject('Pocket010').Length = 5.000000
>>> App.getDocument('MedicineBox').getObject('Pocket010').Length2 = 5.000000
>>> App.getDocument('MedicineBox').getObject('Pocket010').TaperAngle = 0.000000
>>> App.getDocument('MedicineBox').getObject('Pocket010').TaperAngle2 = 0.000000
>>> App.getDocument('MedicineBox').getObject('Pocket010').UseCustomVector = 0
>>> App.getDocument('MedicineBox').getObject('Pocket010').Direction = (0, 1, -0)
>>> App.getDocument('MedicineBox').getObject('Pocket010').ReferenceAxis = (App.getDocument('MedicineBox').getObject('Sketch016'), ['N_Axis'])
>>> App.getDocument('MedicineBox').getObject('Pocket010').AlongSketchNormal = 1
>>> App.getDocument('MedicineBox').getObject('Pocket010').Type = 0
>>> App.getDocument('MedicineBox').getObject('Pocket010').UpToFace = None
>>> App.getDocument('MedicineBox').getObject('Pocket010').Reversed = 0
>>> App.getDocument('MedicineBox').getObject('Pocket010').Midplane = 0
>>> App.getDocument('MedicineBox').getObject('Pocket010').Offset = 0
>>> App.getDocument('MedicineBox').recompute()
>>> App.getDocument('MedicineBox').getObject('Mirrored012').Visibility = False
>>> Gui.getDocument('MedicineBox').resetEdit()
>>> App.getDocument('MedicineBox').getObject('Sketch016').Visibility = False
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Pocket010.')
>>> ### Begin command PartDesign_LinearPattern
>>> App.getDocument('MedicineBox').getObject('Body003').newObject('PartDesign::LinearPattern','LinearPattern')
>>> App.ActiveDocument.recompute()
>>> App.getDocument('MedicineBox').getObject('LinearPattern').Originals = [App.getDocument('MedicineBox').getObject('Pocket010'),]
>>> App.getDocument('MedicineBox').getObject('LinearPattern').Direction = (App.getDocument('MedicineBox').getObject('Sketch016'), ['H_Axis'])
>>> App.getDocument('MedicineBox').getObject('LinearPattern').Length = 100
>>> App.getDocument('MedicineBox').getObject('LinearPattern').Occurrences = 2
>>> App.ActiveDocument.recompute()
>>> App.getDocument('MedicineBox').getObject('LinearPattern').ViewObject.ShapeColor=getattr(App.getDocument('MedicineBox').getObject('Pocket010').getLinkedObject(True).ViewObject,'ShapeColor',App.getDocument('MedicineBox').getObject('LinearPattern').ViewObject.ShapeColor)
>>> App.getDocument('MedicineBox').getObject('LinearPattern').ViewObject.LineColor=getattr(App.getDocument('MedicineBox').getObject('Pocket010').getLinkedObject(True).ViewObject,'LineColor',App.getDocument('MedicineBox').getObject('LinearPattern').ViewObject.LineColor)
>>> App.getDocument('MedicineBox').getObject('LinearPattern').ViewObject.PointColor=getattr(App.getDocument('MedicineBox').getObject('Pocket010').getLinkedObject(True).ViewObject,'PointColor',App.getDocument('MedicineBox').getObject('LinearPattern').ViewObject.PointColor)
>>> App.getDocument('MedicineBox').getObject('LinearPattern').ViewObject.Transparency=getattr(App.getDocument('MedicineBox').getObject('Pocket010').getLinkedObject(True).ViewObject,'Transparency',App.getDocument('MedicineBox').getObject('LinearPattern').ViewObject.Transparency)
>>> App.getDocument('MedicineBox').getObject('LinearPattern').ViewObject.DisplayMode=getattr(App.getDocument('MedicineBox').getObject('Pocket010').getLinkedObject(True).ViewObject,'DisplayMode',App.getDocument('MedicineBox').getObject('LinearPattern').ViewObject.DisplayMode)
>>> Gui.getDocument('MedicineBox').setEdit(App.getDocument('MedicineBox').getObject('Part001'), 0, 'Body003.LinearPattern.')
>>> Gui.Selection.clearSelection()
>>> App.getDocument('MedicineBox').getObject('Body003').Tip = App.getDocument('MedicineBox').getObject('LinearPattern')
>>> App.ActiveDocument.recompute()
>>> ### End command PartDesign_LinearPattern
>>> # Gui.Selection.clearSelection()
>>> App.getDocument('MedicineBox').getObject('LinearPattern').Visibility = True
>>> App.getDocument('MedicineBox').recompute()
>>> Gui.getDocument('MedicineBox').resetEdit()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Pocket010.')
>>> ### Begin command PartDesign_Mirrored
>>> App.getDocument('MedicineBox').getObject('Body003').newObject('PartDesign::Mirrored','Mirrored013')
>>> App.ActiveDocument.recompute()
>>> App.getDocument('MedicineBox').getObject('Mirrored013').Originals = [App.getDocument('MedicineBox').getObject('Pocket010'),]
>>> App.getDocument('MedicineBox').getObject('Mirrored013').MirrorPlane = (App.getDocument('MedicineBox').getObject('Sketch016'), ['V_Axis'])
>>> App.ActiveDocument.recompute()
>>> App.getDocument('MedicineBox').getObject('Mirrored013').ViewObject.ShapeColor=getattr(App.getDocument('MedicineBox').getObject('Pocket010').getLinkedObject(True).ViewObject,'ShapeColor',App.getDocument('MedicineBox').getObject('Mirrored013').ViewObject.ShapeColor)
>>> App.getDocument('MedicineBox').getObject('Mirrored013').ViewObject.LineColor=getattr(App.getDocument('MedicineBox').getObject('Pocket010').getLinkedObject(True).ViewObject,'LineColor',App.getDocument('MedicineBox').getObject('Mirrored013').ViewObject.LineColor)
>>> App.getDocument('MedicineBox').getObject('Mirrored013').ViewObject.PointColor=getattr(App.getDocument('MedicineBox').getObject('Pocket010').getLinkedObject(True).ViewObject,'PointColor',App.getDocument('MedicineBox').getObject('Mirrored013').ViewObject.PointColor)
>>> App.getDocument('MedicineBox').getObject('Mirrored013').ViewObject.Transparency=getattr(App.getDocument('MedicineBox').getObject('Pocket010').getLinkedObject(True).ViewObject,'Transparency',App.getDocument('MedicineBox').getObject('Mirrored013').ViewObject.Transparency)
>>> App.getDocument('MedicineBox').getObject('Mirrored013').ViewObject.DisplayMode=getattr(App.getDocument('MedicineBox').getObject('Pocket010').getLinkedObject(True).ViewObject,'DisplayMode',App.getDocument('MedicineBox').getObject('Mirrored013').ViewObject.DisplayMode)
>>> Gui.getDocument('MedicineBox').setEdit(App.getDocument('MedicineBox').getObject('Part001'), 0, 'Body003.Mirrored013.')
>>> Gui.Selection.clearSelection()
>>> App.getDocument('MedicineBox').getObject('Body003').Tip = App.getDocument('MedicineBox').getObject('Mirrored013')
>>> App.ActiveDocument.recompute()
>>> ### End command PartDesign_Mirrored
>>> # Gui.Selection.clearSelection()
>>> App.getDocument('MedicineBox').getObject('Mirrored013').Visibility = True
>>> App.getDocument('MedicineBox').getObject('Mirrored013').Visibility = True
>>> App.getDocument('MedicineBox').getObject('Mirrored013').MirrorPlane = (App.getDocument('MedicineBox').getObject('YZ_Plane005'), [''])
>>> App.getDocument('MedicineBox').getObject('Mirrored013').Visibility = True
>>> App.getDocument('MedicineBox').recompute()
>>> App.getDocument('MedicineBox').getObject('Pocket010').Visibility = False
>>> Gui.getDocument('MedicineBox').resetEdit()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.DatumPlane008.')
>>> Gui.runCommand('Std_ToggleVisibility',0)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Mirrored013.Face1',0.702789,-33.8614,50)
>>> ### Begin command PartDesign_Fillet
>>> App.getDocument('MedicineBox').getObject('Body003').newObject('PartDesign::Fillet','Fillet009')
>>> App.getDocument('MedicineBox').getObject('Fillet009').Base = (App.getDocument('MedicineBox').getObject('Mirrored013'),['Face1',])
>>> Gui.Selection.clearSelection()
>>> App.getDocument('MedicineBox').getObject('Mirrored013').Visibility = False
>>> App.ActiveDocument.recompute()
>>> App.getDocument('MedicineBox').getObject('Fillet009').ViewObject.ShapeColor=getattr(App.getDocument('MedicineBox').getObject('Mirrored013').getLinkedObject(True).ViewObject,'ShapeColor',App.getDocument('MedicineBox').getObject('Fillet009').ViewObject.ShapeColor)
>>> App.getDocument('MedicineBox').getObject('Fillet009').ViewObject.LineColor=getattr(App.getDocument('MedicineBox').getObject('Mirrored013').getLinkedObject(True).ViewObject,'LineColor',App.getDocument('MedicineBox').getObject('Fillet009').ViewObject.LineColor)
>>> App.getDocument('MedicineBox').getObject('Fillet009').ViewObject.PointColor=getattr(App.getDocument('MedicineBox').getObject('Mirrored013').getLinkedObject(True).ViewObject,'PointColor',App.getDocument('MedicineBox').getObject('Fillet009').ViewObject.PointColor)
>>> App.getDocument('MedicineBox').getObject('Fillet009').ViewObject.Transparency=getattr(App.getDocument('MedicineBox').getObject('Mirrored013').getLinkedObject(True).ViewObject,'Transparency',App.getDocument('MedicineBox').getObject('Fillet009').ViewObject.Transparency)
>>> App.getDocument('MedicineBox').getObject('Fillet009').ViewObject.DisplayMode=getattr(App.getDocument('MedicineBox').getObject('Mirrored013').getLinkedObject(True).ViewObject,'DisplayMode',App.getDocument('MedicineBox').getObject('Fillet009').ViewObject.DisplayMode)
>>> Gui.getDocument('MedicineBox').setEdit(App.getDocument('MedicineBox').getObject('Part001'), 0, 'Body003.Fillet009.')
>>> Gui.Selection.clearSelection()
>>> ### End command PartDesign_Fillet
>>> # Gui.Selection.clearSelection()
>>> App.getDocument('MedicineBox').getObject('Fillet009').Radius = 1.000000
>>> App.getDocument('MedicineBox').getObject('Fillet009').Base = (App.getDocument('MedicineBox').getObject('Mirrored013'),["Face1",])
>>> App.getDocument('MedicineBox').recompute()
>>> App.getDocument('MedicineBox').recompute()
>>> Gui.getDocument('MedicineBox').resetEdit()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Mirrored013.Face5',-11.8649,-60,24.4369)
>>> ### Begin command PartDesign_Fillet
>>> App.getDocument('MedicineBox').getObject('Body003').newObject('PartDesign::Fillet','Fillet009')
>>> App.getDocument('MedicineBox').getObject('Fillet009').Base = (App.getDocument('MedicineBox').getObject('Mirrored013'),['Face5',])
>>> Gui.Selection.clearSelection()
>>> App.getDocument('MedicineBox').getObject('Mirrored013').Visibility = False
>>> App.ActiveDocument.recompute()
>>> App.getDocument('MedicineBox').getObject('Fillet009').ViewObject.ShapeColor=getattr(App.getDocument('MedicineBox').getObject('Mirrored013').getLinkedObject(True).ViewObject,'ShapeColor',App.getDocument('MedicineBox').getObject('Fillet009').ViewObject.ShapeColor)
>>> App.getDocument('MedicineBox').getObject('Fillet009').ViewObject.LineColor=getattr(App.getDocument('MedicineBox').getObject('Mirrored013').getLinkedObject(True).ViewObject,'LineColor',App.getDocument('MedicineBox').getObject('Fillet009').ViewObject.LineColor)
>>> App.getDocument('MedicineBox').getObject('Fillet009').ViewObject.PointColor=getattr(App.getDocument('MedicineBox').getObject('Mirrored013').getLinkedObject(True).ViewObject,'PointColor',App.getDocument('MedicineBox').getObject('Fillet009').ViewObject.PointColor)
>>> App.getDocument('MedicineBox').getObject('Fillet009').ViewObject.Transparency=getattr(App.getDocument('MedicineBox').getObject('Mirrored013').getLinkedObject(True).ViewObject,'Transparency',App.getDocument('MedicineBox').getObject('Fillet009').ViewObject.Transparency)
>>> App.getDocument('MedicineBox').getObject('Fillet009').ViewObject.DisplayMode=getattr(App.getDocument('MedicineBox').getObject('Mirrored013').getLinkedObject(True).ViewObject,'DisplayMode',App.getDocument('MedicineBox').getObject('Fillet009').ViewObject.DisplayMode)
>>> Gui.getDocument('MedicineBox').setEdit(App.getDocument('MedicineBox').getObject('Part001'), 0, 'Body003.Fillet009.')
>>> Gui.Selection.clearSelection()
>>> ### End command PartDesign_Fillet
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Mirrored013.Face6',50,6.4183,26.5585)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Mirrored013.Face3',22.4363,60,38.6062)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Mirrored013.Face4',-50,54.054,20.8379)
>>> App.getDocument('MedicineBox').getObject('Fillet009').Radius = 1.000000
>>> App.getDocument('MedicineBox').getObject('Fillet009').Base = (App.getDocument('MedicineBox').getObject('Mirrored013'),["Face5","Face6","Face3","Face4",])
>>> App.getDocument('MedicineBox').recompute()
>>> App.getDocument('MedicineBox').getObject('Mirrored013').Visibility = False
>>> Gui.getDocument('MedicineBox').resetEdit()
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.')
>>> ### Begin command Std_Export
>>> __objs__=[]
>>> __objs__.append(FreeCAD.getDocument("MedicineBox").getObject("Body003"))
>>> import Mesh
>>> Mesh.export(__objs__,u"/Users/ebaur/Library/Mobile Documents/com~apple~CloudDocs/Crafts/designs/models/MedicineBox/models/Scaffolding-2x2.stl")
>>>
>>> del __objs__
>>> ### End command Std_Export
>>> FreeCAD.getDocument('MedicineBox').getObject('Body003').Label = "Scaffolding00"
>>>
>>> FreeCAD.getDocument('MedicineBox').getObject('Body003').Label = "Scaffolding0"
>>>
>>> FreeCAD.getDocument('MedicineBox').getObject('Body003').Label = "Scaffolding"
>>>
>>> FreeCAD.getDocument('MedicineBox').getObject('Body003').Label = "Scaffolding2"
>>>
>>> FreeCAD.getDocument('MedicineBox').getObject('Body003').Label = "Scaffolding"
>>>
>>> FreeCAD.getDocument('MedicineBox').getObject('Body003').Label = "Scaffolding-"
>>>
>>> FreeCAD.getDocument('MedicineBox').getObject('Body003').Label = "Scaffolding-2"
>>>
>>> FreeCAD.getDocument('MedicineBox').getObject('Body003').Label = "Scaffolding-2x"
>>>
>>> FreeCAD.getDocument('MedicineBox').getObject('Body003').Label = "Scaffolding-2x2"
>>>
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body002.Pocket005.')
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001')
>>> Gui.runCommand('Std_ToggleVisibility',0)
>>> Gui.runCommand('Std_ToggleVisibility',0)
>>> Gui.runCommand('Std_ToggleVisibility',0)
>>> Gui.runCommand('Std_ToggleVisibility',0)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.')
>>> Gui.runCommand('Std_ToggleVisibility',0)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body002.')
>>> Gui.runCommand('Std_ToggleVisibility',0)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001')
>>> Gui.runCommand('Std_ToggleVisibility',0)
>>> # Gui.Selection.clearSelection()
>>> import FreeCAD as App
>>> import Part
>>>
>>> doc = App.newDocument()
>>> # App.setActiveDocument("Unnamed")
>>> # App.ActiveDocument=App.getDocument("Unnamed")
>>> # Gui.ActiveDocument=Gui.getDocument("Unnamed")
>>>
>>> line = Part.LineSegment()
>>> line.StartPoint = (0.0, 0.0, 0.0)
>>> line.EndPoint = (1.0, 1.0, 1.0)
>>> obj = doc.addObject("Part::Feature", "Line")
>>> obj.Shape= line.toShape()
>>>
>>> doc.recompute()
1
>>> # Gui.Selection.addSelection('Unnamed','Line')
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001')
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.')
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Origin005.')
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Pad005.Sketch011.')
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.')
>>> Gui.runCommand('Std_ToggleVisibility',0)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Fillet009.')
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Mirrored013.')
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Pocket010.')
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Pocket010.Sketch016.')
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Origin005.')
>>> Gui.runCommand('Std_ToggleVisibility',0)
>>> Gui.runCommand('Std_ToggleVisibility',0)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Pad005.Sketch011.')
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Pad005.')
>>> Gui.runCommand('Std_ToggleVisibility',0)
>>> Gui.runCommand('Std_ToggleVisibility',0)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Pad005.Sketch011.')
>>> Gui.runCommand('Std_ToggleVisibility',0)
>>> Gui.runCommand('Std_ToggleVisibility',0)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.')
>>> Gui.runCommand('Std_ToggleVisibility',0)
>>> Gui.runCommand('Std_ToggleVisibility',0)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('MedicineBox','Part001','Body003.Fillet009.')
>>> Gui.runCommand('Std_ToggleVisibility',0)
>>> # Gui.Selection.clearSelection()
>>> # Gui.Selection.addSelection('Unnamed','Line')
>>> ### Begin command Std_Delete
>>> App.getDocument('Unnamed').removeObject('Line')
>>> App.getDocument('Unnamed').recompute()
>>> ### End command Std_Delete
>>> # Gui.Selection.clearSelection()
>>> ### Begin command Std_Part
>>> App.activeDocument().Tip = App.activeDocument().addObject('App::Part','Part')
>>> App.activeDocument().Part.Label = 'Part'
>>> Gui.activateView('Gui::View3DInventor', True)
>>> Gui.activeView().setActiveObject('part', App.activeDocument().Part)
>>> App.ActiveDocument.recompute()
>>> ### End command Std_Part
>>> # Gui.Selection.addSelection('Unnamed','Part')
>>> ### Begin command PartDesign_Body
>>> App.activeDocument().addObject('PartDesign::Body','Body')
>>> import PartDesignGui
>>> Gui.activateView('Gui::View3DInventor', True)
>>> Gui.activeView().setActiveObject('pdbody', App.activeDocument().Body)
>>> Gui.Selection.clearSelection()
>>> Gui.Selection.addSelection(App.ActiveDocument.Body)
>>> App.activeDocument().Part.addObject(App.ActiveDocument.Body)
>>> App.ActiveDocument.recompute()
>>> ### End command PartDesign_Body
>>> # Gui.Selection.addSelection('Unnamed','Body')
>>>
