import streamlit as st
import sqlite3
import pandas as pd
import time
from datetime import datetime
import base64

# CONFIGURAÇÃO DO VIGIA DA COLMEIA


st.set_page_config(
    page_title="Vigia da Colmeia",
    page_icon="🐝",
    layout="wide"
)


# AUTO UPDATE

st.empty()


# CENTRALIZAÇAO DA DIV kkk

st.markdown(
    """
    <div style='text-align:center;'>
        <img src='data:image/jpg;base64,{}' width='220'>
    </div>
    """.format(
        base64.b64encode(
            open("logo.jpg", "rb").read()
        ).decode()
    ),
    unsafe_allow_html=True
)


st.markdown(
    """
    <h1 style='text-align:center;'>
        🐝 Vigia da Colmeia
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <p style='text-align:center; font-size:18px;'>
        Monitoramento inteligente de colmeias em tempo real
    </p>
    """,
    unsafe_allow_html=True
)
# CONECTA NO SQLITE


conn = sqlite3.connect(
    "colmeia.db"
)

query = """

SELECT *
FROM leituras

ORDER BY id DESC

LIMIT 100

"""

df = pd.read_sql_query(
    query,
    conn
)
print(df.columns)

conn.close()

# VERIFICA SE EXISTEM DADOS

if df.empty:

    st.warning(
        "⏳ Aguardando dados..."
    )

else:



    colmeias = sorted(
        df["colmeia"].unique()
    )

    # OFFLINE

offline = []

ativas = []

agora = datetime.now()

for colmeia in colmeias:
    

    dados_colmeia = df[
        df["colmeia"] == colmeia
    ]
    ultima = dados_colmeia.iloc[0]
    alerta = dados_colmeia.iloc[0]["alerta"]

    ultima_data_str = (
        dados_colmeia.iloc[0]["data"]
    )

    ultima_data = datetime.strptime(
        ultima_data_str,
        "%d/%m/%Y %H:%M:%S"
    )

    diferenca = (
        agora - ultima_data
    ).total_seconds()


    # DEFINE STATUS


    if diferenca > 35:

        offline.append(colmeia)

    else:

        ativas.append(colmeia)

    # SISTEMA DE STATUS
   
    if colmeia in offline:

        status = "🚨 OFFLINE"
        
        

    else:

        status = "🟢 ONLINE"


    with st.container():

        st.markdown("---")

        c1, c2, c3, c4 = st.columns(4)
        

        c1.metric(
            f"🐝 Colmeia {colmeia}",
            status
        )
        if (colmeia in offline):
            
            c2.metric(
                "🌡️ Temperatura",
                "N/A"
            )

            c3.metric(
                "🔊 Som",
                "N/A"
            )

            c4.metric(
                "⚠️ Alerta",
                "SEM DADOS"
            )
        else:

            c2.metric(
                "🌡️ Temperatura",
                f"{ultima['temperatura']} °C"
            )

            c3.metric(
                "🔊 Som",
                ultima["som"]
            )

            c4.metric(
                "⚠️ Alerta",
                alerta
            )

        # SISTEMAS EXPANSÍVEIS       

        with st.expander(
            f"📊 Ver detalhes da Colmeia {colmeia}"
        ):

          
            # SISTEMA DE ALERTAS
       
            if alerta == "SUPERAQUECIMENTO":

                st.error(
                    "🔥 Temperatura crítica"
                )

            elif alerta == "ESTRESSE SONORO":

                st.warning(
                    "🔊 Som anormal"
                )

            elif alerta == "NORMAL":

                st.success(
                    "✅ Funcionamento normal"
                )

            # SISTEMA GRÁFICO
           
            g1, g2 = st.columns(2)

            with g1:

                st.markdown(
                    "### 🌡️ Temperatura"
                )

                st.line_chart(
                    dados_colmeia[
                        "temperatura"
                    ]
                )

            with g2:

                st.markdown(
                    "### 🔊 Som"
                )

                st.line_chart(
                    dados_colmeia[
                        "som"
                    ]
                )

           
            # SISTEMA DE HISTÓRICO


            st.markdown(
                "### 📜 Histórico"
            )

            st.dataframe(
                dados_colmeia,
                width="stretch"
            )


# ATUALIZA AUTOMATICAMENTE


time.sleep(2)

st.rerun()