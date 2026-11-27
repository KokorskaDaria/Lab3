from dataclasses import replace

from model import Rental


def add_option(rental: Rental, option: str) -> Rental:
    if not option:
        raise ValueError("Option must not be empty")
    return replace(rental, options=(*rental.options, option))


def extend_rental(rental: Rental, extra_days: int) -> Rental:
    if extra_days <= 0:
        raise ValueError("Extra days must be positive")
    return replace(rental, days=rental.days + extra_days)


def change_status(rental: Rental, status: str) -> Rental:
    if not status:
        raise ValueError("Status must not be empty")
    return replace(rental, status=status)
