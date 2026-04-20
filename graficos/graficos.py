from dash import Dash, html, dcc
import dash_ag_grid as dag
import pandas as pd
import plotly.express as px

from dados.processamento_dados import preprocess_data

df = preprocess_data()

def create_kpi_total_acidentes():
    
    total = len(df)

    return html.Div([
       html.H1(
            id='KPI-TOTAL',
            children=f"{total}",
                style={
                    'margin': '0',
                    'fontSize': '48px',
                    'fontWeight': '600',
                    'color': '#333'
                }
        ),
        
        html.P("Acidentes Registrados", style={
            'margin': '10px 0 0 0',
            'fontSize': '18px',
            'color': '#555'
        })
        
    ], style={
        'backgroundColor': 'white',
        'borderRadius': '8px',
        'padding': '40px 20px',
        'textAlign': 'center',
        'display': 'flex',
        'flexDirection': 'column',
        'justifyContent': 'center',
        'boxShadow': '0 4px 6px rgba(0, 0, 0, 0.05)'
    })
    
def create_acidentes_graph(df_filtrado):
    
    contagem = df_filtrado['CLASSIFICACAO'].value_counts().reset_index()
    contagem.columns = ['CLASSIFICACAO', 'TOTAL']
    
    fig = px.bar(
        contagem,
        x='CLASSIFICACAO',
        y='TOTAL',
        text='TOTAL',
        color='CLASSIFICACAO',
        color_discrete_map={
            'Com Feridos': '#2C5A8C',          
            'Danos Materiais': '#537BAA',  
            'Com Vítimas Fatais': '#537BAA',
            'Sem Danos/Vítimas': '#A6BDE5'
        },
        title='Acidentes'
    )

    # Texto acima das barras
    fig.update_traces(
        textposition='outside',
        marker_line_width=0  # remove borda da barra
    )

    # Layout clean
    fig.update_layout(
        autosize=True,
        showlegend=False,  # remove legenda (já dá pra entender pelo eixo X)
        plot_bgcolor='white',
        paper_bgcolor='white',
        
        title={
            'x': 0.5,  # centraliza título
            'xanchor': 'center'
        },
        
        xaxis=dict(
            title='',
            showgrid=False,
            zeroline=False
        ),
        
        yaxis=dict(
            title='',
            showgrid=False,   # remove linhas horizontais
            showticklabels=False  # remove números do eixo Y (fica clean igual imagem)
        )
    )    
    
    return fig
    
def create_acidentes_por_regiao_graph(df_filtrado):
    
    tipos_desejados = [
        'Oeste',
        'Norte',
        'Centro',
        'Leste',
        'Sul'
    ]
    
    df_filtrado = df_filtrado[df_filtrado['REGIÃO'].isin(tipos_desejados)]
    
    contagem = df_filtrado['REGIÃO'].value_counts().reset_index()
    contagem.columns = ['REGIÃO', 'TOTAL']
    
    fig = px.pie(
        contagem,
        names='REGIÃO',
        values='TOTAL',
        hole=0.6,
        title='Acidentes por região',
        color='REGIÃO',
        color_discrete_map={
            'Norte': '#2C5A8C',
            'Sul': '#537BAA',
            'Leste': '#7D9BC8',
            'Oeste': '#A6BDE5',
            'Centro': '#D0E0FF'
        }
    )

    # Texto dentro das fatias
    fig.update_traces(
        textinfo='value',
        textfont_size=14,
        hovertemplate='<b>%{label}</b><br>Acidentes: %{value}<br>%: %{percent}<extra></extra>'
    )

    # TOTAL no centro
    total = contagem['TOTAL'].sum()

    fig.update_layout(
        autosize=True,
        annotations=[
            dict(
                text=f'{total}<br><span style="font-size:12px;">Total</span>',
                x=0.5, y=0.5,
                font_size=20,
                showarrow=False
            )
        ],
        
        showlegend=True,
        legend=dict(
            orientation='h',   # horizontal
            yanchor='top',
            y=-0.1,            # joga pra baixo do gráfico
            xanchor='center',
            x=0.5
        ),
        
        paper_bgcolor='white',
        plot_bgcolor='white',
        
        title={
            'x': 0.5,
            'xanchor': 'center'
        },
        
        margin=dict(t=60, b=20, l=20, r=20)
    )

    return fig

