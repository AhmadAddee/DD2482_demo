from statistics import mean as _mean, pstdev as _pstdev
from typing import Iterable
import time

def add(a: float, b: float) -> float:
    time.sleep(3)
    return a + b

def sub(a: float, b: float) -> float:
    time.sleep(3)
    return a - b

def mul(a: float, b: float) -> float:
    time.sleep(3)
    return a * b

def div(a: float, b: float) -> float:
    time.sleep(3)
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b

def mean(values: Iterable[float]) -> float:
    time.sleep(3)
    vals = list(values)
    if not vals:
        raise ValueError("mean of empty sequence")
    return float(_mean(vals))

def stddev(values: Iterable[float]) -> float:
    time.sleep(3)
    vals = list(values)
    if len(vals) < 2:
        raise ValueError("stddev requires at least two values")
    return float(_pstdev(vals))