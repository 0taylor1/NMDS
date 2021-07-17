# code for rotating 2D image

import numpy as np
import matplotlib.pyplot as plt
import cvxpy as cp
import numpy.linalg as npl
from PIL import Image
np.set_printoptions(precision=2)

im = Image.open("./data/ucla/ucla.png")
for i in range(35):
    x = im.rotate(i*10, fillcolor='white')
    x.thumbnail((28,28))
    x.save("./data/ucla/ucla-%d"%(i*10), "png")