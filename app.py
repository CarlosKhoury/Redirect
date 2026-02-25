import streamlit as st
import streamlit.components.v1 as components

def redirect_to(url):
    """
    Redirects the user's browser to the specified URL.
    Uses window.parent to break out of the Streamlit iframe.
    """
    js = f"window.parent.location.href = '{url}';"
    html = f"<script>{js}</script>"
    components.html(html)

# Add a message so the user knows what is happening
st.title("Redirecting...")
st.write("If you are not redirected automatically, please wait a moment.")

# Call the redirect function with your target website
target_website = "golf-swing-analyzer.up.railway.app" 
redirect_to(target_website)
