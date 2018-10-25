import matplotlib.pyplot as plt
import numpy as np
from astropy.modeling import models, fitting
x = np.arange(1, 10, .1)
g1 = models.Gaussian1D(amplitude=[10, 9], mean=[2,3], stddev=[.15,.1])
y = g1(np.array([x, x]).T)
plt.plot(x, y)
plt.title('Evaluating a Gaussian1D model with 2 parameter sets and 2 sets '
          'of input data')
plt.show()