import numpy as np
import matplotlib.pyplot as plt

N = 256
img = np.zeros((N, N, 3))

for i in range(0, N):
    img[i, :, 0] = i * 0.0039
    img[i, :, 1] = 1 - i * 0.0039
    img[i, :, 2] = 0.5

plt.imshow(img)
plt.show()
