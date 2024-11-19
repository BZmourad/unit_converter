from abc import ABC, abstractmethod

LENGTH_CONVERSION_FACTORS = {
    # Millimeter to others
    ("mm", "cm"): 0.1,
    ("mm", "m"): 0.001,
    ("mm", "km"): 0.000001,
    ("mm", "in"): 0.0393701,
    ("mm", "ft"): 0.00328084,
    ("mm", "yd"): 0.00109361,
    ("mm", "mi"): 0.00000062137,
    # Centimeter to others
    ("cm", "mm"): 10,
    ("cm", "m"): 0.01,
    ("cm", "km"): 0.00001,
    ("cm", "in"): 0.393701,
    ("cm", "ft"): 0.0328084,
    ("cm", "yd"): 0.0109361,
    ("cm", "mi"): 0.0000062137,
    # Meter to others
    ("m", "mm"): 1000,
    ("m", "cm"): 100,
    ("m", "km"): 0.001,
    ("m", "in"): 39.3701,
    ("m", "ft"): 3.28084,
    ("m", "yd"): 1.09361,
    ("m", "mi"): 0.000621371,
    # Kilometer to others
    ("km", "mm"): 0.000001,
    ("km", "cm"): 100000,
    ("km", "m"): 1000,
    ("km", "in"): 39370.1,
    ("km", "ft"): 3280.84,
    ("km", "yd"): 1093.61,
    ("km", "mi"): 0.621371,
    # Inch to others
    ("in", "mm"): 25.4,
    ("in", "cm"): 2.54,
    ("in", "m"): 0.0254,
    ("in", "km"): 0.0000254,
    ("in", "ft"): 0.0833333,
    ("in", "yd"): 0.0277778,
    ("in", "mi"): 0.000015783,
    # Foot to others
    ("ft", "mm"): 304.8,
    ("ft", "cm"): 30.48,
    ("ft", "m"): 0.3048,
    ("ft", "km"): 0.0003048,
    ("ft", "in"): 12,
    ("ft", "yd"): 0.333333,
    ("ft", "mi"): 0.000189394,
    # Yard to others
    ("yd", "mm"): 914.4,
    ("yd", "cm"): 91.44,
    ("yd", "m"): 0.9144,
    ("yd", "km"): 0.0009144,
    ("yd", "in"): 36,
    ("yd", "ft"): 3,
    ("yd", "mi"): 0.000568182,
    # Mile to others
    ("mi", "mm"): 0.000001609,
    ("mi", "cm"): 160934,
    ("mi", "m"): 1609.34,
    ("mi", "km"): 1.60934,
    ("mi", "in"): 63360,
    ("mi", "ft"): 5280,
    ("mi", "yd"): 1760,
}

WEIGHT_CONVERSION_FACTORS = {
    # Milligram to others
    ("mg", "g"): 0.001,
    ("mg", "kg"): 0.000001,
    ("mg", "oz"): 0.000035274,
    ("mg", "lb"): 0.0000022046,
    # Gram to others
    ("g", "mg"): 1000,
    ("g", "kg"): 0.001,
    ("g", "oz"): 0.035274,
    ("g", "lb"): 0.00220462,
    # Kilogram to others
    ("kg", "mg"): 0.000001,
    ("kg", "g"): 1000,
    ("kg", "oz"): 35.274,
    ("kg", "lb"): 2.20462,
    # Ounce to others
    ("oz", "mg"): 28349.5,
    ("oz", "g"): 28.3495,
    ("oz", "kg"): 0.0283495,
    ("oz", "lb"): 0.0625,
    # Pound to others
    ("lb", "mg"): 453592,
    ("lb", "g"): 453.592,
    ("lb", "kg"): 0.453592,
    ("lb", "oz"): 16,
}

TEMPERATURE_CONVERSION_MATRIX = {
    "C": {
        "C": lambda x: x,  # Celsius to Celsius
        "F": lambda x: x * 9 / 5 + 32,  # Celsius to Fahrenheit
        "K": lambda x: x + 273.15,  # Celsius to Kelvin
    },
    "F": {
        "C": lambda x: (x - 32) * 5 / 9,  # Fahrenheit to Celsius
        "F": lambda x: x,  # Fahrenheit to Fahrenheit
        "K": lambda x: (x - 32) * 5 / 9 + 273.15,  # Fahrenheit to Kelvin
    },
    "K": {
        "C": lambda x: x - 273.15,  # Kelvin to Celsius
        "F": lambda x: (x - 273.15) * 9 / 5 + 32,  # Kelvin to Fahrenheit
        "K": lambda x: x,  # Kelvin to Kelvin
    },
}


class ConversionStrategy(ABC):
    @abstractmethod
    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        pass


class LengthConversionStrategy(ConversionStrategy):
    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        # if units are the same, no conversion is required.
        if from_unit == to_unit:
            return value
        # perform conversions
        if (from_unit, to_unit) in LENGTH_CONVERSION_FACTORS:
            return float(value) * LENGTH_CONVERSION_FACTORS[(from_unit, to_unit)]
        else:
            raise ValueError(f"Unsupported conversion from {from_unit} to {to_unit}.")


class WeightConversionStrategy(ConversionStrategy):
    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        # if units are the same, no conversion is required.
        if from_unit == to_unit:
            return value
        # perform conversions
        if (from_unit, to_unit) in WEIGHT_CONVERSION_FACTORS:
            return float(value) * WEIGHT_CONVERSION_FACTORS[(from_unit, to_unit)]
        else:
            raise ValueError(f"Unsupported conversion from {from_unit} to {to_unit}.")


class TemperatureConversionStrategy(ConversionStrategy):
    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        if (
            from_unit not in TEMPERATURE_CONVERSION_MATRIX
            or to_unit not in TEMPERATURE_CONVERSION_MATRIX
        ):
            raise ValueError(f"Unsupported conversion from {from_unit} to {to_unit}.")

        return TEMPERATURE_CONVERSION_MATRIX[from_unit][to_unit](value)


class UnitConverter:
    def __init__(self, strategy: ConversionStrategy):
        self.strategy = strategy

    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        return self.strategy.convert(value, from_unit, to_unit)
