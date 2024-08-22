import time
from line_follower.data_collection.line_detection.globals import MOTOR_VELOCITY, CONFIG_KEY, DT, calculate

DATA_FILE_PATH = f"/line_follower/data_collection/line_detection/raw_collected_data/data_{CONFIG_KEY}.bin"


def main():
    from Robi42Lib.robi42 import Robi42
    from machine import Timer

    turn_time = calculate(f"/line_follower/data_collection/robi_configs/robi_{CONFIG_KEY}.json").turn_time

    r = Robi42()
    r.motors.left.set_direction(r.motors.DIR_BACKWARD)
    timer = Timer(-1)

    open(DATA_FILE_PATH, "wb").close()

    time.sleep(3)

    with open(DATA_FILE_PATH, "ab") as f:
        def timer_callback(_: Timer):
            rv = r.ir_sensors.read_raw_values()
            combined = (rv[0] << 20) | (rv[1] << 10) | rv[2]
            byte_data = combined.to_bytes(4, "big")
            f.write(byte_data)

        timer.init(period=int(DT * 1000), callback=timer_callback)

        r.motors.set_velocity(MOTOR_VELOCITY)

        time.sleep(turn_time)

        timer.deinit()

    r.motors.disable()


if __name__ == "__main__":
    main()
