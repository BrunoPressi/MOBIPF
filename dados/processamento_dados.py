import pandas as pd

df_original = pd.read_csv('./dados/sinistros_ficticios.csv')

# --- Pre-processamento dos Dados ---
def preprocess_data():
    df = df_original.copy()

    # Coluna 'CLASSIFICACAO' para o gráfico de tipos de acidentes
    def classificar_acidente(row):
        if row['ÓBITOS'] > 0:
            return 'Com Vítimas Fatais'
        elif row['FERIDOS'] > 0:
            return 'Com Feridos'
        elif row['HOUVE DANOS AO PATRIMÔNIO PÚBLICO?'] == 'Sim' or row['HOUVE DANOS AO MEIO AMBIENTE?'] == 'Sim':
            return 'Danos Materiais'
        return 'Sem Danos/Vítimas'
    df['CLASSIFICACAO'] = df.apply(classificar_acidente, axis=1)

    # Coluna 'Faixa Horária' para o gráfico de acidentes por turno
    df['HORA'] = pd.to_datetime(df['HORA'], format='%H:%M', errors='coerce').dt.time
    def classificar_turno(row):
        hora = row['HORA']
        if pd.isnull(hora):
            return 'Indefinido'
        if pd.to_datetime('06:00').time() <= hora < pd.to_datetime('12:00').time():
            return 'Manhã'
        elif pd.to_datetime('12:00').time() <= hora < pd.to_datetime('18:00').time():
            return 'Tarde'
        elif pd.to_datetime('18:00').time() <= hora:
            return 'Noite'
        else:
            return 'Madrugada'
    df['FAIXA HORARIA'] = df.apply(classificar_turno, axis=1)

    # Colunas de data para o gráfico de acidentes por mês
    df['DATA'] = pd.to_datetime(df['DATA'], errors='coerce')
    df['MES'] = df['DATA'].dt.month
    df['MES_NOME'] = df['DATA'].dt.strftime('%b')

    return df

df = preprocess_data()

# --- Função para aplicar os filtros no df ---
def filtrar_df(ano='Todos', mes='Todos', dia_semana = 'Todos', faixa_horaria = 'Todos'):

    df_filtrado = df.copy()

    if ano != 'Todos':
        df_filtrado = df_filtrado[df_filtrado['DATA'].dt.year == int(ano)]

    if mes != 'Todos':
        df_filtrado = df_filtrado[df_filtrado['DATA'].dt.month == int(mes)]

    if dia_semana != 'Todos':
        df_filtrado = df_filtrado[df_filtrado['DATA'].dt.day_name() == dia_semana]
        
    if faixa_horaria != 'Todos':
        df_filtrado = df_filtrado[df_filtrado['FAIXA HORARIA'] == faixa_horaria]

    return df_filtrado

# --- Função para exibir os anos no dropdown ---
def get_anos():
    data_minima = df['DATA'].min()
    data_maxima = df['DATA'].max()
    
    anos = list(range(data_minima.year, data_maxima.year + 1))
    anos.append('Todos')
    anos = anos[::-1]
            
    return anos

    