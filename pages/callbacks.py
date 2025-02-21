# Author:  Cornelius Tanui
# Email: kiplimocornelius at gmail.com
# Description: A basic Dash app to demonstrate components (with Navbar) and deployment.
# Date: 25 Feb 2025
# Version: 1.0
# Usage: python app.py
# Deployment: gunicorn app:server (on Render.com)
# URL: https://dash-app-demo3.onrender.com/

# Callback to update the page content based on the URL
@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))

# Function to display the page content
def display_page(pathname):
    return render_page_content(pathname)
