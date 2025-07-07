import streamlit as st

st.set_page_config(page_title="موقعي البسيط", page_icon="🚀")

st.title("✨ أهلاً بك في موقعي")
st.subheader("تطبيق بسيط باستخدام Streamlit")

name = st.text_input("ما اسمك؟")
if name:
    st.success(f"مرحباً، {name}!")
