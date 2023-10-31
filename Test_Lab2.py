import Lab2


def test_find_min_max():
    result = []
    input_value = [1, 2, 3, 4, 5]
    test = [1, 5]

    result = Lab2.find_min_max(input_value)
    assert (result == test)


def test_calc_average():
    result = []
    input_value = [1, 2, 3, 4, 5]
    test = 3

    result = Lab2.calc_average(input_value)
    assert (result == test)


def test_calc_median():
    result = []
    input_value = [1, 2, 3, 4, 5]
    test = 3

    result = Lab2.calc_median(input_value)
    assert (result == test)