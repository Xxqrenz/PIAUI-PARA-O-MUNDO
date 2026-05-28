import streamlit as st
import sqlite3
import pandas as pd
import time
from datetime import datetime

# ======================================
# CONFIGURAÇÃO
# ======================================

st.set_page_config(
    page_title="Vigia da Colmeia",
    page_icon="🐝",
    layout="wide"
)

# ======================================
# AUTO UPDATE
# ======================================

st.empty()

# ======================================
# LOGO CENTRALIZADA
# ======================================

col1, col2, col3 = st.columns([1,2,1])

with col2:

    st.image(
        "logo.jpg",
        width=350
    )

# ======================================
# TÍTULO
# ======================================

st.title("🐝 Vigia da Colmeia")

st.caption(
    "Monitoramento inteligente de colmeias em tempo real"
)

# ======================================
# CONECTA NO SQLITE
# ======================================

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

conn.close()

# ======================================
# VERIFICA SE EXISTEM DADOS
# ======================================

if df.empty:

    st.warning(
        "⏳ Aguardando dados..."
    )

else:

    # COLMEIAS


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


    if diferenca > 60:

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