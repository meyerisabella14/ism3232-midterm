CREDIT_CHECK_LIMIT = 2000.00
WELCOME_NIGHTS_LIMIT = 5
WELCOME_TOTAL_LIMIT = 1000.00

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


def requires_credit_check(total: float) -> bool:
    """Return whether the stay total requires a credit check."""
    return total >= CREDIT_CHECK_LIMIT


def gets_welcome_package(nights: int, total: float) -> bool:
    """Return whether both welcome package conditions are met."""
    return nights > WELCOME_NIGHTS_LIMIT and total >= WELCOME_TOTAL_LIMIT


def total_reserved(stays: list) -> float:
    """Return the combined total of all stays."""
    total = 0.0
    for stay in stays:
        total += calculate_stay_total(
            stay["nightly_rate"], stay["nights"], stay["corporate"]
        )
    return total


def largest_stay(stays: list) -> str:
    """Return the first guest with the largest total, or an empty string."""
    largest_guest = ""
    largest_total = 0.0
    for stay in stays:
        stay_total = calculate_stay_total(
            stay["nightly_rate"], stay["nights"], stay["corporate"]
        )
        if largest_guest == "" or stay_total > largest_total:
            largest_total = stay_total
            largest_guest = stay["guest"]
    return largest_guest


def format_stay_line(
    guest: str, total: float, credit_check: bool, welcome_package: bool
) -> str:
    """Return one formatted stay report line."""
    credit_text = "yes" if credit_check else "no"
    welcome_text = "yes" if welcome_package else "no"
    return (
        f"{guest}: ${total:.2f} | credit check: {credit_text}"
        f" | welcome package: {welcome_text}"
    )
