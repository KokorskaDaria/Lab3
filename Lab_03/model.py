from dataclasses import dataclass, field
from types import MappingProxyType
from typing import Mapping


@dataclass(frozen=True, slots=True)
class Car:
    id: int
    model: str
    plate: str


@dataclass(frozen=True, slots=True)
class Rental:
    id: int
    car: Car
    days: int
    status: str
    options: tuple[str, ...] = ()
    tags: frozenset[str] = frozenset()
    meta: Mapping[str, str] = field(default_factory=lambda: MappingProxyType({}))

    def __post_init__(self) -> None:
        if self.days <= 0:
            raise ValueError("Rental days must be positive")
        object.__setattr__(self, "options", tuple(self.options))
        object.__setattr__(self, "tags", frozenset(self.tags))
        object.__setattr__(self, "meta", MappingProxyType(dict(self.meta)))
