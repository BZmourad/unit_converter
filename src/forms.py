from flask_wtf import FlaskForm
from wtforms import DecimalField, SelectField, SubmitField
from wtforms.validators import DataRequired

LENGTH_UNIT_CHOICES = [
    ("mm", "Millimeter"),
    ("cm", "Centimeter"),
    ("m", "Meter"),
    ("km", "Kilometer"),
    ("in", "Inch"),
    ("ft", "Foot"),
    ("yd", "Yard"),
    ("mi", "Mile"),
]

WEIGHT_UNIT_CHOICES = [
    ("mg", "Milligram"),
    ("g", "Gram"),
    ("kg", "Kilogram"),
    ("oz", "Ounce"),
    ("lb", "Pound"),
]

TEMPERATURE_UNIT_CHOICES = [("C", "Celsius"), ("F", "Fahrenheit"), ("K", "Kelvin")]

class LengthForm(FlaskForm):
    value = DecimalField("Enter length to convert:", validators=[DataRequired()])
    from_unit = SelectField(
        "Unit to convert from:",
        choices=LENGTH_UNIT_CHOICES,
        validators=[DataRequired()],
    )
    to_unit = SelectField(
        "Unit to convert to:", choices=LENGTH_UNIT_CHOICES, validators=[DataRequired()]
    )
    convert = SubmitField(label="Convert")


class WeightForm(FlaskForm):
    value = DecimalField("Enter weight to convert:", validators=[DataRequired()])
    from_unit = SelectField(
        "Unit to convert from:",
        choices=WEIGHT_UNIT_CHOICES,
        validators=[DataRequired()],
    )
    to_unit = SelectField(
        "Unit to convert to:", choices=WEIGHT_UNIT_CHOICES, validators=[DataRequired()]
    )
    convert = SubmitField(label="Convert")


class TemperatureForm(FlaskForm):
    value = DecimalField("Enter temperature to convert:", validators=[DataRequired()])
    from_unit = SelectField(
        "Unit to convert from:",
        choices=TEMPERATURE_UNIT_CHOICES,
        validators=[DataRequired()],
    )
    to_unit = SelectField(
        "Unit to convert to:",
        choices=TEMPERATURE_UNIT_CHOICES,
        validators=[DataRequired()],
    )
    convert = SubmitField(label="Convert")
