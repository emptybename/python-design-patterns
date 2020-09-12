"""
https://stackabuse.com/creational-design-patterns-in-python/#factory
Problem Statement: Create Robot of any type
"""
from abc import ABC, abstractmethod


class Robot:
    def __init__(self):
        self.bipedal = False
        self.quadripedal = False
        self.wheeled = False
        self.flying = False
        self.traversal = []
        self.detection_systems = []

    def __str__(self):
        string = ""
        if self.bipedal:
            string += "BIPEDAL "
        if self.quadripedal:
            string += "QUADRIPEDAL "
        if self.flying:
            string += "FLYING ROBOT "
        if self.wheeled:
            string += "ROBOT ON WHEELS\n"
        else:
            string += "ROBOT\n"

        if self.traversal:
            string += "Traversal modules installed:\n"

        for module in self.traversal:
            string += "- " + str(module) + "\n"

        if self.detection_systems:
            string += "Detection systems installed:\n"

        for system in self.detection_systems:
            string += "- " + str(system) + "\n"

        return string


class BipedalLegs:
    def __str__(self):
        return "two legs"


class QuadripedalLegs:
    def __str__(self):
        return "four legs"


class Arms:
    def __str__(self):
        return "Two arms"


class Wings:
    def __str__(self):
        return "wings"


class Blades:
    def __str__(self):
        return "blades"


class FourWheels:
    def __str__(self):
        return "four wheels"


class TwoWheels:
    def __str__(self):
        return "two wheels"


class CameraDetectionSystem:
    def __str__(self):
        return "cameras"


class InfraredDetectionSystem:
    def __str__(self):
        return "infrared"


class RobotBuilder(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def build_traversal(self):
        pass

    @abstractmethod
    def build_detection_system(self):
        pass


class AndroidBuilder(RobotBuilder):
    def __init__(self):
        self.robot = Robot()

    def reset(self):
        self.robot = Robot()

    def get_robot(self):
        return self.robot

    def build_traversal(self):
        self.robot.bipedal = True
        self.robot.traversal.append(BipedalLegs())
        self.robot.traversal.append(Arms())

    def build_detection_system(self):
        self.robot.detection_systems.append(CameraDetectionSystem())


class AutonomousCarBuilder(RobotBuilder):
    def __init__(self):
        self.robot = Robot()

    def reset(self):
        self.robot = Robot()

    def get_robot(self):
        return self.robot

    def build_traversal(self):
        self.robot.wheeled = True
        self.robot.traversal.append(FourWheels())

    def build_detection_system(self):
        self.robot.detection_systems.append(InfraredDetectionSystem())


class Directive:
    @staticmethod
    def build_robot(builder):
        if not builder:
            return None
        builder.build_traversal()
        builder.build_detection_system()
        return builder.get_robot()


if __name__ == "__main__":
    print(Directive.build_robot(AutonomousCarBuilder()))
