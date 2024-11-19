from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

from src.forms import LengthForm, TemperatureForm, WeightForm
from src.conversion_strategy import (
    LengthConversionStrategy,
    TemperatureConversionStrategy,
    WeightConversionStrategy,
)
from src.operations import calc_conversion_based_on_form_inputs

app = Flask(__name__, static_folder="static", template_folder="templates")
# generates a CSRF token that's required for Flask session handling
app.secret_key = "MY_SECRET_KEY"
bootstrap = Bootstrap5(app)


@app.route("/", methods=["GET", "POST"])
def home():

    return render_template("home.html")


@app.route("/length", methods=["GET", "POST"])
def length_conversion():
    form = LengthForm()
    result = None

    if form.validate_on_submit():
        strategy = LengthConversionStrategy()
        result = calc_conversion_based_on_form_inputs(form, strategy)

    return render_template("index.html", form=form, result=result)


@app.route("/weight", methods=["GET", "POST"])
def weight_conversion():
    form = WeightForm()
    result = None

    if form.validate_on_submit():
        strategy = WeightConversionStrategy()
        result = calc_conversion_based_on_form_inputs(form, strategy)

    return render_template("index.html", form=form, result=result)


@app.route("/temperature", methods=["GET", "POST"])
def temperature_conversion():
    form = TemperatureForm()
    result = None

    if form.validate_on_submit():
        strategy = TemperatureConversionStrategy()
        result = calc_conversion_based_on_form_inputs(form, strategy)

    return render_template("index.html", form=form, result=result)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
