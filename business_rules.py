SHORT_STAY_MIN_NIGHTS = 4
LONG_STAY_MIN_NIGHTS = 14
NO_DISCOUNT = 0.0
SHORT_STAY_DISCOUNT = 0.06
LONG_STAY_DISCOUNT = 0.18


def calculate_room_cost(nightly_rate: float, nights: int) -> float:
    """Return the room cost before discounts."""
    return nightly_rate * nights


def get_stay_discount(nights: int, corporate: bool = False) -> float:
    """Return the discount rate for the stay."""
    if nights >= LONG_STAY_MIN_NIGHTS:
        return LONG_STAY_DISCOUNT
    if nights >= SHORT_STAY_MIN_NIGHTS or corporate:
        return SHORT_STAY_DISCOUNT
    return NO_DISCOUNT
