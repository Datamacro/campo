
DATA_INICIO = '2017-01-01'
DATA_FIM = date.today().strftime('%Y-%m-%d')

# Nome do app

st.title ('fieldapp')

# Criando sidebar

st.sidebar.header('ESCOLHA A AÇÃO')

n_dias = st.slider('QUANTIDADE DE DIAS DE PREVISÃO', 30, 365)

def pegar_dados_acoes():
    path = 'C:/Users/jdslh/Documents/Datamacro/acoes.csv'
    return pd.read_csv(path, delimiter=';')
    df = pagar_dados_acoes
    acao = df['snome']
    nome_acao_escolhida = st.sidebar.selectbox('ESCOLHA UMA AÇÃO')
    df_acao = df[df['snome'] == nome_acao_escolhida]
    acao_escolhida = df_acao.iloc[0]['sigla_acao']
    acao_escolhida = acao_escolhida + '.SA'

def pegar_valores_online(sigla_acao):
    df = yf.download(sigla_acao, DATA_INICIO, DATA_FIM)
    df.reset_index(inplace=True)
    return df
    df_valores = pegar_valores_online(acap_escolhida)
    st.subheader('TABELA DE VALORES - ') + nome_acao_escolhida
    st.write(df_valores.tail(10))

    st.subheader('GRÁFICO')
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_valores['Date'],
                             y=df_valores['Close'],
                             name='FECHAMENTO',
                             Line_color='orange'))
    st.plotly_chart(fig)

# Previsão   

    df_treino = df_valores[['Date', 'Close']]

# Renomear Colunas

    df_treino = df_treino.rename(colums={"Date": 'ds', 'Close': 'y'})

# Modelo

    modelo = Prophet()
    modelo_fit(df_treino)

    futuro = modelo.make_future_dataframe(periods=n_dias, freq='B')
    previsao = modelo.predict(futuro)

    st.subheader('PREVISÃO DE PREÇOS (POSSÍVEIS) PARA DATAS FUTURAS')
    st.write(previsao[['ds','yhat', 'yhat_lower', 'yhat_upper', ]].tail.n_dias)

    grafico1 = plot.plotly(modelo, previsao)
    st.plotly_chart(grafico1)

    grafico2 = plot.plot_components_plotly(modelo, previsao)
    st.plotly_chart(grafico2)
