from business_rules import calculate_room_cost, get_stay_discount


def test_room_cost_multiplies_rate_by_nights():
    assert round(calculate_room_cost(110.00, 2), 2) == 220.00


def test_no_discount_at_three_nights():
    assert get_stay_discount(3) == 0.0


def test_six_percent_discount_at_four_nights():
    assert get_stay_discount(4) == 0.06


def test_six_percent_discount_at_thirteen_nights():
    assert get_stay_discount(13) == 0.06


def test_eighteen_percent_discount_at_fourteen_nights():
    assert get_stay_discount(14) == 0.18


def test_corporate_changes_short_stay_discount():
    assert get_stay_discount(2, False) == 0.0
    assert get_stay_discount(2, True) == 0.06


def test_corporate_keeps_larger_long_stay_discount():
    assert get_stay_discount(14, True) == 0.18
