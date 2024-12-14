import vtk

#source başlangıç
cube = vtk.vtkCubeSource()
cube.SetXLength(5)
cube.SetYLength(5)
cube.SetZLength(5)
#source bitiş

camera = vtk.vtkCamera()
camera.SetPosition(10,10,0)
camera.SetFocalPoint(0,0,0)
camera.Zoom(0.75)
camera.Azimuth(45)

camera.Roll(225)

#mapper başlangıç
mapper = vtk.vtkPolyDataMapper()
#mapper.SetInputData(cube)#dosya olduğu gibi gönderilir
mapper.SetInputConnection(cube.GetOutputPort())
#mapper bitiş

#actor başlangıç
actor = vtk.vtkActor()
actor.SetMapper(mapper)
#actor bitiş

#renderer başlangıç
renderer = vtk.vtkRenderer()
renderer.AddActor(actor)
renderer.SetActiveCamera(camera)
#renderer bitiş

#window başlangıç
window = vtk.vtkRenderWindow()
window.AddRenderer(renderer)
#window bitiş

inter = vtk.vtkRenderWindowInteractor()
inter.SetRenderWindow(window)

window.Render()
inter.Start()
