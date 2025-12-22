import dash
from dash import dcc, html, Input, Output, State
import plotly.express as px
import requests
import pandas as pd

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Real-Time Attendance Dashboard", style={'textAlign': 'center'}),
    
    # Login Section
    html.Div(id='login-box', children=[
        dcc.Input(id='u_roll', type='text', placeholder='Roll Number'),
        dcc.Input(id='u_pass', type='password', placeholder='Password'),
        html.Button('Login', id='btn_login'),
        html.Div(id='err_msg', style={'color': 'red'})
    ], style={'textAlign': 'center', 'marginTop': '100px'}),

    # Dashboard Content
    html.Div(id='dash-view', style={'display': 'none'}, children=[
        html.H2(id='welcome-header'),
        html.Button('Logout', id='btn_logout'),
        
        # Real-time Update Timer
        dcc.Interval(id='refresh-timer', interval=2000), 
        
        html.Div([
            dcc.Graph(id='bar-g', style={'width': '33%', 'display': 'inline-block'}),
            dcc.Graph(id='pie-g', style={'width': '33%', 'display': 'inline-block'}),
            dcc.Graph(id='scatter-g', style={'width': '33%', 'display': 'inline-block'})
        ])
    ])
])

@app.callback(
    [Output('login-box', 'style'), Output('dash-view', 'style'), 
     Output('err_msg', 'children'), Output('welcome-header', 'children'),
     Output('bar-g', 'figure'), Output('pie-g', 'figure'), Output('scatter-g', 'figure')],
    [Input('btn_login', 'n_clicks'), Input('btn_logout', 'n_clicks'), Input('refresh-timer', 'n_intervals')],
    [State('u_roll', 'value'), State('u_pass', 'value')]
)
def sync_data(l_clk, lo_clk, n, roll, pwd):
    ctx = dash.callback_context
    if not ctx.triggered: return dash.no_update
    
    trigger = ctx.triggered[0]['prop_id'].split('.')[0]
    if trigger == 'btn_logout': return {'display': 'block'}, {'display': 'none'}, "", "", {}, {}, {}

    if roll and pwd:
        res = requests.post("http://127.0.0.1:8000/login", json={"roll_no": roll, "password": pwd})
        if res.status_code == 200:
            user_info = res.json()
            # Fetch latest data for auto-update
            all_data = requests.get("http://127.0.0.1:8000/get_attendance").json()
            df = pd.DataFrame(all_data)
            df = df[df['roll_no'] == roll]

            f1 = px.bar(df, x='subject', y='attendance_count', title="Attendance")
            f2 = px.pie(df, names='subject', values='attendance_count')
            f3 = px.scatter(df, x='subject', y='attendance_count')

            return {'display': 'none'}, {'display': 'block'}, "", f"Welcome, {user_info['name']}", f1, f2, f3
        return dash.no_update, dash.no_update, "Login Failed", "", {}, {}, {}
    return dash.no_update

if __name__ == '__main__':
    app.run(port=8050)