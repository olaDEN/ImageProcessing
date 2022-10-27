import numpy as np
import matplotlib.pyplot as plt

# a create a matrix (or image), Density picture:
row = 256
col = 256
img = np.zeros((row, col))
img[100:105, :] = 0.5 # change value from 0 to 0.5 in rows between 100 and 105
img[ : , 100:105]= 1 # change value from 0 to 1 in columns between 100 and 105
plt.figure(figsize=(10,4))
plt.imshow(img)
plt.show()