from dataclasses import FrozenInstanceError
from types import MappingProxyType
from operator import setitem

import pytest

from core import add_option, change_status, extend_rental
from model import Car, Rental


@pytest.fixture
def rental() -> Rental:
    return Rental(
        id=101,
        car=Car(id=1, model="Toyota Corolla", plate="BC1234AA"),
        days=3,
        status="active",
        options=("Insurance",),
        tags=frozenset({"vip"}),
        meta={"source": "web"},
    )


def test_add_option_pure(rental: Rental) -> None:
    result = add_option(rental, "GPS")
    assert result is not rental
    assert result.options == ("Insurance", "GPS")
    assert rental.options == ("Insurance",)


def test_extend_rental_pure(rental: Rental) -> None:
    result = extend_rental(rental, 2)
    assert result.days == 5
    assert rental.days == 3


def test_change_status_pure(rental: Rental) -> None:
    result = change_status(rental, "completed")
    assert result.status == "completed"
    assert rental.status == "active"


def test_frozen_fields(rental: Rental) -> None:
    with pytest.raises(FrozenInstanceError):
        setattr(rental, "days", 8)


def test_read_only_meta(rental: Rental) -> None:
    assert isinstance(rental.meta, MappingProxyType)
    with pytest.raises(TypeError):
        setitem(rental.meta, "source", "app")


def test_nested_inputs_are_copied() -> None:
    source = {"source": "web"}
    rental = Rental(1, Car(1, "Toyota Corolla", "BC1234AA"), 3, "active", meta=source)
    source["source"] = "changed"
    assert rental.meta["source"] == "web"


def test_tags_are_frozen(rental: Rental) -> None:
    assert isinstance(rental.tags, frozenset)
    with pytest.raises(AttributeError):
        getattr(rental.tags, "add")("extra")


def test_repeatability(rental: Rental) -> None:
    assert add_option(rental, "GPS") == add_option(rental, "GPS")


def test_invalid_input(rental: Rental) -> None:
    with pytest.raises(ValueError):
        extend_rental(rental, 0)
    with pytest.raises(ValueError):
        add_option(rental, "")


def test_no_mutation_after_updates(rental: Rental) -> None:
    before = (rental.days, rental.status, rental.options, dict(rental.meta))
    change_status(extend_rental(add_option(rental, "GPS"), 2), "completed")
    assert (rental.days, rental.status, rental.options, dict(rental.meta)) == before
