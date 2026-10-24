from business_rules import requires_credit_check, gets_welcome_package
from business_rules import calculate_stay_total
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


def test_cleaning_fee_at_exactly_three_hundred():
    assert round(calculate_stay_total(150.00, 2), 2) == 340.00


def test_no_cleaning_fee_one_cent_above_limit():
    assert round(calculate_stay_total(300.01, 1), 2) == 300.01


def test_cleaning_fee_below_limit():
    assert round(calculate_stay_total(110.00, 2), 2) == 260.00


def test_corporate_discount_before_cleaning_fee():
    assert round(calculate_stay_total(150.00, 2, True), 2) == 322.00


def test_stay_total_with_six_percent_discount():
    assert round(calculate_stay_total(125.00, 6), 2) == 705.00


def test_stay_total_with_eighteen_percent_discount():
    assert round(calculate_stay_total(140.00, 20), 2) == 2296.00


def test_no_credit_check_one_cent_below_limit():
    assert requires_credit_check(1999.99) is False


def test_credit_check_at_exact_limit():
    assert requires_credit_check(2000.00) is True


def test_no_welcome_package_at_five_nights():
    assert gets_welcome_package(5, 1200.00) is False


def test_welcome_package_at_six_nights():
    assert gets_welcome_package(6, 1200.00) is True


def test_no_welcome_package_one_cent_below_total_limit():
    assert gets_welcome_package(6, 999.99) is False


def test_welcome_package_at_exact_total_limit():
    assert gets_welcome_package(6, 1000.00) is True


def test_no_welcome_package_when_both_conditions_fail():
    assert gets_welcome_package(5, 999.99) is False
