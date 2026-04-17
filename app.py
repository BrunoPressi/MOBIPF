from dash import Dash

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(external_stylesheets=external_stylesheets)
server = app.server
app.title = 'MOBIPF'
