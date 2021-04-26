import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms

fig, ax = plt.subplots()
ax.plot(range(10))
ax.set_yticks((2, 5, 7))
labels = ax.set_yticklabels(('really, really, really', 'long', 'labels'))

def on_draw(event):
    bboxes = []
    for label in labels:
        bbox = label.get_window_extent()
        # the figure transform goes from relative coords->pixels and we
        # want the inverse of that
        bboxi = bbox.transformed(fig.transFigure.inverted())
        bboxes.append(bboxi)
    # the bbox that bounds all the bboxes, again in relative figure coords
    bbox = mtransforms.Bbox.union(bboxes)
    if fig.subplotpars.left < bbox.width:
        # we need to move it over
        fig.subplots_adjust(left=1.1*bbox.width)  # pad a little
        fig.canvas.draw()

fig.canvas.mpl_connect('draw_event', on_draw)

plt.show()

# import matplotlib.pyplot as plt
# import pydicom
# from pydicom.data import get_testdata_files
# filename = "C855020546.dcm"
# import numpy as np


# ds = pydicom.dcmread(filename)

# if 'SamplesPerPixel' not in ds:
#     ds.SamplesPerPixel = 1

# array  = ds.pixel_array

# plt.imshow(array, cmap=plt.cm.bone)
# plt.show()