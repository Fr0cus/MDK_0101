import numpy as np
a = np.arange(11)
a[(4 < a) & (a < 7)] *= -1
print(a)