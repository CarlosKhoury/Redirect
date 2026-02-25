import streamlit as st

# Replace this with your actual Railway URL
RAILWAY_URL = "golf-swing-analyzer.up.railway.app"

# Immediate redirect using JavaScript (cleanest method)
st.markdown(f"""
<script>
    window.location.replace("{RAILWAY_URL}");
</script>
""", unsafe_allow_html=True)

# Fallback in case JS is disabled
st.markdown(f"""
<meta http-equiv="refresh" content="0; url={RAILWAY_URL}">
""", unsafe_allow_html=True)

# Stop Streamlit from rendering anything else
st.stop()
