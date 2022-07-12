import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output

from util.helpers import get_all_players

all_players = get_all_players()

# the actual app starts here
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.CERULEAN],
    meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1'}]
    )
server = app.server
app.title = "Team Cese Stats"

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.Div([
                dcc.Dropdown(all_players, all_players[0], id='player-dropdown')
            ])
        ])
    ]),
    dbc.Row([
        dbc.Col(
            html.Div(
                dbc.Card([
                    dbc.CardHeader([
                        html.H4(id='player-dropdown-select', className='card-title'),
                    ]),
                    dbc.CardBody([
                        html.P([
                            'Anzahl Jahre:    12', html.Br(),
                        ],
                        className='card-text',
                        style={'white-space': 'pre', 'font-family': 'monospace'},
                        ),
                    ])
                ])
            )
        )
    ])
])

@app.callback(
    Output('player-dropdown-select', 'children'),
    Input('player-dropdown', 'value')
)
def return_player(player):
    return player

if __name__ == '__main__':
    app.run_server(debug=True)
