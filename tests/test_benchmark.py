from copy import deepcopy
from time import perf_counter

from core import extend_rental
from model import Car, Rental


def test_benchmark_updates() -> None:
    rental = Rental(1, Car(1, "Toyota Corolla", "BC1234AA"), 3, "active")
    mutable = {"id": 1, "days": 3, "status": "active"}
    runs = 10000
    start = perf_counter()
    for _ in range(runs):
        extend_rental(rental, 2)
    immutable_duration = perf_counter() - start
    start = perf_counter()
    for _ in range(runs):
        copied = deepcopy(mutable)
        copied["days"] += 2
    mutable_duration = perf_counter() - start
    print(f"\nPure update ({runs}): {immutable_duration:.6f} s")
    print(f"Deepcopy update ({runs}): {mutable_duration:.6f} s")
    assert immutable_duration >= 0
    assert mutable_duration >= 0
