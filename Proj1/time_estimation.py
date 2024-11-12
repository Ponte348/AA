import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Greedy data (let's use a good sample)
nodes_greedy = np.array([100, 200, 300, 400, 500, 600])
times_greedy = np.array([0.05, 0.37, 1.26, 3.07, 6.21, 12.88])

# Exhaustive data
nodes_exhaustive = np.array([20, 21, 22, 23, 24, 25, 26])
times_exhaustive = np.array([4.84, 10.39, 24.91, 52.08, 107.77, 252.42, 556.37])

# Define fitting functions
def polynomial(x, a, b, c):
    return a * x**3 + b * x**2 + c

def exponential(x, a, b, c):
    return a * np.exp(b * x) + c

# Fit the data
popt_greedy, _ = curve_fit(polynomial, nodes_greedy, times_greedy)
popt_exhaustive, _ = curve_fit(exponential, nodes_exhaustive, times_exhaustive)

# Create smooth curves for plotting
x_greedy = np.linspace(0, 700, 1000)
y_greedy = polynomial(x_greedy, *popt_greedy)

x_exhaustive = np.linspace(18, 28, 1000)
y_exhaustive = exponential(x_exhaustive, *popt_exhaustive)

# Create plots
plt.figure(figsize=(12, 5))

# Greedy plot
plt.subplot(1, 2, 1)
plt.scatter(nodes_greedy, times_greedy, color='blue', label='Actual Data')
plt.plot(x_greedy, y_greedy, 'r-', label='Fitted Curve')
plt.xlabel('Number of Nodes')
plt.ylabel('Time (seconds)')
plt.title('Greedy Algorithm')
plt.legend()
plt.grid(True)

# Exhaustive plot
plt.subplot(1, 2, 2)
plt.scatter(nodes_exhaustive, times_exhaustive, color='blue', label='Actual Data')
plt.plot(x_exhaustive, y_exhaustive, 'r-', label='Fitted Curve')
plt.xlabel('Number of Nodes')
plt.ylabel('Time (seconds)')
plt.title('Exhaustive Algorithm')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig('time_fits.png')
plt.close()

# Print the fitted equations
print("\nFitted equations:")
print(f"Greedy: time = {popt_greedy[0]:.2e}n³ + {popt_greedy[1]:.2e}n² + {popt_greedy[2]:.2e}")
print(f"Exhaustive: time = {popt_exhaustive[0]:.2e}e^({popt_exhaustive[1]:.2e}n) + {popt_exhaustive[2]:.2e}")

# Function to predict time for any number of nodes
def predict_time(n, algorithm='greedy'):
    if algorithm.lower() == 'greedy':
        return polynomial(n, *popt_greedy)
    else:
        return exponential(n, *popt_exhaustive)

# Test predictions
print("\nPredicted times for different sizes:")
test_sizes = [100, 500, 1000, 5000]
print("\nGreedy algorithm:")
for n in test_sizes:
    print(f"{n} nodes: {predict_time(n, 'greedy'):.2f} seconds")

print("\nExhaustive algorithm:")
test_sizes = [27, 30, 35, 40]
for n in test_sizes:
    time = predict_time(n, 'exhaustive')
    if time < 60:
        print(f"{n} nodes: {time:.2f} seconds")
    elif time < 3600:
        print(f"{n} nodes: {time/60:.2f} minutes")
    elif time < 86400:
        print(f"{n} nodes: {time/3600:.2f} hours")
    else:
        print(f"{n} nodes: {time/86400:.2f} days")