import pydicom
import matplotlib.pyplot as plt
from skimage import io
from skimage.color import rgb2gray
from skimage import filters
from scipy import ndimage
import numpy as np
import glob


def LoadFileDCM(inpath: str):
    
    myDCMfile = pydicom.dcmread(inpath)
    if 'SamplesPerPixel' not in myDCMfile:
        myDCMfile.SamplesPerPixel = 1
   
    return myDCMfile

def ShowDCM(myfile):

    # if 'SamplesPerPixel' not in myfile:
    #     myfile.SamplesPerPixel = 1
    
    grayscale = io.imread(myfile, as_gray= True) # ładowanie pliku dcm skanu CT
    #grayscale = rgb2gray(raw_image) # konwersja na grayscale 

    grayscale = grayscale.astype('float64') # rzutowanie za uint8 na float64
    grayscale *= (1.0/grayscale.max()) # normalizacja do zakresu 0...1

    val = filters.threshold_otsu(grayscale) 
    mask = grayscale < val # binaryzacja zdjęcia 0,1

    fig, axes = plt.subplots(2, 2, figsize=(12, 12))
    ax = axes.ravel()

    ax[0].imshow(grayscale, cmap=plt.cm.gray)
    ax[0].set_title('Przegrój gazaru - zdjęcie oryginalne')
    ax[0].set_xlabel("Piksel, x")
    ax[0].set_ylabel("Piksel, y")

    ax[1].imshow(mask, cmap=plt.cm.gray)
    ax[1].set_title('Przegrój gazaru - zdjęcie binarne') 
    ax[1].set_xlabel("Piksel, x")
    ax[1].set_ylabel("Piksel, y")

    ax[2].set_title('Przegrój gazaru - zdjęcie binarne') 
    ax[2].set_xlabel("Piksel, x")
    ax[2].set_ylabel("Piksel, y")
    #ax[2].text(0.5, 0.5, "monospace")

    #ax[3].text(0.5, 0.5, "monospace")

  
    print("Hello from a function")


    # Generate the structuring element for the morphological operation that follows
    
    s = ndimage.morphology.generate_binary_structure(2,1)  

    # Label the pores 
    labelled_image, n_labels = ndimage.label(mask, structure=s)

    # Compute the size of each region:
    sizes = ndimage.sum(mask, labelled_image, range(n_labels + 1))[2:]

    # Set the range, excluding pixels of size 1
    rg = (2, sizes.max())

    #Set the number of bins 
    nbins = int(sizes.max()-2)

    # Calculate the histogram
    hh, bin_edges = np.histogram(sizes, range = rg, bins = nbins)
    # set the abscissa in the middle of the bin
    px = 0.1022 # Pixel size, mm

    x = 0.5*(bin_edges[:-1] + bin_edges[1:])*px**2

    # bar width in the histogram bar plot
    width=x[2]-x[1]  

    # Bar plot
    # with plt.style.context(('bmh')):    
    #     plt.bar(x,hh, width, color='r')
    #     plt.xlabel('Powierzhnia porów (mm$^{2}$)')
    #     plt.ylabel('Ilość porów')

    iloscporow = "Całkowita ilość porów = " + str(n_labels)
    ax[3].text(10.5, 80, iloscporow)

    fig.tight_layout()

    plt.show()