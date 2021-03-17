import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from progress.bar import Bar 


#Początek programu#################################################################

def recalculateTime(TimeLineLocal):
    TimeSize = TimeLineLocal.size
    TimeLineLocal[0:] = 0
    bar = Bar('Processing', max=TimeSize, suffix='%(percent)d%%')
    for x in range(TimeSize):
        TimeLineLocal[x] = x
        bar.next()
    bar.finish()

xlimit = (460, 21000)
ylimit = (250, 950)

filename = "20200408_100411.txt"

dt = np.dtypedtype={'names': ('Date', 'Time0', 'Time1', 'TempPiec', 'TempMetal', 'TempKrystal', 'HA0', 'HA1', 'PA0', 'PA1'), 
'formats': ('S10', 'S10', 'i4', 'i2', 'i2', 'i2', 'S10', 'S10', 'f4', 'i2')}
#dt = np.dtypedtype={'names': ('osX'), 'formats': ('S10')}

array_from_file = np.loadtxt(filename, delimiter=';', dtype=dt, skiprows=1) 

# Create array
TimeLine = array_from_file['Time1']
TempPiec = array_from_file['TempPiec']
TempMetal = array_from_file['TempMetal']
TempKrystal = array_from_file['TempKrystal']
Pressure0 = array_from_file['PA0']

recalculateTime(TimeLine)

#plt.xlim(110000, 4500000)
#plt.ylim(250, 950)
#print(array_from_file)
# Show the plot
#ax = plt.subplot()

fig, ax = plt.subplots()

# Opis wykresu
ax.set_xlabel('Czas, s', fontsize='14')
ax.set_ylabel('Temperatura, °C', fontsize='14')

ax.tick_params(axis="x", labelsize=14)
ax.tick_params(axis="y", labelsize=14)
ax.tick_params(axis='y', labelcolor='red')

ax.annotate('local max', xy=(13000, 800), xytext=(10000, 650),
            arrowprops=dict(facecolor='black', shrink=3),
            )



lns1 = ax.plot(TimeLine, TempPiec, label='Temperatura pieca', color="red")
lns2 = ax.plot(TimeLine, TempMetal, label='Temperatura metalu', color="orange")
lns3 = ax.plot(TimeLine, TempKrystal, label='Temperatura formy', color="brown")


ax.set_ylim(ylimit)
ax.set_xlim(xlimit)

ax2 = ax.twinx()

colorblue = 'tab:blue'
ax2.tick_params(axis="x", labelsize=14)
ax2.tick_params(axis="y", labelsize=14)
ax2.set_ylabel('Ciśnienie, bar', color=colorblue, fontsize='12')  # we already handled the x-label with ax1
lns4 = ax2.plot(TimeLine, Pressure0, dashes=[10, 2], color=colorblue, label='Ciśnienie w komorze')
ax2.tick_params(axis='y', labelcolor=colorblue)

leg = lns1 + lns2 + lns3 + lns4
labs = [l.get_label() for l in leg]
ax.legend(leg, labs, loc=0)

ax.grid()
#ax2.grid(color = colorblue)
fig.tight_layout()
plt.show()

#np.set_printoptions(threshold=np.inf)
#print(repr(array_from_file))
#print(array_from_file[2:5])

if __name__ == "__main__":
    # execute only if run as a script
    pass

