import streamlit as st
import streamlit.components.v1 as components

# 1. Configuration
TARGET_URL = "https://golf-swing-analyzer.up.railway.app"

st.set_page_config(page_title="Redirecting...", page_icon="🏌️")

# --- UI CONTENT ---
st.title("Moving to our new home! 🚀")
st.write(f"The AI Golf Swing Analyzer has moved to: **{TARGET_URL}**")

# The Manual Fallback Button
st.link_button("Go to New Site Now", TARGET_URL, type="primary", use_container_width=True)

st.divider()
st.info("We are redirecting you automatically. If nothing happens within 3 seconds, please click the button above.")

# --- THE AUTO-REDIRECT LOGIC ---

# A. The JavaScript Method (Immediate)
js_code = f"""
    <script>
        setTimeout(function(){{
            window.top.location.href = '{TARGET_URL}';
        }}, 1000);
    </script>
"""
components.html(js_code, height=0)

# B. The Meta Refresh Method (Backup)
# This lives in the Markdown and acts as a secondary trigger
st.markdown(f'<meta http-equiv="refresh" content="2; url={TARGET_URL}">', unsafe_allow_html=True)

# C. Hide Streamlit UI elements for a cleaner "Landing Page" look
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)
