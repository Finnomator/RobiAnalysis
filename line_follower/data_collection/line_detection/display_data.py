import math
from ast import literal_eval as make_tuple
from collect_data import DT, IR_DISTANCE, ROBI_TRACK_WIDTH, CONFIG_KEY
import matplotlib.pyplot as plt
import numpy as np

TAPE_WIDTH = 0.015  # m

data = []
with open(f"raw_collected_data/data_{CONFIG_KEY}.txt", "r") as f:
    for line in f.read().strip().splitlines():
        data.append(make_tuple(line))

x_values = np.arange(0, DT * len(data), DT)
x_scaled = x_values / (DT * len(data))

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x_scaled * 180, [d[0] for d in data], linestyle='-', label='Left')
plt.plot(x_scaled * 180, [d[1] for d in data], linestyle='-', label='Middle')
plt.plot(x_scaled * 180, [d[2] for d in data], linestyle='-', label='Right')

tape_start = (IR_DISTANCE / 2 - TAPE_WIDTH / 2) / (ROBI_TRACK_WIDTH * math.pi / 2)
tape_end = (IR_DISTANCE / 2 + TAPE_WIDTH / 2) / (ROBI_TRACK_WIDTH * math.pi / 2)

plt.axvline(x=tape_start * 180, color='black', linestyle='-', label='Tape')
plt.axvline(x=tape_end * 180, color='black', linestyle='-')
plt.axvline(x=0.5 * 180, color='black', linestyle='--', label='90° - Middle')

plt.xlabel('Degrees turned')
plt.ylabel('IR sensors raw values')
plt.grid(True)
plt.legend()
# plt.show()
plt.savefig(f'processed_data/data_{CONFIG_KEY}.png', dpi=300)
