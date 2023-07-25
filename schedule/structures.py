from datetime import datetime
from typing import Dict, Any, List
from enum import Enum
import json


class Shift:

    def __init__(self, date, start_time, end_time, duration, raw):
        self._date = date
        self._start_time = start_time
        self._end_time = end_time
        self._duration = duration
        self._raw = raw

    @property
    def date(self) -> datetime:
        return self._date

    @property
    def start_time(self) -> str:
        return self._start_time

    @property
    def end_time(self) -> str:
        return self._end_time

    @property
    def duration(self) -> str:
        return self._duration

    @property
    def raw_data(self) -> Dict[str, Any]:
        return self._raw

    def __repr__(self) -> str:
        return "Shift("+json.dumps({
            "date": self.date.strftime("%d/%m/%Y"),
            "start_time": self.start_time,
            "end_time": self.end_time,
            "duration": self.duration
        }) + ")"


class PunchType(Enum):

    ShiftStart = "ShiftStart"
    BreakStart = "MealStart"
    BreakEnd = "MealEnd"
    ShiftEnd = "ShiftEnd"


class Punch:

    def __init__(self, punch_type: PunchType, time: str) -> None:
        self.punch_type = punch_type
        self.time = time

    def __repr__(self) -> str:
        return f"Punch({self.punch_type}, {self.time})"


class Clock:

    def __init__(self, date: str, punches: List[Punch]) -> None:
        self.date = date
        self.punches = punches

    def __repr__(self) -> str:
        data = "Clock("
        for punch in self.punches:
            data += punch.__repr__() + ", "
        return data[:-2] + ")"
