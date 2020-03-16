import pymc3 as pm
import numpy as np
import random
import theano

data1 = np.empty(0)
print(data1)

for i in range(10):
    x = random.random()
    if (x > 0.5):
        data1 = np.append(data1, 1)
    else:
        data1 = np.append(data1, 0)

data = theano.shared(data1)
print(data1)

def calc(given):
    with pm.Model() as model_bkt:
        a = 1
        b = 1
        theta = pm.Beta('Beta', a, b)
        p = pm.Deterministic('p', 1.0 / (1 + pm.math.exp(-1 * (theta * 10 - 5))))
        x = pm.Bernoulli('x', p=p, observed=given)
    m = pm.find_MAP(model=model_bkt)
    return print(m.get('Beta'), m.get('p'))


calc(data)
