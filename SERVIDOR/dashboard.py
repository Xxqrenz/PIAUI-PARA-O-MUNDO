import streamlit as st
import sqlite3
import pandas as pd
import time

st.set_page_config(
    page_title="Vigia da Colmeia",
    page_icon="🐝",
    layout="wide"
)

st.title("🐝 Vigia da Colmeia")

st.markdown(
    "Monitoramento inteligente de colmeias em tempo real"
)



placeholder = st.empty()



while True:


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

    if not df.empty:



        colmeias = sorted(
            df["colmeia"].unique()
        )

        with placeholder.container():
            st.header("📊 Resumo Geral")

            total_colmeias = len(colmeias)

            alertas = len(
                df[
                    df["alerta"] != "NORMAL"
                ]
            )

            media_temp = round(
                df["temperatura"].mean(),
                1
            )

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "Colmeias Ativas",
                total_colmeias
            )

            col2.metric(
                "Temperatura Média",
                f"{media_temp} °C"
            )

            col3.metric(
                "Alertas Ativos",
                alertas
            )

            st.divider()

            for colmeia in colmeias:

                dados_colmeia = df[
                    df["colmeia"] == colmeia
                ]

                ultima = dados_colmeia.iloc[0]

                st.subheader(
                    f"🐝 Colmeia {colmeia}"
                )

                c1, c2, c3 = st.columns(3)


                c1.metric(
                    "Temperatura",
                    f"{ultima['temperatura']} °C"
                )

                c2.metric(
                    "Som",
                    f"{ultima['som']}"
                )

                alerta = ultima["alerta"]

                c3.metric(
                    "Status",
                    alerta
                )

                if alerta == "NORMAL":

                    st.success(
                        "✅ Colmeia operando normalmente"
                    )

                elif alerta == "SUPERAQUECIMENTO":

                    st.error(
                        "🔥 Temperatura crítica detectada"
                    )

                elif alerta == "ESTRESSE SONORO":

                    st.warning(
                        "🔊 Atividade sonora anormal"
                    )

                elif alerta == "POSSIVEL ENXAMEACAO":

                    st.error(
                        "⚠️ Possível enxameação detectada"
                    )

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

                with st.expander(
                    f"📜 Histórico Colmeia {colmeia}"
                ):

                    st.dataframe(
                        dados_colmeia[
                            [
                                "temperatura",
                                "som",
                                "alerta",
                                "data"
                            ]
                        ],
                        use_container_width=True
                    )

                st.divider()
    else:

        with placeholder.container():

            st.warning(
                "⏳ Aguardando dados das colmeias..."
            )

    time.sleep(2)