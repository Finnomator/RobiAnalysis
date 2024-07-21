import time

DT = 0.0011
MOTOR_VELOCITY = 0.02
DATA_FILE_PATH = "/line_follower/data_collection/ninety_degree_corner/raw_collected_data/data.txt"
DISTANCE_TO_TAPE = 0.1  # Distance from the contact patch of the wheel to the tape of the 90° corner.

DRIVE_TIME = DISTANCE_TO_TAPE / MOTOR_VELOCITY


def main():
    from Robi42Lib.robi42 import Robi42

    r = Robi42()

    open(DATA_FILE_PATH, "w").close()

    time.sleep(3)

    with open(DATA_FILE_PATH, "a") as f:
        r.motors.enable()
        r.motors.set_velocity(MOTOR_VELOCITY)

        s = time.time_ns()

        t = 0
        while t < DRIVE_TIME:
            f.write(f"{r.ir_sensors.read_raw_values()}\n")
            t += DT

        e = time.time_ns()

        print(f"Actual time: {(e - s) / 1e9}, should time: {DRIVE_TIME}")

    r.motors.disable()


if __name__ == "__main__":
    main()
