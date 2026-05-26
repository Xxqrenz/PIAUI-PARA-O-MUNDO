import streamlit as st
import sqlite3
import pandas as pd
import time

st.set_page_config(
    page_title="Vigia da Colmeia",
    layout="wide"
)

st.title("🐝 Vigia da Colmeia")

placeholder = st.empty()

while True:

    conn = sqlite3.connect(
        "colmeia.db"
    )

    query = """

    SELECT *
    FROM leituras

    ORDER BY id DESC

    LIMIT 20

    """

    df = pd.read_sql_query(
        query,
        conn
    )

    conn.close()

    if not df.empty:

        ultima = df.iloc[0]

        with placeholder.container():

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "Temperatura",
                f"{ultima['temperatura']} °C"
            )

            col2.metric(
                "Som",
                f"{ultima['som']}"
            )

            col3.metric(
                "Status",
                ultima['alerta']
            )

            st.subheader(
                "Histórico"
            )

            st.dataframe(df)

            st.subheader(
                "Temperatura"
            )

            st.line_chart(
                df["temperatura"]
            )

            st.subheader(
                "Som"
            )

            st.line_chart(
                df["som"]
            )

    time.sleep(2)