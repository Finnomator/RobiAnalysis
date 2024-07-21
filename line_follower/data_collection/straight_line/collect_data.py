import time

from math import pi

DT = 0.0011
MOTOR_VELOCITY = 0.02
DATA_FILE_PATH = "/line_follower/data_collection/straight_line/raw_collected_data/data.txt"
ROBI_TRACK_WIDTH = 0.147  # m

IR_DISTANCE = ROBI_TRACK_WIDTH * pi / 2  # The total distance that the ir sensor travels while the robi turns
TURN_TIME = IR_DISTANCE / MOTOR_VELOCITY

def main():
    from Robi42Lib.robi42 import Robi42

    r = Robi42()

    open(DATA_FILE_PATH, "w").close()

    time.sleep(3)

    with open(DATA_FILE_PATH, "a") as f:
        r.motors.enable()
        r.motors.left.set_direction(True)
        r.motors.set_velocity(MOTOR_VELOCITY)

        s = time.time_ns()

        t = 0
        while t < TURN_TIME:
            f.write(f"{r.ir_sensors.read_raw_values()}\n")
            t += DT

        e = time.time_ns()

        print(f"Actual time: {(e - s) / 1e9}, should time: {TURN_TIME}")

    r.motors.disable()


if __name__ == "__main__":
    main()
