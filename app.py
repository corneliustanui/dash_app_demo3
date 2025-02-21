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
from navbar import navbar

# Add Bootstrap and FontAwesome
external_stylesheets = [
    dbc.themes.BOOTSTRAP,
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css"
]

# Initialize the Dash app
app = dash.Dash(__name__, use_pages=True, 
                external_stylesheets=external_stylesheets, 
                suppress_callback_exceptions=True)

# Layout - This is the only layout needed
app.layout = dbc.Container([
    navbar,  # Navigation bar
    dbc.Row([dbc.Col(dash.page_container, width=12)]),  # Loads the correct page
], fluid=True)

# Expose the server for deployment
server = app.server

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)