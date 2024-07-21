import math
from ast import literal_eval as make_tuple
from collect_data import DT, DISTANCE_TO_TAPE
import matplotlib.pyplot as plt
import numpy as np

TAPE_WIDTH = 0.015  # m

data = []
with open("raw_collected_data/data.txt", "r") as f:
    for line in f.read().strip().splitlines():
        data.append(make_tuple(line))

x_values = np.arange(0, DT * len(data), DT)
x_scaled = x_values / (DT * len(data))

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x_scaled * DISTANCE_TO_TAPE * 100, [d[0] for d in data], linestyle='-', label='Left')
plt.plot(x_scaled * DISTANCE_TO_TAPE * 100, [d[1] for d in data], linestyle='-', label='Middle')
plt.plot(x_scaled * DISTANCE_TO_TAPE * 100, [d[2] for d in data], linestyle='-', label='Right')

tape_start = DISTANCE_TO_TAPE / 2 - TAPE_WIDTH / 2
tape_end = DISTANCE_TO_TAPE / 2 + TAPE_WIDTH / 2

plt.axvline(x=tape_start * 100, color='black', linestyle='-', label='Tape')
plt.axvline(x=tape_end * 100, color='black', linestyle='-')
plt.axvline(x=DISTANCE_TO_TAPE / 2 * 100, color='black', linestyle='--', label='5cm - Middle')

plt.xlabel('Distance driven in cm')
plt.ylabel('IR sensors raw values')
plt.grid(True)
plt.legend()
# plt.show()
plt.savefig('processed_data/data.png', dpi=300)
