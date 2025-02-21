# Author:  Cornelius Tanui
# Email: kiplimocornelius at gmail.com
# Description: A basic Dash app to demonstrate components (with Navbar) and deployment.
# Date: 25 Feb 2025
# Version: 1.0
# Usage: python app.py
# Deployment: gunicorn app:server (on Render.com)
# URL: https://dash-app-demo3.onrender.com/

# Import required libraries
import dash
from dash import html

# Register the page
dash.register_page(__name__, path="/")

# Define the page layout
layout = html.Div([
    html.H1("Home"),
    html.P("Welcome to the home page of our Dash app!")
])
