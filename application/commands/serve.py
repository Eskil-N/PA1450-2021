"""Module for serving an API."""

from flask import Flask, send_file, redirect, render_template
from application.scripts.FormatData import FormatData
from application.scripts.CovGraphs import CompareIRCountryBar, CreateCountryBar, CreateRegionBar, CreateIRCountryBar, CreateIRRegionBar

def serve(options):
    """Serve an API."""

    # Create a Flask application
    app = Flask(__name__)

    @app.route("/")
    def index():
        """Return the index page of the website."""
        return send_file("../www/index.html")

    @app.route("/country/<category>")
    def graphCountry(category):
        """Shows graph of 'category' by country"""
        CreateCountryBar(FormatData(), category)
        return redirect("http://0.0.0.0:8080/")

    @app.route("/search/<search>")
    def graphSearch(search):
        """Shows graph of confirmed cases of searched country"""
        CreateRegionBar(FormatData(), "Confirmed", search)
        return redirect("http://0.0.0.0:8080/")

    @app.route("/infection")
    def graphInfection():
        """Shows graph of Infection rate per capita for each country"""
        CreateIRCountryBar(FormatData()) # Opens Graph in new window
        return redirect("http://0.0.0.0:8080/") # Returns current window to main menu

    @app.route("/compare")
    def rerout1():
        """Reroutes to correct directory"""
        return redirect("http://0.0.0.0:8080/compare/")

    @app.route("/compare/")
    def reroute2():
        """Reroutes to correct directory"""
        return send_file("../www/compare.html")

    @app.route("/compare/<country1>/")
    def compare1(country1):
        """Shows compare.html when adding a country"""
        return send_file("../www/compare.html")

    @app.route("/compare/<country1>/<country2>")
    def compare2(country1, country2):
        """Shows graph of country1 and country2"""
        country1 = checkString(country1)
        country2 = checkString(country2)
        CompareIRCountryBar(FormatData(), country1, country2)
        return redirect("http://0.0.0.0:8080/compare/")

    def checkString(country):
        """Modifies string to fit standards for JHU"""
        country = country[0:-1]
        if country == "United_Kingdom": # Removes underscore
            country = "United Kingdom"
        return country

    app.run(host=options.address, port=options.port, debug=True)

def create_parser(subparsers):
    """Create an argument parser for the "serve" command."""
    parser = subparsers.add_parser("serve")
    parser.set_defaults(command=serve)
    # Add optional parameters to control the server configuration
    parser.add_argument("-p", "--port", default=8080, type=int, help="The port to listen on")
    parser.add_argument("--address", default="0.0.0.0", help="The address to listen on")
