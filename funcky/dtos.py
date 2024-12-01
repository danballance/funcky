from dataclasses import dataclass


@dataclass
class Event:
    cmd: int  # Range 0-127
    note: int  # Range 0-127
    velocity: int  # Range 0-127

    def to_wire(self):
        return self.cmd, self.note, self.velocity


@dataclass
class Note:
    note: int  # Range 0-127
    duration: int   # ticks
    velocity: int  # Range 0-127
