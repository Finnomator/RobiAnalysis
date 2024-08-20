import json
import math
import collections

CONFIG_KEY = "0"
TAPE_WIDTH = 0.015
MOTOR_VELOCITY = 0.02
DT = 0.01

Calculations = collections.namedtuple("Calculations", "track_width ir_distance turn_time")


def calculate(config_path: str) -> Calculations:
    with open(config_path, "r") as config_file:
        config = json.loads(config_file.read())

    robi_track_width = config["track_width"]  # m
    ir_distance = robi_track_width * math.pi / 2  # The total distance that the ir sensor travels while the robi turns
    turn_time = ir_distance / MOTOR_VELOCITY

    return Calculations(robi_track_width, ir_distance, turn_time)
