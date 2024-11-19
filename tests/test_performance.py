import pytest
import time
import tracemalloc

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
    st = time.time()
    tracemalloc.start()
    strategy = LengthConversionStrategy()
    result = strategy.convert(value, from_unit, to_unit)
    print('consommation_mémoire_test_length: ', tracemalloc.get_traced_memory())
    tracemalloc.stop()
    et = time.time()
    elapsed_time = et - st
    print('temps_exécution_test_length: ', elapsed_time, 'seconds')

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
    st = time.time()
    tracemalloc.start()
    strategy = WeightConversionStrategy()
    result = strategy.convert(value, from_unit, to_unit)
    print('consommation_mémoire_test_weight: ', tracemalloc.get_traced_memory())
    tracemalloc.stop()
    et = time.time()
    elapsed_time = et - st
    print('temps_exécution_test_weight: ', elapsed_time, 'seconds')

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
    st = time.time()
    tracemalloc.start()
    strategy = TemperatureConversionStrategy()
    result = strategy.convert(value, from_unit, to_unit)
    print('consommation_mémoire_test_temperature: ', tracemalloc.get_traced_memory())
    tracemalloc.stop()
    et = time.time()
    elapsed_time = et - st
    print('temps_exécution_test_temperature: ', elapsed_time, 'seconds')
