#!/usr/bin/env python3

import numpy as np
import matplotlib.plot as plt

np.random.seed(42)
X = np.random.rand(100, 1)
y = 4 + 3 * X + np.ramdom.randn(100, 1)

learning_rate = 0.1
n_iteration = 1000
m = len(X)

theta = np.random.randn(2, 1)
