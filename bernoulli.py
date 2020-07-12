import numpy

class bernoulli():
    def pmf(x,p):
        """
        probabilty mass function (pmf)

        where x is a random variable and p is the probabilty
        of an event with a Bernoulli distribution
        """
        return (p**x)*((1-p)**(1-x))

    def mean(p):
        """
        mean (expected value E(x)) of a Bernoulli random variable x
        """
        return p

    def var(p):
        """
        variance of bernoulli random variable x
        """
        return p*(1-p)

    def std(p,self):
        """
        standard deviation as the square root of variance
        """
        return self.var(p)**(1/2)

    def rvs(p,size):
        """
        generate random variates corresponding to a Bernoulli distribution

        size determines number of generated variates
        """
        rvs = numpy.array([])
        for i in range(0,size):
            if numpy.random.rand() <= p:
                a = 1
            else:
                a = 0
            rvs = numpy.append(rvs,a)
        return rvs