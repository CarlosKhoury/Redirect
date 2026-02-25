import streamlit as st
import streamlit.components.v1 as components

RAILWAY_URL = "golf-swing-analyzer.up.railway.app"

components.html(
    f"""
    <script>
        window.top.location.href = "{RAILWAY_URL}";
    </script>
    """,
    height=0,
)

st.stop()
