import numpy

# probabilty mass function (pmf)
# where x is a random variable and p is the probabilty
# of an event with a Bernoulli distribution
def pmf(x,p):
    return (p**x)*((1-p)**(1-x))

# mean (expected value E(x)) of a Bernoulli random variable x
def mean(p):
    return p

# variance of random variable x
def var(p):
    return p*(1-p)

# standard deviation as root of variance
def std(p):
    return var(p)**(1/2)

# generate random variates corresponding to a Bernoulli distribution
# size determines number of generated variates
SIZE = 1
def rvs(p,SIZE):
    rvs = numpy.array([])
    for i in range(0,SIZE):
        if numpy.random.rand() <= p:
            a = 1
        else:
            a = 0
        rvs = numpy.append(rvs,a)
    return rvs