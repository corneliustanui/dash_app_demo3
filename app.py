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
import dash_bootstrap_components as dbc

# Add Bootstrap and FontAwesome
external_stylesheets = [
    dbc.themes.BOOTSTRAP,
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css"
]

# Initialize the Dash app
app = dash.Dash(__name__, use_pages=True, 
                external_stylesheets=external_stylesheets, 
                suppress_callback_exceptions=True)

 # Required for deployment on Render
server = app.server  
