import math
import scipy.stats as stats

# The numerical solution
T = 100
p = math.exp(-0/T) - math.exp(-(T/4)/T)
P = 0

for k in range(0, 101):
    P += math.comb(1000, k) * (p ** k) * ((1 - p) ** (1000 - k))

print(f"The value of P is {P}")

# The normal approximation
x = -9.21
mu = 0
sigma = 1

cdf = stats.norm.cdf(x, mu, sigma)

print(f"The CDF of a normal distribution with argument {x} is {cdf}")
