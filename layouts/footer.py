from dash import html

def create_footer():
    return html.Footer(
        html.Div(
            html.P(
                'Fonte: Sistema de Dados Fictícios de Acidentes de Trânsito - Python/Dash/Pandas/Plotly - Abril de 2026',
                style={'margin': '0', 'fontStyle': 'italic', 'fontSize': '14px'}
            ),
            style={
                'padding': '20px',
                'textAlign': 'center',
                'backgroundColor': '#ECF0F1',
                'color': '#7F8C8D',
                'borderTop': '1px solid #dee2e6'
            }
        )
    )