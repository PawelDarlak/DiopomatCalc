from vtk import *

# reader the dicom file
reader = vtkDICOMImageReader()
reader.SetDataByteOrderToLittleEndian()
reader.SetFileName("00efb2fedf64b867a36031a394e5855a.dcm")
reader.Update()

# show the dicom flie
imageViewer = vtkImageViewer2()
imageViewer.SetInputConnection(reader.GetOutputPort())
renderWindowInteractor = vtkRenderWindowInteractor()
imageViewer.SetupInteractor(renderWindowInteractor)
imageViewer.Render()
imageViewer.GetRenderer().ResetCamera()
imageViewer.Render()
renderWindowInteractor.Start()