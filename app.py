import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

app = dash.Dash(__name__)

app.layout = html.Div(children=[
       html.H1(children='Hello Dash'),
       html.Div(children='''Dash: A web application framework for Python.'''),
       dbc.Button('Click me')
   ])

if __name__ == '__main__':
       app.run_server(debug=True)