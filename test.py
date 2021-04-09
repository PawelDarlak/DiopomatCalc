import matplotlib.pyplot as plt
import pydicom
from pydicom.data import get_testdata_files
filename = "C855020546.dcm"
import numpy as np


ds = pydicom.dcmread(filename)

if 'SamplesPerPixel' not in ds:
    ds.SamplesPerPixel = 1

array  = ds.pixel_array

plt.imshow(array, cmap=plt.cm.bone)
plt.show()