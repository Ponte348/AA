import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

data = np.genfromtxt('karger_analysis.txt', delimiter=',', skip_header=1)
nodes = data[:, 0]  # First column
times = data[:, 2]  # Third column

# Define fitting function
def complexity_function(x, a, b, c):
    return a * (x**b) + c

# fit
popt, _ = curve_fit(complexity_function, nodes, times)

# smooth curve for plotting
x_smooth = np.linspace(min(nodes), max(nodes)*2, 1000)
y_smooth = complexity_function(x_smooth, *popt)

plt.figure(figsize=(10, 6))
plt.scatter(nodes, times, color='blue', label='Actual Data')
plt.plot(x_smooth, y_smooth, 'r-', label='Fitted Curve')
plt.xlabel('Number of Nodes')
plt.ylabel('Time (seconds)')
plt.title('Karger Algorithm Execution Time')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('karger_time_fit.png')
plt.close()

print("\nFitted equation:")
print(f"time = {popt[0]:.2e}n^{popt[1]:.2f} + {popt[2]:.2e}")

def predict_time(n):
    return complexity_function(n, *popt)

# predictions
print("\nPredicted times for different sizes:")
test_sizes = [150, 200, 250, 256, 300, 400, 500, 750, 1000]
for n in test_sizes:
    time = predict_time(n)
    if time < 60:
        print(f"{n} nodes: {time:.2f} seconds")
    elif time < 3600:
        print(f"{n} nodes: {time/60:.2f} minutes")
    elif time < 86400:
        print(f"{n} nodes: {time/3600:.2f} hours")
    else:
        print(f"{n} nodes: {time/86400:.2f} days")
