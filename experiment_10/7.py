import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 100) 
y = np.sin(x)
fig, axs = plt.subplots(3, 2, figsize=(12, 12))
axs[0, 0].plot(x, y, label='Sine Wave', color='blue')
axs[0, 0].set_title('Line Plot')
axs[0, 0].set_xlabel('X-axis')
axs[0, 0].set_ylabel('Y-axis')
axs[0, 0].legend()
axs[0, 0].grid()
categories = ['A', 'B', 'C', 'D']
values = [3, 7, 5, 6]
axs[0, 1].bar(categories, values, color='orange')
axs[0, 1].set_title('Bar Plot')
axs[0, 1].set_xlabel('Categories')
axs[0, 1].set_ylabel('Values')
x_scatter = np.random.rand(50)
y_scatter = np.random.rand(50)
axs[1, 0].scatter(x_scatter, y_scatter, color='green')
axs[1, 0].set_title('Scatter Plot')
axs[1, 0].set_xlabel('X-axis')
axs[1, 0].set_ylabel('Y-axis')

data = np.random.randn(1000) 
axs[1, 1].hist(data, bins=30, color='purple', alpha=0.7)
axs[1, 1].set_title('Histogram')
axs[1, 1].set_xlabel('Value')
axs[1, 1].set_ylabel('Frequency')

sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
axs[2, 0].pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
axs[2, 0].set_title('Pie Chart')
fig.delaxes(axs[2, 1])
plt.tight_layout()
plt.show()