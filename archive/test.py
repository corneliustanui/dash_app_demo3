# Author:  Cornelius Tanui
# Email: kiplimocornelius at gmail.com
# Description: A basic Dash app to demonstrate components (with Navbar) and deployment.
# Date: 25 Feb 2025
# Version: 1.0
# Usage: python app.py
# Deployment: gunicorn app:server (on Render.com)
# URL: https://dash-app-demo3.onrender.com/

# Import the required libraries
import dash
import dash_bootstrap_components as dbc  # Import Dash Bootstrap Components
from dash import html, dcc, Input, Output
import datetime

# Add both Bootstrap and FontAwesome
external_stylesheets = [
    dbc.themes.BOOTSTRAP,
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css"
]

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Define the navigation bar
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

# Define the layout
app.layout = dbc.Container([
    dcc.Location(id='url', refresh=False),
    navbar,  # Add the navbar here
    dbc.Row([
        dbc.Col(id='page-content', children=[], width=12)
    ])
], fluid=True,

# adjust layout margins
style={
    'margin': '0px'
})

# Define the content for each page
def render_page_content(pathname):
    if pathname == "/":
        return html.Div([
            html.H1("Home"),
            html.P("This is the Home page.")
        ])
    elif pathname == "/about":
        return html.Div([
            html.H1("About"),
            html.P("This is the About page.")
        ])
    elif pathname == "/content":
        return html.Div([
            dbc.Row([
                dbc.Col([
                    # bigger text
                    html.H1("Dash App Demo!"),

                    # smaller text
                    html.P("This is a basic Dash app to demonstrate components and deployment."),

                    # input 1 - text box
                    html.Div([
                        html.Label([
                            "What is your name? ",
                            html.Span("*", style={'color': 'red'})  # Red asterisk for required field
                        ]),
                        dcc.Input(
                            id='username',
                            type='text',
                            placeholder='Enter your name...',
                            required=True,
                            className='custom-input1'  # Apply the custom CSS class
                        ),
                    ], style={'display': 'flex', 'flexDirection': 'column'}),

                    # input 2 - number box
                    html.Div([
                        html.Label([
                            "What is your age? ",
                            html.Span("*", style={'color': 'red'})  # Red asterisk for required field
                        ]),
                        dcc.Input(
                            id='age',
                            type='number',
                            placeholder='Enter your age...',
                            min=1,  # Minimum allowed age
                            max=120,  # Maximum allowed age
                            required=True,
                            className='custom-input1'  # Apply the custom CSS class
                        )
                    ], style={'display': 'flex', 'flexDirection': 'column'}),

                    # input 3 - dropdown
                    html.Div([
                        html.Label("What is your biological sex?"),
                        dcc.Dropdown(
                            id='gender',
                            options=[
                                {'label': 'Male', 'value': 'male'},
                                {'label': 'Female', 'value': 'female'},
                                {'label': 'Intersex', 'value': 'intersex'}
                            ],
                            placeholder='Select a sex...',
                            style={
                                'marginTop': '8px',  # Adjusts the margin above the box
                                'marginBottom': '12px',  # Adjusts the margin below the box
                                'width': '260px'  # Adjusts the width
                            }
                        )
                    ]),

                    # input 4 - radio buttons
                    html.Div([
                        html.Label("Highest level of education"),
                        dcc.RadioItems(
                            id='education',
                            options=[
                                {'label': 'Primary', 'value': 'primary'},
                                {'label': 'Secondary', 'value': 'secondary'},
                                {'label': 'Tertiary', 'value': 'tertiary'}
                            ],
                            value='primary',  # Default value
                            labelStyle={'display': 'inline-block', 'margin-right': '10px'},  # Adjusts the space between the label and radio button
                            style={
                                'marginTop': '8px',  # Adjusts the margin above the radio buttons
                                'marginBottom': '12px'  # Adjusts the margin above the radio buttons
                            }
                        )
                    ]),

                    # input 5 - checkbox
                    html.Div([
                        html.Label("Select your favorite colors:"),
                        dcc.Checklist(
                            id='colors',
                            options=[
                                {'label': 'Red', 'value': 'red'},
                                {'label': 'Green', 'value': 'green'},
                                {'label': 'Blue', 'value': 'blue'}
                            ],
                            value=['red'],  # Default value
                            labelStyle={'display': 'inline-block', 'margin-right': '10px'},  # Displays the options horizontally
                            style={
                                'marginTop': '8px',  # Adjusts the margin above the radio buttons
                                'marginBottom': '12px'  # Adjusts the margin above the radio buttons
                            }
                        )
                    ]),

                    # input 6 - textarea
                    html.Div([
                        html.Label("Tell me about yourself:"),
                        dcc.Textarea(
                            id='yourself',
                            placeholder='Enter your comments...',
                            className='custom-input2'  # Apply the custom CSS class
                        )
                    ], style={'display': 'flex', 'flexDirection': 'column'}),

                ], width=4),  # Takes third the screen

                dbc.Col([
                    # input 7 - select multiple
                    html.Div([
                        html.Label("Select your favorite fruits:"),
                        dcc.Dropdown(
                            id='fruits',
                            options=[
                                {'label': 'Apple', 'value': 'apple'},
                                {'label': 'Banana', 'value': 'banana'},
                                {'label': 'Orange', 'value': 'orange'},
                                {'label': 'Grapes', 'value': 'grapes'},
                                {'label': 'Strawberry', 'value': 'strawberry'}
                            ],
                            multi=True,  # Allows multiple selections
                            placeholder='Select fruits...',
                            style={
                                'marginTop': '8px',  # Adjusts the margin above the box
                                'marginBottom': '12px',  # Adjusts the margin below the box
                                'width': '260px'  # Adjusts the width
                            }
                        )
                    ]),

                    # input 8 - date picker
                    html.Div([
                        html.Label("Select your birthdate:"),
                        dcc.DatePickerSingle(
                            id='birthdate',
                            placeholder='Select a date...',
                            min_date_allowed=datetime.date(1920, 1, 1),
                            max_date_allowed=datetime.date.today(),
                            initial_visible_month=datetime.date(2000, 1, 1),  # Opens in year 2000
                            display_format='YYYY-MM-DD',  # Ensures year is visible
                            style={
                                'marginTop': '8px',  # Adjusts the margin above the box
                                'marginBottom': '12px',  # Adjusts the margin below the box
                                'fontSize': '16px'  # Adjusts the font size
                            }
                        )
                    ], style={'display': 'flex', 'flexDirection': 'column'}),

                    # input 9 - slider
                    html.Div([
                        html.Label("Select a number between 1 and 10:"),
                        dcc.Slider(
                            id='slider',
                            min=1,
                            max=10,
                            step=1,
                            marks={i: str(i) for i in range(1, 11)},  # Adds labels to the slider
                            value=5,  # Default value,
                        )
                    ], style={'width': '80%', 'margin': '20px'}),

                    # input 10 - range slider
                    html.Div([
                        html.Label("Select a range between 1 and 100:"),
                        dcc.RangeSlider(
                            id='range-slider',
                            min=1,
                            max=10,
                            step=1,
                            marks={i: str(i) for i in range(1, 11)},  # Adds labels to the slider
                            value=[3, 6],  # Default value,
                        )
                    ], style={'width': '80%', 'margin': '20px'}),

                    # input 11 - upload
                    html.Div([
                        html.Label("Upload a file:"),
                        dcc.Upload(
                            id='upload',
                            children=html.Button([
                                html.I(className="fas fa-upload"),  # FontAwesome icon
                                " Upload File"
                            ]),
                            multiple=False,  # Allow multiple files to be uploaded
                            style={
                                'marginTop': '8px',  # Adjusts the margin above the box
                                'marginBottom': '12px',  # Adjusts the margin below the box
                                'width': '150px'  # Adjusts the width
                            }
                        )
                    ]),

                    # input 12 - button
                    html.Div([
                        html.Label("Action button:"),
                        html.Button('Submit',
                                    id='submit',
                                    n_clicks=0,
                                    style={'display': 'flex', 'flexDirection': 'column',
                                           'justifyContent': 'left', 'width': '100px'})
                    ]),

                ], width=4),  # Takes the other third

                dbc.Col([
                    # input 13 - download - link
                    html.Div([
                        html.Label("Download a file(link):"),
                        html.A("Download", href='/download', download='data.csv',
                               style={'marginTop': '8px', 'marginBottom': '12px', 'width': '100px'})
                    ]),

                    # input 13 - download - button
                    html.Div([
                        html.Label("Download a file(button):"),
                        html.Button('Download', id='download', n_clicks=0,
                                    style={'display': 'flex', 'flexDirection': 'column',
                                           'marginTop': '8px', 'marginBottom': '12px', 'width': '100px'})
                    ]),

                    # input 14 - alert
                    html.Div([
                        html.Label("Alert message:"),
                        dbc.Alert("This is a custom alert message.", color='info', id='alert', style={'marginTop': '8px'})
                    ]),

                    # input 15 - toast
                    html.Div([
                        html.Label("Toast message:"),
                        dbc.Toast(
                            "This is a custom toast message.",
                            id='toast',
                            header="Toast Header",
                            icon="danger",
                            style={'marginTop': '8px'}
                        )
                    ]),

                    # input 16 - progress bar
                    html.Div([
                        html.Label("Progress bar:"),
                        dbc.Progress(id='progress', value=50, style={'marginTop': '8px'})
                    ]),

                ], width=4),  # Takes the other third
            ])
        ])
    elif pathname == "/contact":
        return html.Div([
            html.H1("Contact"),
            html.P("This is the Contact page.")
        ])
    else:
        return html.Div([
            html.H1("404: Not found"),
            html.P("The page you are looking for does not exist.")
        ])

# Callback to update the page content based on the URL
@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    return render_page_content(pathname)

# This line is crucial for Gunicorn (deployment on Render)
server = app.server

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)