import streamlit as st
from PIL import Image
import io

# 全域頁面設定
st.set_page_config(
    page_title="圖片灰階轉換器",
    page_icon="🖤",
    layout="centered"
)

st.title("📷 圖片灰階轉換器")
st.write("上傳一張照片，馬上轉成灰階並下載！")

# 1. 上傳檔案
uploaded_file = st.file_uploader(
    "請上傳照片（JPG/PNG）", 
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    # 2. 讀取並顯示原圖
    image = Image.open(uploaded_file)
    st.subheader("原始圖片")
    st.image(image, use_column_width=True)

    # 3. 轉成灰階並顯示
    gray_image = image.convert("L")
    st.subheader("灰階圖片")
    st.image(gray_image, use_column_width=True)

    # 4. 準備下載
    buf = io.BytesIO()
    gray_image.save(buf, format="PNG")
    byte_data = buf.getvalue()

    st.download_button(
        label="⬇️ 下載灰階圖片",
        data=byte_data,
        file_name="gray_image.png",
        mime="image/png"
    )
