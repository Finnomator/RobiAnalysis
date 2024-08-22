import time
from line_follower.data_collection.line_detection.globals import (
    MOTOR_ANGULAR_VELOCITY,
    CONFIG_KEY,
    DT_MS,
    load,
)
from Robi42Lib.robi42 import Robi42
from machine import Timer
from math import pi

DATA_FILE_PATH = f"/line_follower/data_collection/line_detection/raw_collected_data/data_{CONFIG_KEY}.bin"
res = load(
    f"/line_follower/data_collection/robi_configs/robi_{CONFIG_KEY}.json"
)
TURN_TIME = 180 / MOTOR_ANGULAR_VELOCITY
MOTOR_VELOCITY = pi * MOTOR_ANGULAR_VELOCITY * res.track_width / 360


def main():
    r = Robi42()
    r.motors.left.set_direction(r.motors.DIR_BACKWARD)
    timer = Timer(-1)

    open(DATA_FILE_PATH, "wb").close()
    f = open(DATA_FILE_PATH, "ab")

    time.sleep(5)

    def timer_callback(_: Timer):
        rv = r.ir_sensors.read_raw_values()
        combined = (rv[0] << 20) | (rv[1] << 10) | rv[2]
        byte_data = combined.to_bytes(4, "big")
        f.write(byte_data)

    r.motors.set_velocity(MOTOR_VELOCITY)

    timer.init(period=DT_MS, callback=timer_callback)
    time.sleep(TURN_TIME)
    timer.deinit()

    r.motors.disable()

    f.close()


if __name__ == "__main__":
    main()
