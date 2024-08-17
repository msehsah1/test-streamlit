import streamlit as st
import numpy as np

"""
with st.chat_message("ai"):
    st.write("Hello 👋")
    st.line_chart(np.random.randn(30, 3))

message = st.chat_message("assistant")
message.write("Hello human")
message.bar_chart(np.random.randn(30, 3))
"""


prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")