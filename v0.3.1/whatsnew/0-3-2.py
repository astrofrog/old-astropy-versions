import numpy as np
from astropy.convolution import convolve, Gaussian2DKernel

# Generate data
np.random.seed(0)
image = np.random.random((128, 128))

# Create kernel
g = Gaussian2DKernel(width=1)

# Convolve data
image_new = convolve(image, g, boundary='extend')

# Plot the results
plt.figure(figsize=(8,3))
plt.subplot(1,2,1)
plt.imshow(image, interpolation='none', origin='lower', vmin=0., vmax=1.)
plt.title('Reference')
plt.subplot(1,2,2)
plt.imshow(image_new, interpolation='none', origin='lower', vmin=0., vmax=1.)
plt.title('Convolved')