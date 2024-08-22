import math
from ast import literal_eval as make_tuple
import matplotlib.pyplot as plt
import numpy as np

from globals import CONFIG_KEY, TAPE_WIDTH, DT, calculate

res = calculate(f"../robi_configs/robi_{CONFIG_KEY}.json")
IR_DISTANCE = res.ir_distance
ROBI_TRACK_WIDTH = res.track_width

data = []
with open(f"raw_collected_data/data_{CONFIG_KEY}.bin", "rb") as f:
    while True:
        byte_data = f.read(4)
        if not byte_data:
            break

        combined = int.from_bytes(byte_data, byteorder='big')

        left = (combined >> 20) & 0x3FF
        middle = (combined >> 10) & 0x3FF
        right = combined & 0x3FF

        data.append([left, middle, right])

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
plt.ylim(0, 1024)
plt.xlim(0, 180)
plt.grid(True)
plt.minorticks_on()
plt.legend()
# plt.show()
plt.savefig(f'processed_data/data_{CONFIG_KEY}.png', dpi=300)
