from dash import html

def create_title():
    return html.Div(className='row', children=[

        html.H2(
            'Acidentes de Trânsito',
            style={'margin': '0', 'fontWeight': '300', 'letterSpacing': '1px'}
        ),

        html.P(
            'Panorama da acidentalidade no munícipio de Passo Fundo/RS',
            style={'margin': '5px 0 0 0', 'fontStyle': 'italic', 'color': '#BDC3C7'}
        )

    ], style={'backgroundColor': '#2C3E50', 
              'color': 'white', 
              'padding': '20px 30px', 
              'textAlign': 'center',
              'borderBottom': '5px solid #16A085'
            })