from bernoulli import bernoulli

# get probabilty
p = float(input("Probability: "))

print("Bernoulli Mean: %f" % bernoulli.mean(p))
print("Bernoulli Variance: %f" % bernoulli.var(p))
print("Bernoulli Standard Deviation: %f" % bernoulli.std(p))

# get number of random variates to generate
size = int(input("\nNumber of Variates: "))
print("Bernoulli Random Variates: ", bernoulli.rvs(p,size))