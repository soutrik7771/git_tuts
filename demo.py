# Example from Visual Studio Code's official website.

import numpy as np
import matplotlib.pyplot as plt
from utils.rand_func import my_sum, my_sub

print("hello")
x = "Rahul"
print(f"Name is {x}")
x = np.linspace(
    0, 10, 100
)  # Create a list of evenly-spaced numbers over the range
plt.plot(x, np.sin(x))  # Plot the sine of each x point
plt.show()  # Display the plot

print(my_sum(1, 2, 3))
print(my_sub(7, 2, 4))

