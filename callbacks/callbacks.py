from dash import Input, Output
import pandas as pd
from app import app

from dados.processamento_dados import filtrar_df
from graficos.graficos import *

def register_callbacks():
    
    @app.callback(
        Output('KPI-TOTAL', 'children'),
        Output('ACIDENTES_GRAPH', 'figure'),
        Output('ACIDENTES_REGIAO_GRAPH', 'figure'),
        Output('ACIDENTES_TURNO_GRAPH', 'figure'),
        Output('ACIDENTES_TIPO_GRAPH', 'figure'),
        Output('ACIDENTES_VEICULO_GRAPH', 'figure'),
        Output('ACIDENTES_MES_GRAPH', 'figure'),
        Input('dropdown-ano', 'value'),
        Input('dropdown-ano', 'value'),
        Input('dropdown-mes', 'value'),
        Input('dropdown-dia-semana', 'value'),
        Input('dropdown-faixa-horaria', 'value')
    )
    def update_graficos(ano_kpi, ano, mes, dia_semana, faixa_horaria):
        df_filtrado = filtrar_df(ano, mes, dia_semana, faixa_horaria)
        total = len(filtrar_df(ano_kpi, mes, dia_semana, faixa_horaria))
        return (
            total,
            create_acidentes_graph(df_filtrado), 
            create_acidentes_por_regiao_graph(df_filtrado), 
            create_acidentes_por_turno_graph(df_filtrado), 
            create_acidentes_por_tipo_graph(df_filtrado), 
            create_acidentes_por_veiculo_graph(df_filtrado), 
            create_acidentes_por_mes_graph(df_filtrado)
        )
