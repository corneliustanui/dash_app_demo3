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
    color="black",
    dark=True,
    children=[
        dbc.NavItem(dcc.Link("Home", href="/", className="nav-link")),
        dbc.NavItem(dcc.Link("About", href="/about", className="nav-link")),
        dbc.NavItem(dcc.Link("Content", href="/content", className="nav-link")),
        dbc.NavItem(dcc.Link("Contact", href="/contact", className="nav-link")),
    ]
)
