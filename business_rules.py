CLEANING_FEE = 40.00
CLEANING_FEE_LIMIT = 300.00

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


def calculate_stay_total(
    nightly_rate: float, nights: int, corporate: bool = False
) -> float:
    """Return the discounted stay cost including any cleaning fee."""
    room_cost = calculate_room_cost(nightly_rate, nights)
    discount = get_stay_discount(nights, corporate)
    discounted_cost = room_cost - room_cost * discount
    if discounted_cost <= CLEANING_FEE_LIMIT:
        return discounted_cost + CLEANING_FEE
    return discounted_cost
