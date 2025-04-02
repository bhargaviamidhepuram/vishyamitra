import streamlit as st
from pandasai.connectors import SQLConnector
import pandas as pd
st.set_page_config(layout="wide", page_title="VISHAYAMITRA", page_icon="🧠")
st.sidebar.page_link("app.py", label="Home", icon="🏠")
st.sidebar.page_link("pages/home.py", label="ChatBI", icon="💬")
st.sidebar.page_link("pages/pattern.py", label="Pattern Identifier", icon="📈")
st.sidebar.page_link("pages/visualization.py", label="Data Visualizer", icon="✨")
st.sidebar.page_link("pages/sqldata.py", label="Database Connector", icon="💽")


def get_sql_connection(url, database,username, password, table):
    try:
        sql_connector = SQLConnector(
        config={
            "host": url,
            "port": 3306,
            "database": database,
            "username": username,
            "password": password,
            "table": table,
            
        }
    )
    except:
        st.write("Please check the connection details and try again.")
    return sql_connector

st.title(":orange[Vishayamitra] Database Connector")
with st.container():
    st.title("Database Connector")
    st.write("Connect to your SQL database to retrieve data.")
    url = st.text_input("Enter the URL of the SQL database:")
    database = st.text_input("Enter the name of the database")
    username = st.text_input("Enter the username:")
    password = st.text_input("Enter the password:", type="password")
    table = st.text_input("Enter the table name:")
    if st.button("Connect"):
        sql_connector = get_sql_connection(url, database, username, password, table)
        sql_connection = sql_connector.connect()
        st.write("SQL database connection successful!")
        query = "SELECT * FROM "+table
        df = pd.read_sql(query, sql_connection)
        st.dataframe(df)
        sql_connector.close()
    else:
        st.write("Please enter the connection details and click the 'Connect' button.")
    

