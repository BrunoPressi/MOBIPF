from dash import html, dcc

from dados.processamento_dados import get_anos

def create_dropdowns_menu():
    return html.Div(children=[

        # Filtro por Ano
        html.Div([
            html.P('Ano', style={'fontWeight': '500', 'margin': '0 0 8px 0'}),
            dcc.Dropdown(
                options=get_anos(),
                placeholder='Selecione...',
                value='Todos',
                id='dropdown-ano',
                searchable=False,
                clearable=False,
                style = {
                    'font-size': '15px'
                }
            ),
            html.Div(id='dropdown-output-ano', style={'display': 'none'})
        ]),

        # Filtro por Mês
        html.Div([
            html.P('Mês', style={'fontWeight': '500', 'margin': '0 0 8px 0'}),
            dcc.Dropdown(
                options=[
                    {'label': 'Todos', 'value': 'Todos'},
                    {'label': 'Janeiro', 'value': 1},
                    {'label': 'Fevereiro', 'value': 2},
                    {'label': 'Março', 'value': 3},
                    {'label': 'Abril', 'value': 4},
                    {'label': 'Maio', 'value': 5},
                    {'label': 'Junho', 'value': 6},
                    {'label': 'Julho', 'value': 7},
                    {'label': 'Agosto', 'value': 8},
                    {'label': 'Setembro', 'value': 9},
                    {'label': 'Outubro', 'value': 10},
                    {'label': 'Novembro', 'value': 11},
                    {'label': 'Dezembro', 'value': 12}
                ],
                placeholder='Selecione...',
                value='Todos',
                id='dropdown-mes',
                searchable=False,
                clearable=False,
                style = {
                    'font-size': '15px'
                }
            ),
            html.Div(id='dropdown-output-mes', style={'display': 'none'})
        ]),

        # Filtro por Dia da Semana
        html.Div([
            html.P('Dia da Semana', style={'fontWeight': '500', 'margin': '0 0 8px 0'}),
            dcc.Dropdown(
                options=[
                    {'label': 'Todos', 'value': 'Todos'},
                    {'label': 'Segunda-Feira', 'value': 'Monday'},
                    {'label': 'Terça-Feira', 'value': 'Tuesday'},
                    {'label': 'Quarta-Feira', 'value': 'Wednesday'},
                    {'label': 'Quinta-Feira', 'value': 'Thursday'},
                    {'label': 'Sexta-Feira', 'value': 'Friday'},
                    {'label': 'Sábado', 'value': 'Saturday'},
                    {'label': 'Domingo', 'value': 'Sunday'}
                ],
                placeholder='Selecione...',
                value='Todos',
                id='dropdown-dia-semana',
                searchable=False,
                clearable=False,
                style = {
                    'font-size': '15px'
                }
            ),
            html.Div(id='dropdown-output-dia-semana', style={'display': 'none'})
        ]),

        # Filtro por Faixa Horária
        html.Div([
            html.P('Faixa Horária', style={'fontWeight': '500', 'margin': '0 0 8px 0'}),
            dcc.Dropdown(
                options=['Todos', 'Manhã', 'Tarde', 'Noite', 'Madrugada'],
                placeholder='Selecione...',
                value='Todos',
                id='dropdown-faixa-horaria',
                searchable=False,
                clearable=False,
                style = {
                    'font-size': '15px'
                }
            ),
            html.Div(id='dropdown-output-faixa-horaria', style={'display': 'none'})
        ])
    ], style={
        'display': 'grid',
        'grid-template-columns': 'repeat(auto-fit, minmax(200px, 1fr))', # Colunas responsivas
        'gap': '25px', # Espaçamento entre os filtros
        'padding': '20px 30px', # Espaçamento interno
        'backgroundColor': '#F8F9FA', # Cor de fundo suave
        'borderBottom': '1px solid #dee2e6', # Linha separadora
        'width': '50%', # Define a largura do container para 50%
        'margin': '0 auto', # Centraliza o container na página
        'margin-top': '17px'
    })