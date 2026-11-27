from core import add_option, change_status, extend_rental
from model import Car, Rental


def main() -> None:
    car = Car(id=1, model="Toyota Corolla", plate="BC1234AA")
    rental = Rental(id=101, car=car, days=3, status="active", meta={"source": "web"})
    with_option = add_option(rental, "GPS")
    extended = extend_rental(with_option, 2)
    completed = change_status(extended, "completed")
    print("Original:", rental)
    print("With option:", with_option)
    print("Extended:", extended)
    print("Completed:", completed)
    print("Original unchanged:", rental.days == 3 and rental.options == () and rental.status == "active")
