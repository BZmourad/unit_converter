import pytest

from src.conversion_strategy import (
    LengthConversionStrategy,
    TemperatureConversionStrategy,
    WeightConversionStrategy,
)


# -- LengthConversionStrategy --
@pytest.mark.parametrize(
    argnames="value, from_unit, to_unit, conversion",
    argvalues=[
        (5400, "cm", "in", 2125.99),
        (36, "mi", "yd", 63360),
        (100, "km", "ft", 328084),
        (99999, "mm", "yd", 109.36),
        (654321, "yd", "km", 598.31),
        (1218, "ft", "ft", 1218),
    ],
)
def test_length_convert_success(value, from_unit, to_unit, conversion):
    strategy = LengthConversionStrategy()
    result = strategy.convert(value, from_unit, to_unit)
    assert round(result, 2) == conversion


@pytest.mark.parametrize(
    argnames="value, from_unit, to_unit",
    argvalues=[(42, "cabbage", "ft"), (222, "mm", "burger")],
)
def test_length_convert_raises_error(value, from_unit, to_unit):
    strategy = LengthConversionStrategy()
    with pytest.raises(ValueError):
        strategy.convert(value, from_unit, to_unit)


# -- WeightConversionStrategy --
@pytest.mark.parametrize(
    argnames="value, from_unit, to_unit, conversion",
    argvalues=[
        (33, "kg", "lb", 72.75),
        (3456, "oz", "kg", 97.98),
        (3.2, "g", "mg", 3200),
    ],
)
def test_weight_convert_success(value, from_unit, to_unit, conversion):
    strategy = WeightConversionStrategy()
    result = strategy.convert(value, from_unit, to_unit)
    assert round(result, 2) == conversion


@pytest.mark.parametrize(
    argnames="value, from_unit, to_unit",
    argvalues=[(42, "snow", "lb"), (222, "kg", "sand")],
)
def test_weight_convert_raises_error(value, from_unit, to_unit):
    strategy = WeightConversionStrategy()
    with pytest.raises(ValueError):
        strategy.convert(value, from_unit, to_unit)


# -- TemperatureConversionStrategy --
@pytest.mark.parametrize(
    argnames="value, from_unit, to_unit, conversion",
    argvalues=[
        (84, "F", "F", 84),
        (100, "F", "C", 37.78),
        (333, "K", "F", 139.73),
    ],
)
def test_temperature_convert_success(value, from_unit, to_unit, conversion):
    strategy = TemperatureConversionStrategy()
    result = strategy.convert(value, from_unit, to_unit)
    assert round(result, 2) == conversion


@pytest.mark.parametrize(
    argnames="value, from_unit, to_unit",
    argvalues=[(42, "yin", "F"), (222, "K", "yang")],
)
def test_temperature_convert_raises_error(value, from_unit, to_unit):
    strategy = TemperatureConversionStrategy()
    with pytest.raises(ValueError):
        strategy.convert(value, from_unit, to_unit)
