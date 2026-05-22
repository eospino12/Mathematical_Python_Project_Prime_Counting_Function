#prime distribution 

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Testing prime numbers
def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5) + 1):  
       # By a classical result in number theory, if n has a divisor,
        # then it must have one less than or equal to sqrt(n).
        # Therefore, we only test divisibility up to sqrt(n).
        if x % i == 0:
            return False
    return True

x = int(input("Enter a number:"))

if is_prime(x):
    print(x, "is a prime number.")
else:    
    print(x, "is not a prime number.")


#primes until n
# Returns all prime numbers less than or equal to n
def primes_until(x):
    primes = []
    for num in range(2, x + 1):
        if is_prime(num):
            primes.append(num)
    return primes

print("Prime numbers until", x, ":", primes_until(x))

def pi(x):
    return len(primes_until(x))

print("π(", x, ") =", pi(x))


# -----------------------------------------
# Generating data for π(x)
# -----------------------------------------

x_values = []

pi_values = []

for x in range(2, 101):

    x_values.append(x)

    pi_values.append(pi(x))

# -----------------------------------------
# Creating DataFrame
# -----------------------------------------

df = pd.DataFrame({

    "x": x_values,

    "pi(x)": pi_values

})

# -----------------------------------------
# Plotting π(x)
# -----------------------------------------

sns.set_style("darkgrid")

plt.figure(figsize=(12, 7))

sns.lineplot(
    data=df,
    x="x",
    y="pi(x)"
)

plt.title("Prime Counting Function π(x)")

plt.xlabel("x")

plt.ylabel("π(x)")

plt.xticks(range(0, 101, 10))

plt.show()

