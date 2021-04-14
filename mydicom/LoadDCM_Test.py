# from typing import List
import pydicom
import numpy as np
import matplotlib.pyplot as plt
import sys, os
import glob

#path to dcm files
inpath = "E:\\Gasar\\test\\dcm\\Gazar*.dcm"
#outpath = "E:\\Gasar\\test\\dcm\\new\\"
outname = 'out1'
strPatientName = "gasar"

def LoadFileDCM(inpath: str):
    files = []
    for fname in glob.glob(inpath, recursive=False):
        print("loading: {}".format(fname))
        files.append(pydicom.dcmread(fname))
    print("file count: {}".format(len(files)))

    return files


def SaveFileDCM(outpath: str, DataSetDCM: pydicom):
    try:
        os.mkdir(outpath)
    except OSError:
        print ("Creation of the directory %s failed" % outpath)
    else:
        print ("Successfully created the directory %s " % outpath)

    count = 100
    for onefile in DataSetDCM:
        count +=2
        onefile.save_as(outpath + outname + "_" + str(count) + '.dcm')
#       onefile.save_as(outpath + str(count) + '.dcm')
    
def AddSamplePerPixel(files: pydicom):
    #sprawdza czy istnieje w tagach SamplePerPixel. Jeżeli nie to ustawia na 1for onefile in files:
    for onefile in files:
        if 'SamplesPerPixel' not in onefile:
            onefile.SamplesPerPixel = 1

# Dodaje lub zmienia nazwę pacjenta
def AddPatientName(files: pydicom, PatientName: str):
    for onefile in files:
        onefile.PatientName = strPatientName

def AddSliceLocation(files: pydicom):
    
    icount = 0.0
    
    for onefile in files:
    #    onefile.SliceLocation = icount
        onefile.SliceThickness = onefile.PixelSpacing[0] 
        onefile.ImagePositionPatient = [0.0, 0.0, icount]
        icount += onefile.SliceThickness

def RemoveExtraData(files: pydicom):
    for onefile in files:
        del onefile.PatientName
        del onefile.ImagePositionPatient
        del onefile.PixelSpacing
        del onefile.SeriesNumber
        del onefile.ImageOrientationPatient
        del onefile.PhotometricInterpretation

def ShowDCM(files):

    AddSamplePerPixel(files)

# #sprawdza czy istnieje w tagach SamplePerPixel. Jeżeli nie to ustawia na 1
    for onefile in files:
        onefile.SliceLocation = onefile.ImagePositionPatient[2] 

    for onefile in files:
        onefile.SliceThickness = onefile.PixelSpacing[0]



    # skip files with no SliceLocation (eg scout views)
    slices = []
    skipcount = 0
    for f in files:
        if hasattr(f, 'SliceLocation'):
            slices.append(f)
        else:
            skipcount = skipcount + 1

    print("skipped, no SliceLocation: {}".format(skipcount))

    # ensure they are in the correct order
    slices = sorted(slices, key=lambda s: s.SliceLocation)

    # pixel aspects, assuming all slices are the same
    ps = slices[0].PixelSpacing
    ss = slices[0].SliceThickness
    ax_aspect = ps[1]/ps[0]
    sag_aspect = ps[1]/ss
    cor_aspect = ss/ps[0]

    # create 3D array
    img_shape = list(slices[0].pixel_array.shape)
    img_shape.append(len(slices))
    img3d = np.zeros(img_shape)

    # fill 3D array with the images from the files
    for i, s in enumerate(slices):
        img2d = s.pixel_array
        img3d[:, :, i] = img2d

    # plot 3 orthogonal slices
    a1 = plt.subplot(2, 2, 1)
    plt.imshow(img3d[:, :, img_shape[2]//2])
    a1.set_aspect(ax_aspect)

    a2 = plt.subplot(2, 2, 2)
    plt.imshow(img3d[:, img_shape[1]//2, :])
    a2.set_aspect(sag_aspect)

    a3 = plt.subplot(2, 2, 3)
    plt.imshow(img3d[img_shape[0]//2, :, :].T)
    a3.set_aspect(cor_aspect)

    

    plt.show()

   
# Templodadefiles = LoadFileDCM(inpath)
# AddSamplePerPixel(Templodadefiles)
# AddPatientName(Templodadefiles, strPatientName)
# AddSliceLocation(Templodadefiles)
# #RemoveExtraData(Templodadefiles)
# SaveFileDCM(outpath, Templodadefiles)