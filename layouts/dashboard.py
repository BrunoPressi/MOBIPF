from dash import html

from graficos.graficos import *

# --- Estilo Comum para os Contêineres dos Gráficos ---
chart_container_style = {
    'backgroundColor': 'white',
    'borderRadius': '8px',
    'padding': '20px',
    'boxShadow': '0 4px 6px rgba(0, 0, 0, 0.05)'
}

config_graphs = {
   'staticPlot': True
}

def create_dashboard():
    return html.Div([
        # Linha 1: KPI em destaque e os dois gráficos principais
        create_kpi_total_acidentes(),
        html.Div(dcc.Graph(id='ACIDENTES_GRAPH', config=config_graphs), style=chart_container_style),
        html.Div(dcc.Graph(id='ACIDENTES_REGIAO_GRAPH', config=config_graphs), style=chart_container_style),

        # Linha 2: Gráficos de detalhamento
        html.Div(dcc.Graph(id='ACIDENTES_TURNO_GRAPH', config=config_graphs), style=chart_container_style),
        html.Div(dcc.Graph(id='ACIDENTES_TIPO_GRAPH', config=config_graphs), style=chart_container_style),
        html.Div(dcc.Graph(id='ACIDENTES_VEICULO_GRAPH', config=config_graphs), style=chart_container_style),

        # Linha 3: Gráfico de tendência ocupando toda a largura
        html.Div(
            html.Div(dcc.Graph(id='ACIDENTES_MES_GRAPH', config=config_graphs), style=chart_container_style), 
            style={'gridColumn': '1 / span 3'} # Ocupa as 3 colunas da grade
        ),
    ], style={
        'display': 'grid',
        'grid-template-columns': 'repeat(3, 1fr)', # Grade fixa de 3 colunas
        'gap': '25px',
        'padding': '20px 30px', # Espaçamento interno
        'backgroundColor': '#F8F9FA', # Cor de fundo suave
        'margin-top': '20px'
    })