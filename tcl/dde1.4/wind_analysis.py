import numpy as np
import matplotlib.pyplot as plt
from windrose import WindroseAxes

# Sample data
wind_speed = np.random.random(500) * 10  # Wind speed data
wind_direction = np.random.random(500) * 360  # Wind direction data

# Create wind rose plot
ax = WindroseAxes.from_ax()
ax.bar(wind_direction, wind_speed, normed=True, opening=0.8, edgecolor='white')
ax.set_legend()
plt.show()
