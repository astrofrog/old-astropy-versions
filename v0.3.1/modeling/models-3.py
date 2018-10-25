import matplotlib.pyplot as plt
import numpy as np
from astropy.modeling import models, fitting
x = np.arange(1, 10, .1)
p1 = models.Polynomial1D(1, param_dim=5)
p1.c1 = [0, 1, 2, 3, 4]
y = p1(x)
plt.plot(x, y)
plt.title("Polynomial1D model with 5 parameter sets")
plt.show()