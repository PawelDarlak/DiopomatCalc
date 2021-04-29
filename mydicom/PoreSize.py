import pydicom
import matplotlib.pyplot as plt
from skimage import filters
from scipy import ndimage
import numpy as np
from matplotlib.offsetbox import AnchoredText
from pydicom.errors import InvalidDicomError

size= 16
params = {'legend.fontsize': 'large',
        'figure.figsize': (20,8),
        'axes.labelsize': size,
        'axes.titlesize': size,
        'xtick.labelsize': size*0.9,
        'ytick.labelsize': size*0.9,
        'axes.titlepad': 25}

def LoadFileDCM(inpath: str) -> None:
    
    myDCMfile = pydicom.dcmread(inpath)
    if 'SamplesPerPixel' not in myDCMfile:
        myDCMfile.SamplesPerPixel = 1
   
    return myDCMfile

def ShowDCM(myfile):

    try:
        myDCMfile = pydicom.read_file(myfile)
    except InvalidDicomError:
        print("File is missing DICOM File Meta Information")
        return False
    except:
        print('no select file')
        return False

    if 'SamplesPerPixel' not in myDCMfile:
        myDCMfile.SamplesPerPixel = 1

    pixelarray = myDCMfile.pixel_array

    # im = ps.filters.prune_branches(pixelarray)
    # my_porosity = ps.metrics.porosity(im = im)


    # plt.show(block= True)

    # grayscale = io.imread(pixelarray, cmap=plt.cm.bone) # ładowanie pliku dcm skanu CT
    
    # grayscale = rgb2gray(pixelarray) # konwersja na grayscale 

    grayscale = pixelarray.astype('float64') # rzutowanie za uint8 na float64
    
    grayscale *= (1.0/pixelarray.max()) # normalizacja do zakresu 0...1

    val = filters.threshold_otsu(grayscale) 
    mask = grayscale < val # binaryzacja zdjęcia 0,1

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

    plt.ion()
    fig, axes = plt.subplots(1, 2, figsize=(14, 7))
   
    fig.canvas.manager.set_window_title('Porosity distribution')
    # plt.get_current_fig_manager().window.setWindowIcon(QIcon('icon.png'))
    
    ax = axes.ravel()
    ax[0].tick_params(labelsize=12)
    ax[0].imshow(mask, cmap=plt.cm.gray)
    ax[0].set_title('Przekrój poprzeczny gazaru - CT', fontsize = 14)
    ax[0].set_xlabel("Oś x, px", fontsize = 16)
    ax[0].set_ylabel("Oś y, px", fontsize = 16)
    # ax[0].set_yticklabels(fontsize=16)

    # ax[1].imshow(mask, cmap=plt.cm.gray)
    # ax[1].set_title('Przegrój gazaru - zdjęcie binarne') 
    # ax[1].set_xlabel("Piksel, x")
    # ax[1].set_ylabel("Piksel, y")

   
    # ax[1].set_xlabel("Powierzchnia, x")
    # ax[1].set_ylabel("Piksel, y")
    # # ax[1].text(0.5, 0.5, "monospace")

    # #ax[3].text(0.5, 0.5, "monospace")

  
    print("Hello from a function")  

    with plt.style.context(('bmh')): 
        ax[1].bar(x, hh, width, color='r')
        ax[1].tick_params(labelsize=12) 
        ax[1].set_xlabel('Powierzchnia porów, mm$^{2}$', fontsize = 16)
        ax[1].set_ylabel('Ilość porów', fontsize = 16)
        ax[1].set_title('Rozkład wielkości porów', fontsize = 14) 

    #Powierzchnia maksymalna poru
    pow_max = round(sizes.max() * px * 0.1, 3)
    pow_min = round(sizes.min() * px * 0.1, 3)

    TotalPors = f"Całkowita ilość porów = {str(n_labels)} \n"
    MinPors = f"Powierzchnia min. 1 pora: {str(pow_min)}mm$^{2}$ \n"
    MaxPors = f"Powierzchnia max. 1 pora: {str(pow_max)}mm$^{2}$"
    Legenda = TotalPors + MinPors + MaxPors

    at = AnchoredText(Legenda,
                  prop=dict(size=12), frameon=True,
                  loc='upper right',
                  )
    at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
    ax[1].add_artist(at)

    # #Bar plot
    # with plt.style.context(('bmh')):   
    #     plt.tick_params(labelsize=12) 
    #     plt.bar(x,hh, width, color='r')
    #     plt.xlabel('Powierzhnia porów (mm$^{2}$)', fontsize = 16)
    #     plt.ylabel('Ilość porów', fontsize = 16)

    # iloscporow = "Całkowita ilość porów = " + str(n_labels)

    
    # at = AnchoredText(iloscporow,
    #               prop=dict(size=12), frameon=True,
    #               loc='upper right',
    #               )
    # at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
    # ax[1].add_artist(at)

    # ax[1].text(2, 2, iloscporow)

  
    print('Zaraz będzie wykres...')

    fig.tight_layout()
    # plt.draw()
    plt.show()