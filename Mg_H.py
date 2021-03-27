# importing the required modules 
import matplotlib.pyplot as plt 
import numpy as np 

a = np.log(7)
b = np.log(130)


x = np.arange(0.7, 1.99, 0.0001)

y =  np.exp(-0.000001 / x)

#iloraz = - y / x

#y =  np.reciprocal(np.exp( -70 / x ))


plt.plot(x, y)

# Add a title
plt.title('Granica rozpuszczalności wodoru w ciekłym magnezie')

# Add X and y Label
plt.xlabel('Temperatura, K')
plt.ylabel('Granica rozpuszczalności wodoru, ml/100g')

# Add a grid
plt.grid(alpha=.4, linestyle='--')

# Add a Legend
#plt.legend()

plt.show()


  
