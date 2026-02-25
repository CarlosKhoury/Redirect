importimport streamlit as st
import streamlit.components.v1 as components

RAILWAY_URL = "golf-swing-analyzer.up.railway.app"

st.write("Redirecting to our new site...")

components.html(
    f"""
    <script>
        window.location.replace("{RAILWAY_URL}");
    </script>
    """,
    height=0,
)

st.stop()
