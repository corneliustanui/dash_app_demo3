# Author:  Cornelius Tanui
# Email: kiplimocornelius at gmail.com
# Description: A basic Dash app to demonstrate components (with Navbar) and deployment.
# Date: 25 Feb 2025
# Version: 1.0
# Usage: python app.py
# Deployment: gunicorn app:server (on Render.com)
# URL: https://dash-app-demo3.onrender.com/

# Import required libraries
from dash import html
import dash

# Import the app and navbar (user defined)
from app import app
from navbar import navbar

# Define the main layout
app.layout = html.Div([
    navbar,
    dash.page_container  # Automatically loads the correct page
])

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True) # Set to False for production
