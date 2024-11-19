from flask import flash
from flask_wtf import FlaskForm

from src.conversion_strategy import ConversionStrategy, UnitConverter


def calc_conversion_based_on_form_inputs(form: FlaskForm, strategy: ConversionStrategy):
    value = form.value.data
    from_unit = form.from_unit.data
    to_unit = form.to_unit.data

    converter = UnitConverter(strategy=strategy)
    result = None  # Default return value in case of an error

    try:
        result = converter.convert(value, from_unit, to_unit)
    except ValueError as e:
        flash(str(e), "danger")

    return result
