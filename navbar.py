# Author:  Cornelius Tanui
# Email: kiplimocornelius at gmail.com
# Description: A basic Dash app to demonstrate components (with Navbar) and deployment.
# Date: 25 Feb 2025
# Version: 1.0
# Usage: python app.py
# Deployment: gunicorn app:server (on Render.com)
# URL: https://dash-app-demo3.onrender.com/

# Import required libraries
import dash_bootstrap_components as dbc
from dash import dcc

# Define the Navbar
navbar = dbc.NavbarSimple(
    brand="Dash App Demo",
    brand_href="/",
    color="#4D4D4F",
    dark=True,
    children=[
        dbc.NavItem(dcc.Link("Home", href="/", className="nav-link")),
        dbc.NavItem(dcc.Link("About", href="/about", className="nav-link text-lowercase fw-light fs-5 text-white")),
        dbc.NavItem(dcc.Link("Content", href="/content", className="nav-link text-titlecase fw-bold fs-5 text-white")),
        dbc.NavItem(dcc.Link("Contact", href="/contact", className="nav-link text-uppercase fw-bold fs-5 text-white")),
        dbc.NavItem(dbc.NavLink("GitHub", href="https://github.com/corneliustanui", external_link=True, className="nav-link")),
        dbc.NavItem(dbc.NavLink("LinkedIn", href="https://ke.linkedin.com/in/cornelius-tanui-527979b9", external_link=True)),

        # The main dropdown link text
        dbc.DropdownMenu(
            label="Contact",
            nav=True,
            in_navbar=True,
            children=[
                dbc.DropdownMenuItem("GitHub", href="https://github.com/corneliustanui", external_link=True),
                dbc.DropdownMenuItem("LinkedIn", href="https://ke.linkedin.com/in/cornelius-tanui-527979b9", external_link=True)
            ]
        ),
    ],
    style={"height": "30%", "width": "100%", 'margin': "0px", 'padding': "0px"}
)