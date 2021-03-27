import matplotlib.pyplot as plt
import glob
import sys
from pydicom import dcmread

files = []

fpath = 'a1.dcm'

ds = dcmread('a1.dcm')
if 'SamplesPerPixel' not in ds:
    ds.SamplesPerPixel = 1

ds.SamplesPerPixel = int(len(ds.PixelData) / (ds.get('NumberOfFrames', 1) * ds.Rows * ds.Columns * ds.BitsAllocated / 8))




# Normal mode:
print()
print(f"File path........: {fpath}")
print(f"SOP Class........: {ds.SOPClassUID} ({ds.SOPClassUID.name})")
print()

pat_name = ds.PatientName
display_name = pat_name.family_name + ", " + pat_name.given_name
print(f"Patient's Name...: {display_name}")
print(f"Patient ID.......: {ds.PatientID}")
#print(f"Modality.........: {ds.Modality}")
#print(f"Study Date.......: {ds.StudyDate}")
print(f"Image size.......: {ds.Rows} x {ds.Columns}")
print(f"Pixel Spacing....: {ds.PixelSpacing}")


# use .get() if not sure the item exists, and want a default value if missing
print(f"Slice location...: {ds.get('SliceLocation', '(missing)')}")

# plot the image using matplotlib
#ds.bit


plt.imshow(ds.pixel_array, cmap=plt.cm.gray)
plt.show()