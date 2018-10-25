import numpy as np
from astropy.modeling import models, fitting

# Generate fake data
np.random.seed(0)
x = np.linspace(-5., 5., 200)
y = 3 * np.exp(-0.5 * (x - 1.3)**2 / 0.8**2)
y += np.random.normal(0., 0.2, x.shape)

# Fit the data
g_init = models.Gaussian1D(amplitude=1., mean=0, stddev=1.)
f2 = fitting.NonLinearLSQFitter()
g = f2(g_init, x, y)

# Plot the results
plt.figure(figsize=(8,5))
plt.plot(x, y, 'ko')
plt.plot(x, g(x), 'r-', lw=2)
plt.xlabel('Position')
plt.ylabel('Flux')