def create_acidentes_por_turno_graph(df_filtrado):
    
    contagem = df_filtrado['FAIXA HORARIA'].value_counts().reset_index()
    contagem.columns = ['FAIXA HORARIA', 'TOTAL']
    
    # Ordenar para uma visualização mais lógica (Madrugada -> Noite)
    ordem_faixas = ['Madrugada', 'Manhã', 'Tarde', 'Noite']
    contagem['FAIXA HORARIA'] = pd.Categorical(contagem['FAIXA HORARIA'], categories=ordem_faixas, ordered=True)
    contagem = contagem.sort_values('FAIXA HORARIA')

    fig = px.bar(
        contagem,
        x='FAIXA HORARIA',
        y='TOTAL',
        text='TOTAL',
        color='FAIXA HORARIA',
        color_discrete_map={
            'Manhã': '#A6BDE5',
            'Tarde': '#7D9BC8',
            'Noite': '#537BAA',
            'Madrugada': '#2C5A8C'        
            },
        title='Acidentes por turno'
    )

    # Texto acima das barras
    fig.update_traces(
        textposition='outside',
        marker_line_width=0  # remove borda da barra
    )

    # Layout clean
    fig.update_layout(
        autosize=True,
        showlegend=False,  # remove legenda (já dá pra entender pelo eixo X)
        plot_bgcolor='white',
        paper_bgcolor='white',
        
        title={
            'x': 0.5,  # centraliza título
            'xanchor': 'center'
        },
        
        xaxis=dict(
            title='',
            showgrid=False,
            zeroline=False
        ),
        
        yaxis=dict(
            title='',
            showgrid=False,   # remove linhas horizontais
            showticklabels=False  # remove números do eixo Y (fica clean igual imagem)
        )
    )    
    
    return fig
    
def create_acidentes_por_mes_graph(df_filtrado):

    contagem = df_filtrado.groupby(['MES', 'MES_NOME']).size().reset_index(name='TOTAL')
    contagem = contagem.sort_values('MES')
    
    fig = px.line(
    contagem,
    x='MES_NOME',
    y='TOTAL',
    markers=True,
    title='Acidentes por mês',
    text='TOTAL'
)

    fig.update_traces(
        line=dict(color='#2C5A8C', width=2),
        marker=dict(size=8, color='#2C5A8C'),
        text=contagem['TOTAL'],
        textposition='top center'
    )

    fig.update_layout(
        autosize=True,
        plot_bgcolor='white',
        paper_bgcolor='white',
        
        xaxis=dict(
            title='',
            showgrid=False,
            zeroline=False
        ),
        
        yaxis=dict(
            title='',
            showgrid=False,
            showticklabels=False
        ),
        
        title=dict(
            x=0,
            xanchor='left'
        )
    )
    
    return fig
    
def create_acidentes_por_tipo_graph(df_filtrado):
    
    contagem = df_filtrado['TIPO DE ACIDENTE'].value_counts().reset_index()
    contagem.columns = ['TIPO DE ACIDENTE', 'TOTAL']
    
    fig = px.bar(
        contagem,
        x = 'TIPO DE ACIDENTE',
        y = 'TOTAL',
        text = 'TOTAL',
        color = 'TIPO DE ACIDENTE',
        color_discrete_map={
            'Colisão': '#2C5A8C',
            'Atropelamento': '#537BAA',
            'Queda de moto': '#7D9BC8',
            'Capotamento': '#A6BDE5'        
            },
        title = 'Acidentes por tipo'
    )
    
    # Texto acima das barras
    fig.update_traces(
        textposition='outside',
        marker_line_width=0  # remove borda da barra
    )

    # Layout clean
    fig.update_layout(
        autosize=True,
        showlegend=False,  # remove legenda (já dá pra entender pelo eixo X)
        plot_bgcolor='white',
        paper_bgcolor='white',
        
        title={
            'x': 0.5,  # centraliza título
            'xanchor': 'center'
        },
        
        xaxis=dict(
            title='',
            showgrid=False,
            zeroline=False
        ),
        
        yaxis=dict(
            title='',
            showgrid=False,   # remove linhas horizontais
            showticklabels=False  # remove números do eixo Y (fica clean igual imagem)
        )
    )    
    
    return fig

def create_acidentes_por_veiculo_graph(df_filtrado):
    
    contagem = df_filtrado['VEÍCULO TIPO'].value_counts().reset_index()
    contagem.columns = ['VEÍCULO TIPO', 'TOTAL']
    
    fig = px.bar(
        contagem,
        x = 'VEÍCULO TIPO',
        y = 'TOTAL',
        title = 'Acidentes envolvendo',
        color = 'VEÍCULO TIPO',
        text = 'TOTAL',
        color_discrete_map={
            'Ônibus': '#2C5A8C',
            'Caminhão': '#537BAA',
            'Carro': '#7D9BC8',
            'Bicicleta': '#A6BDE5',
            'Moto': "#CCD9F0"   
            },
    )
    
    # Texto acima das barras
    fig.update_traces(
        textposition='outside',
        marker_line_width=0  # remove borda da barra
    )

    # Layout clean
    fig.update_layout(
        autosize=True,
        showlegend=False,  # remove legenda (já dá pra entender pelo eixo X)
        plot_bgcolor='white',
        paper_bgcolor='white',
        
        title={
            'x': 0.5,  # centraliza título
            'xanchor': 'center'
        },
        
        xaxis=dict(
            title='',
            showgrid=False,
            zeroline=False
        ),
        
        yaxis=dict(
            title='',
            showgrid=False,   # remove linhas horizontais
            showticklabels=False  # remove números do eixo Y (fica clean igual imagem)
        )
    )    
    
    return fig