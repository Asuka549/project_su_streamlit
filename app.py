import streamlit as st

# 頁面標題（可選）
st.set_page_config(page_title="Dockerized Streamlit")

# 顯示 JSON 格式的訊息
data = {"message": "Hello, Dockerized Flask!"}
st.json(data)