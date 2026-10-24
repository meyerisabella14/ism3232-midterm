from business_rules import calculate_room_cost


def test_room_cost_multiplies_rate_by_nights():
    assert round(calculate_room_cost(110.00, 2), 2) == 220.00
