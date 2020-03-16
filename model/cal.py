import pymc3 as pm
import numpy as np
import random
import theano

# gets one number only
# then it would create the array and do all the neccessary stuff

def abilities(num):
    data1 = np.empty(0)
    numdiv = (10 - num) / 10
    for i in range(500):
        x = random.random()
        if x > numdiv:
            data1 = np.append(data1, 1)
        else:
            data1 = np.append(data1, 0)
    data = theano.shared(data1)
    with pm.Model() as model_bkt:
        a = 1
        b = 1
        theta = pm.Beta('Beta', a, b)
        p = pm.Deterministic('p', 1.0 / (1 + pm.math.exp(-1 * (theta * 10 - 5))))
        x = pm.Bernoulli('x', p=p, observed=data)
    m = pm.find_MAP(model=model_bkt)
    n = m.get('Beta').tolist()
    nf = "{0:.2f}".format(n)
    return print(nf)

#    return print(m.get('Beta'), m.get('p'))


abilities(5)


#@app.route('/_add_numbers')
#def add_numbers():
#a = request.args.get('a', 0, type=int)
#b = request.args.get('b', 0, type=int)
#return jsonify(result=a + b)
