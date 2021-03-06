import numpy as np
from astropy.modeling import models, fitting

# Generate fake data
np.random.seed(0)
x, y = np.mgrid[:128, :128]
z = 2. * x ** 2 - 0.5 * x ** 2 + 1.5 * x * y - 1.
z += np.random.normal(0., 0.1, z.shape) * 50000.

# Fit the data using astropy.modeling
p_init = models.Polynomial2D(degree=2)
f = fitting.NonLinearLSQFitter()
p = f(p_init, x, y, z)

# Plot the data with the best-fit model
plt.figure(figsize=(8,2.5))
plt.subplot(1,3,1)
plt.imshow(z, interpolation='nearest', vmin=-1e4, vmax=5e4)
plt.title("Data")
plt.subplot(1,3,2)
plt.imshow(p(x, y), interpolation='nearest', vmin=-1e4, vmax=5e4)
plt.title("Model")
plt.subplot(1,3,3)
plt.imshow(z - p(x, y), interpolation='nearest', vmin=-1e4, vmax=5e4)
plt.title("Residual")