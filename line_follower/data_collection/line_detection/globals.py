import json
import collections

CONFIG_KEY = "1"
TAPE_WIDTH = 0.015  # m
MOTOR_ANGULAR_VELOCITY = 30  # °/s
DT_MS = 5  # ms

RobiConfig = collections.namedtuple("Calculations",
                                    "track_width wheel_radius ir_sensor_plate_height ir_wheel_axle_distance")


def load(config_path: str) -> RobiConfig:
    with open(config_path, "r") as config_file:
        config = json.loads(config_file.read())
    return RobiConfig(**config)
