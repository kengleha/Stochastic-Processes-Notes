#import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# X=sum
def calculate_pmf_cdf():
    pmf = {}
    cdf = {}
    total_outcomes = 6 * 6  # Total number of outcomes for two dice

    cumulative_prob = 0

    for die1 in range(1, 7):
        for die2 in range(1, 7):
            sum_val = die1 + die2
            pmf[sum_val] = pmf.get(sum_val, 0) + 1

    for outcome, count in sorted(pmf.items()):
        probability = count / total_outcomes
        cumulative_prob += probability
        cdf[outcome] = cumulative_prob

    return pmf, cdf

# Calculate the PMF and CDF for X = d1 + d2
pmf_result, cdf_result = calculate_pmf_cdf()

# Plot the PMF as a stem plot
plt.stem(pmf_result.keys(), pmf_result.values(), markerfmt='bo', linefmt='b-', basefmt=' ')

plt.title('Probability Mass Function (PMF) for X = d1 + d2')
plt.xlabel('X')
plt.ylabel('Probability (x36 )')
plt.show()

# Plot the CDF as a staircase function
plt.step(cdf_result.keys(), cdf_result.values(), where='post')

plt.title('Cumulative Distribution Function (CDF) for X = d1 + d2')
plt.xlabel('X')
plt.ylabel('Cumulative Probability (x36)')
plt.show()

# X=Product
def calculate_pmf_cdf():
    pmf = {}
    cdf = {}
    total_outcomes = 6 * 6  # Total number of outcomes for two dice

    cumulative_prob = 0

    for die1 in range(1, 7):
        for die2 in range(1, 7):
            product = die1 * die2
            pmf[product] = pmf.get(product, 0) + 1

    for outcome, count in sorted(pmf.items()):
        probability = count / total_outcomes
        cumulative_prob += probability
        cdf[outcome] = cumulative_prob

    return pmf, cdf

# Calculate the PMF and CDF for X = d1 * d2
pmf_result, cdf_result = calculate_pmf_cdf()

# Plot the PMF as a stem plot
plt.stem(pmf_result.keys(), pmf_result.values(), markerfmt='bo', linefmt='b-', basefmt=' ')

plt.title('Probability Mass Function (PMF) for X = d1 * d2')
plt.xlabel('X')
plt.ylabel('Probability (x 36)')
plt.show()

# Plot the CDF as a staircase function
plt.step(cdf_result.keys(), cdf_result.values(), where='post')

plt.title('Cumulative Distribution Function (CDF) for X = d1 * d2')
plt.xlabel('X')
plt.ylabel('Cumulative Probability (x36)')
plt.show()

from itertools import product

def calculate_pmf():
    outcomes = range(2, 37)
    pmf = {}

    for outcome in outcomes:
        count = 0
        for dice_values in product(range(1, 7), repeat=2):
            if dice_values[0] * dice_values[1] == outcome:
                count += 1

        pmf[outcome] = count / 36

    return pmf

def print_pmf():
    pmf = calculate_pmf()

    print("Outcome   |   PMF")
    print("--------------------")

    for outcome, probability in pmf.items():
        print(f"{outcome}         |   {probability:.4f}")

if __name__ == "__main__":
    print_pmf()

